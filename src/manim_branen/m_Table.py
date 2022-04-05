from branen.Card import Card
from branen.Table import Table
from branen.Hand import Hand
from manim_branen.m_Hand import m_Hand

from warnings import warn
from manim import VGroup, Square, Animation
from manim.constants import UP, DOWN, RIGHT, LEFT
from manim.utils import color
from typing import Dict
import inspect

from manim_branen.m_Card import m_Card


TABLE_TYPE = ["CARD", "DIAGRAM"]
quarter_to_dir = {"N": UP, "S": DOWN, "E": RIGHT, "W": LEFT}

UNICODE_MAP = {
    "S": "♠",
    "H": "♥",
    "D": "♦",
    "C": "♣",
}

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


class m_Table(VGroup):
    def __init__(
        self,
        hands: Dict[str, Hand] = None,
        dealer: str = "N",
        trump: str = None,
        table_type: str = TABLE_TYPE[1],
        **kwargs,
    ):
        table_type = table_type.upper()
        self.table_type = table_type

        if not table_type in TABLE_TYPE:
            raise ValueError(f"Table type must be {', or'.join(TABLE_TYPE)}")

        self.table = Table(hands, dealer, trump)

        self.hands = VGroup()

        if table_type == "CARD":
            self.hands = self.card_view()
        else:
            self.hands = self.diagram_view()[1:]

        super().__init__(self.hands, **kwargs)

    def diagram_view(self) -> VGroup:
        table = self.table
        sq = Square().center()
        gr = VGroup(sq)

        for quarter, hand in table.get_hands().items():
            h = m_Hand(hand).next_to(sq, quarter_to_dir[quarter] * 4)
            gr.add(h)

        return gr

    def card_view(self) -> VGroup:
        func_name = inspect.stack()[0][3]  # the name of this function
        raise NotImplementedError(f"{func_name} is not implemented yet!")

    def get_center_table(self) -> Square:
        t = self.submobjects[0][0]
        if not isinstance(t, Square):
            raise Exception("Table is not initialized yet!")

        return t

    def play_card(self, card: Card) -> Animation:
        ## TODO
        func_name = inspect.stack()[0][3]  # the name of this function
        raise NotImplementedError(f"{func_name} is not implemented yet!")
        self.table.play_card(card)

        for hand in self.hands:
            print(hand)
