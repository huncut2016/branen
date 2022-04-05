from branen.Hand import Hand
from branen.Card import Card
from .m_Card import UNICODE_MAP, m_Card
from manim import VGroup, Text
from manim.utils import color
from manim.constants import DOWN, LEFT
from typing import List, Union, Dict

TABLE_TYPE = ["CARD", "DIAGRAM"]
SUIT_COLOR_MAP = {
    "dark": {
        "S": color.WHITE,
        "H": color.RED,
        "D": color.RED,
        "C": color.WHITE,
    },
    "light": {
        "S": color.BLACK,
        "H": color.RED,
        "D": color.RED,
        "C": color.BLACK,
    },
}


class m_Hand(VGroup):
    def __init__(
        self,
        hand: Union[List[Card], Hand] = None,
        hand_type: str = TABLE_TYPE[1],
        **kwargs,
    ):
        if hand is None:
            raise ValueError("Hand can not be None")

        if isinstance(hand, Hand):
            self.hand = hand
        else:
            self.hand = Hand(hand)

        self.hand.sort(True)

        SUITS = ["S", "H", "D", "C"]

        vmobjects = VGroup()
        ## TODO
        self.m_hand: List[m_Card] = []

        for suit in SUITS:
            suit_symbol = Text(f"{UNICODE_MAP[suit]}").scale(0.5)
            color_of_suit = SUIT_COLOR_MAP["dark"][suit]
            suit_symbol.set_color(color.Color(color_of_suit))

            m_cards = [
                m_Card(card=card, card_type=hand_type)
                for card in hand
                if card.get_suit() == suit
            ]

            self.m_hand += m_cards

            row = VGroup(suit_symbol, *m_cards)
            row.arrange()
            vmobjects.add(row)

        vmobjects.arrange(DOWN, aligned_edge=LEFT)

        super().__init__(vmobjects, **kwargs)

    def __iter__(self):
        return iter(self.m_hand)
