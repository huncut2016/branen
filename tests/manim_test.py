from manim import *
from random import shuffle
from src.manim_branen.m_Card import m_Card
from src.branen.Card import Card
from src.manim_branen.m_Hand import m_Hand


class Test(Scene):
    def construct(self):
        suits: List[str] = ["S", "H", "D", "C"]
        values: List[str] = [
            *["A", "K", "Q", "J", "T"],
            *[str(i) for i in range(2, 10)],
        ]

        hands = [
            Card(suit, value) for suit in suits for value in values
        ]  # creating random hands
        shuffle(hands)

        h = m_Hand(hands[:13], hand_type="DIAGRAM").arrange_in_grid(3, 5)
        c = m_Card("H", "T", card_type="DIAGRAM").center()

        self.play(Create(c))
        self.wait()
        self.remove(c)
        self.play(Create(h))
        self.wait()
