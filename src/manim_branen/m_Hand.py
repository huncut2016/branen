from src.branen.Hand import Hand
from src.branen.Card import Card
from .m_Card import m_Card
from manim import VGroup
from manim.constants import DOWN, LEFT
from typing import List

TABLE_TYPE = ["CARD", "DIAGRAM"]


class m_Hand(VGroup):
    def __init__(
        self, hand: List[Card] = None, hand_type: str = TABLE_TYPE[1], **kwargs
    ):
        if hand is None:
            raise ValueError("Hand can not be None")
        self.hand = Hand(hand)
        self.hand.sort(True)

        SUITS = ["S", "H", "D", "C"]

        vmobjects = VGroup()

        for suit in SUITS:
            HAND = VGroup(
                *[
                    m_Card(card=card, card_type=hand_type)
                    for card in hand
                    if card.get_suit() == suit
                ]
            )
            HAND.arrange()
            vmobjects.add(HAND)

        vmobjects.arrange(DOWN, aligned_edge=LEFT)

        super().__init__(vmobjects, **kwargs)
