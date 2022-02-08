import os

from manim import SVGMobject

from src.branen.Card import Card


class m_Card(SVGMobject):
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
        self, card: Card = None, suit: str = None, value: str = None, **kwargs
    ):
        if Card is not None:
            self.card = card
        else:
            self.card = Card(suit, value)

        file_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "media",
            "cards",
            f"{self.suit}{self.value}.svg",
        )

        super().__init__(file_name=file_path, **kwargs)
