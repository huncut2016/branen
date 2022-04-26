from __future__ import annotations

import sys
from pathlib import Path

dir_path = Path(__file__).absolute().parent.parent
sys.path.append(str(dir_path))


import inspect
from typing import Dict, List, Optional
from warnings import warn

from branen.Card import Card
from branen.Hand import Hand

# TODO dealer is not declarer
class Table:
    NEXT = {"N": "E", "E": "S", "S": "W", "W": "N"}

    def __init__(
        self,
        hands: Dict[str, Hand] = None,
        dealer: str = "N",
        declarer: str = "N",
        trump: str = None,
        curRound: int = 1,
    ):
        if hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.hands = hands
        self.dealer = dealer
        self.declarer = declarer
        self.current_player = dealer
        self.starting_suit: Optional[str] = None
        self.round = curRound
        self.in_play: List[Card] = []
        self.trump = trump

    def play_card_index(self, card_index: int) -> None:
        """
        Play a card depend on an index.

        Parameters
        ----------
        card_index: :class: `int`
            The index of the card, that you want to play.
        """

        if self.is_end_of_round():
            self.end_the_round()

        playing_hand = self.hands[self.current_player]  # the hand who are coming
        card = playing_hand[card_index]

        if self.starting_suit is None:
            self.starting_suit = card.get_suit()

        self.is_valid_play(card)  # Check that playing the card is meets the rules

        card.play()

        self.current_player = self.NEXT[self.current_player]
        self.in_play.append(card)

        self.round += 1

    def is_end_of_round(self) -> bool:
        return self.round == 4

    def end_the_round(self) -> None:
        winning_card = self.win_the_trick()
        for quarter, hand in self.hands.items():
            if hand.has_card(winning_card):
                self.current_player = quarter

        self.round = 1
        self.starting_suit = None
        self.in_play = []

    def win_the_trick(self) -> Card:
        if self.starting_suit is None:
            raise Exception("Starting suit is None")

        biggest = self.in_play[0]

        for card in self.in_play[1:]:
            if card.is_trick(biggest, self.starting_suit, self.trump):
                biggest = card

        return biggest

    def is_valid_play(self, card: Card) -> None:
        """
        Check that playing the card is meets the rules
        Parameters
        ----------
        card
            The card, that you want to play

        Returns
        -------
            Nothing
        """
        if self.starting_suit is None:
            raise Exception("Starting suit is None!")

        playing_hand = self.hands[self.current_player]

        if self.round != 1:  # not the first round
            if (
                playing_hand.has_suit(self.starting_suit)
                and card.get_suit() != self.starting_suit
            ):
                raise Exception(
                    f"{self.current_player} has {self.starting_suit} suit, but the card is {card.get_suit()}"
                )

        if not playing_hand.has_card(card):
            raise Exception(f"{self.current_player} has no card {card}")

    def play_card(self, card: Card) -> None:

        if not self.hands[self.current_player].has_card(card):
            raise Exception(
                f"Current hand: {self.current_player} has not this card: {card}!"
            )

        self.play_card_index(self.hands[self.current_player].get_card_index(card))

    def reset(self, dealer: str = "N") -> None:
        """
        Reset the table
        """

        self.dealer = dealer
        self.current_player = dealer

        for key in self.hands:
            cards: Hand = self.hands[key]

            for card in cards:
                card.reset()

    def set_dealer(self, dealer: str = "N") -> None:
        self.dealer = dealer

    def get_current_player(self) -> str:
        return self.current_player

    def get_dealer(self) -> str:
        return self.dealer

    def get_hands(self) -> Dict[str, Hand]:
        return self.hands.copy()

    def set_E(self, E: Hand) -> None:
        self.hands["E"] = E

    def set_W(self, W: Hand) -> None:
        self.hands["W"] = W

    def set_N(self, N: Hand) -> None:
        self.hands["N"] = N

    def set_S(self, S: Hand) -> None:
        self.hands["S"] = S

    def __str__(self):
        return str(self.hands)

    def __repr__(self):
        return self.__str__()
