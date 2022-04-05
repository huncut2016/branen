from manim import *
from random import shuffle

import sys

sys.path.append("../src")

from manim_branen.m_Card import m_Card
from branen.Card import Card
from branen.Hand import Hand
from manim_branen.m_Hand import m_Hand
from manim_branen.m_Table import m_Table
from typing import List

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

        self.play(FadeIn(t))
        self.play(t.play_card(hands[27]))
        self.play(t.play_card(hands[0]))
        self.wait()
