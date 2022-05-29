import sys
from pathlib import Path

dir_path = Path(__file__).absolute().parent.parent / "src"
sys.path.append(str(dir_path))


from manim import *
from random import shuffle

from manim_branen.m_Card import m_Card
from branen.Card import Card
from branen.Hand import Hand
from manim_branen.m_Hand import m_Hand
from manim_branen.m_Table import m_Table
from branen_tools.lin_parser import LinParser
from typing import List

TEST_DATAS: Path = Path(__file__).absolute().parent / "test_datas"
suits: List[str] = ["S", "H", "D", "C"]
values: List[str] = [
    *["A", "K", "Q", "J", "T"],
    *[str(i) for i in range(2, 10)],
]


class Test_Card(Scene):
    def construct(self):
        c = m_Card("H", "T", card_type="DIAGRAM").center()
        sq = Square().center()

        self.play(Create(c), Create(sq))

        self.play(c.play(sq, LEFT))
        self.wait()


class Test_Hand(Scene):
    def construct(self):
        hands = [
            Card(suit, value) for suit in suits for value in values
        ]  # creating random hands
        shuffle(hands)

        h = m_Hand(hands[:13], hand_type="DIAGRAM").arrange_in_grid(3, 5)

        self.wait()
        self.play(Create(h))
        self.wait()


class Test_Table(Scene):
    def construct(self):
        hands = [
            Card(suit, value) for suit in suits for value in values
        ]  # creating random hands
        shuffle(hands)

        hands_input = {
            "E": Hand(hands[:13]),
            "W": Hand(hands[13:26]),
            "N": Hand(hands[26:39]),
            "S": Hand(hands[39:]),
        }

        t = m_Table(hands_input)

        self.play(Create(t))
        self.wait()


class Table_play_test(Scene):
    def construct(self):
        lp: LinParser = LinParser(path=str(TEST_DATAS / "test1.lin")).parse()

        board, deal, vulnerable, play = lp.get_all()

        t = m_Table(deal)
        self.play(FadeIn(t))

        for _ in range(52):
            current_card = play.get_current_card()
            if current_card.is_claim():
                break

            self.play(t.play_card(current_card.get_card()))
            play.next()

        self.wait()
