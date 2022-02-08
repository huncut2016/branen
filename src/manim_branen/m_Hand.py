from src.branen.Hand import Hand
from src.branen.Card import Card
from m_Card import m_Card
from manim import VGroup
from typing import List


class m_Hand(VGroup):
    def __int__(self, hand: List[Card], **kwargs):
        self.hand = Hand(hand)
        vmobjects = [m_Card(card) for card in hand]

        super().__init__(*vmobjects, **kwargs)
