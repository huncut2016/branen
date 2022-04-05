import os

from manim import SVGMobject, VGroup, Text, VMobject
from manim.utils import color

from statistics import mean
from branen.Card import Card

TABLE_TYPE = ["CARD", "DIAGRAM"]
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


class m_Card(VGroup):
    """branen is one of the basic building blocks of branen.
    This object represents the French card in the bridge, not the bidding card!

    Examples
    --------
    .. code-block:: python
        my_card = m_Card(suit="H", value="A")

    Parameters
    --------
    suit : :class:`str`
        This is the suit of the card. It can be: `S`, `H`, `D`, `C`
    value : :class:`str`
        This is the value of the card. It can be: `A`, `K`, `Q`, `J`, `T`, `9`, `...` , `2`
    """

    def __init__(
        self,
        suit: str = None,
        value: str = None,
        card: Card = None,
        card_type: str = TABLE_TYPE[0],
        **kwargs,
    ):
        if card is not None:
            self.card = card
        else:
            if suit is None:
                raise ValueError("Suit can not be None")
            if value is None:
                raise ValueError("Value can not be None")

            self.card = Card(suit, value)

        if not card_type in TABLE_TYPE:
            raise ValueError(f"Card type must be {', or'.join(TABLE_TYPE)}")

        self.card_type = card_type

        if card_type == "CARD":
            super().__init__(self.card_view(), **kwargs)
        else:
            super().__init__(self.diagram_view(), **kwargs)

    def fullCard(self):
        suit = UNICODE_MAP[self.card.get_suit()]
        value = self.card.value
        card = Text(f"{suit}{10 if value == 'T' else value}").scale(0.5)
        color_of_suit = SUIT_COLOR_MAP["dark"][self.card.get_suit()]

        card[0].set_color(color.Color(color_of_suit))
        return card

    def cardSymbol(self):
        value = self.card.value
        card = Text(f"{10 if value == 'T' else value}").scale(0.5)

        return card

    def diagram_view(self):
        return self.cardSymbol() if self.card_type == TABLE_TYPE[1] else self.fullCard()

    def card_view(self):
        file_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "media",
            "cards",
            f"{self.card.suit}{self.card.value}.svg",
        )

        return SVGMobject(file_path)

    def play(self, table: VMobject, dir):
        self.card.play()
        pos = (table.get_center() + table.get_edge_center(dir)) / 2
        return self.animate.move_to(pos)
