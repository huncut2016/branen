# Source: https://github.com/kevinywlui/lin2pbn

# raise NotImplementedError("This module is not implemented yet!")
from __future__ import annotations

import sys
from pathlib import Path

dir_path = Path(__file__).absolute().parent.parent
sys.path.append(str(dir_path))


import re
from typing import Dict, Optional, List, Tuple, Union
import textwrap
from branen.Table import Table
from branen.Hand import Hand
from branen.Card import Card
from branen.History import History


def numToDirection(n):
    return ["S", "W", "N", "E"][n % 4]


class LinParser:
    """LinParser converts a .lin file to a branen data structure."""

    def __init__(
        self, linstring: Optional[str] = None, path: Optional[str] = None
    ) -> None:
        if (linstring is None) and (path is None):
            raise ValueError(
                f"You need to give a .lin structured string, or a path to the .lin file."
            )

        if (linstring is not None) and (path is not None):
            raise ValueError(
                f"""
                linstring ({textwrap.shorten(linstring, width=50, placeholder="...")}) 
                and path ({textwrap.shorten(path, width=50, placeholder="...")})
                cannot have value in the same time!
            """
            )

        if linstring is not None:  # if a string given
            self.linstring = linstring

        if path is not None:  # if a file given
            self.path = path
            with open(path, "r") as file:
                self.linstring = file.read()

        self.board: int
        self.deal: Table
        # TODO vulnerable must be string
        self.vulnerable: str
        self.play: History

    def parse(self) -> LinParser:
        """Parses the .lin to a manageable format."""
        ## Start of the Black Box

        linstring = self.linstring

        linList = linstring.split("||")

        # Extract Players SWNE
        [south, west, north, east] = linList[0].split("|")[1].split(",")

        # Extract hands
        dd = linList[1].split("|")[1].split(",")
        hands = [list(map(lambda x: x[::-1], re.split("S|H|D|C", d))) for d in dd]
        [dealerIndex, _, _, _] = [x.pop(0) for x in hands]
        dealerIndex = int(dealerIndex)
        dealer = numToDirection(dealerIndex - 1)
        if len(hands[3]) == 0:
            rank = "AKQJT98765432"
            hands[3] = 4 * [""]
            for i in range(4):
                for j in range(13):
                    if all([rank[j] not in hands[k][i] for k in range(3)]):
                        hands[3][i] = hands[3][i] + rank[j]
        # deal = dealer + ":" + " ".join([".".join(x) for x in hands])
        deal = hands

        # Extract auction
        aa = linList[2].split("|")[1::2]
        board = aa[0].split(" ")[1]
        if aa[1] == "o":
            vulnerable = "None"
        elif aa[1] == "e":
            vulnerable = "ES"
        elif aa[1] == "n":
            vulnerable = "NS"
        else:
            vulnerable = "All"

        bids = aa[2::]
        bids = ["Pass" if x == "p" else x for x in bids]
        auction = ""
        for i in range(len(bids) // 4):
            t = ["", "", "", ""]
            for j in range(4):
                if 4 * i + j < len(bids):
                    t[j] = bids[4 * i + j]
            auction = auction + "{0[0]:<7}{0[1]:<7}{0[2]:<7}{0[3]:<7}\n".format(t)

        stake = ""
        for x in bids[::-1]:
            if x == "XX":
                stake = "XX"
                continue
            if x == "X" and stake != "XX":
                stake = "X"
                continue
            if x[1] in ["S", "H", "C", "D", "N"]:
                self.contract = x + stake
                strain = x[1:]
                break

        for x in bids:
            if x[1:] == strain:
                declarerIndex = bids.index(x)
                break
        declarer = ["S", "W", "N", "E"][(declarerIndex + dealerIndex - 1) % 4]

        # Extract play
        pp = linList[3:]
        pp = [p.split("|")[1::2] for p in pp]
        if pp[-1] == []:
            claim = 0
        else:
            claim = pp[-1][-1]

        play = []
        for x in pp:
            if x == []:
                continue
            t = [""] * 4
            for j in range(len(x)):
                t[j] = x[j]
            #######################
            play += t
            #######################
            # print(f"t = {t} \n play = {play}")
        # play = play + "{0[0]:<4}{0[1]:<4}{0[2]:<4}{0[3]:<4}".format(t)

        # play = [numToDirection(declarerIndex + 1), play]

        play = list(filter(lambda n: n != "", play))

        ## End of the Black Box

        self.board = int(board)
        self.declarer = declarer
        self.dealer = dealer
        self.play = self.preprocess_play(play)
        self.vulnerable = vulnerable
        self.deal = self.preprocess_deal(deal)

        return self

    def is_claim(self, card: str):
        suits = ["S", "H", "D", "C"]

        return card[0] not in suits

    def preprocess_play(self, play: List[str]) -> History:
        history = []

        for c in play:
            if len(c) > 2 or len(c) < 1:
                raise ValueError(f"The card is not in correct format! ({c})")

            if self.is_claim(c):
                history.append(c)
            else:
                history.append(Card(c[0], c[1]))

        return History(history=history)

    def preprocess_deal(self, deal: List[List[str]]) -> Table:
        q = ["S", "W", "N", "E"]
        suits = ["S", "H", "D", "C"]

        hands: Dict[str, Hand] = {}

        for quarter, cards in enumerate(q):
            hand = Hand(
                [
                    Card(suit=suits[suit], value=v)
                    for suit in range(4)
                    for v in deal[quarter][suit]
                ]
            )

            hands[q[quarter]] = hand

        #############################
        # TODO trump
        #############################

        return Table(
            hands, trump=self.contract[0], dealer=self.dealer, declarer=self.declarer
        )

    def get_board(self) -> int:
        if self.board is None:
            raise Exception("First call the parse method!")

        return self.board

    def get_deal(self) -> Table:
        if self.board is None:
            raise Exception("First call the parse method!")

        return self.deal

    def get_vulnerable(self) -> str:
        if self.board is None:
            raise Exception("First call the parse method!")

        return self.vulnerable

    def get_play(self) -> History:
        if self.board is None:
            raise Exception("First call the parse method!")

        return self.play

    def get_all(self) -> Tuple[int, Table, str, History]:
        return (self.board, self.deal, self.vulnerable, self.play)
