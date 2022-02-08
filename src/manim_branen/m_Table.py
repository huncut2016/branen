from src.branen.Table import Table
from src.branen.Hand import Hand

from manim import VGroup
from typing import Dict

raise NotImplementedError("This module is not implemented yet!")


class m_Table(VGroup):
    def __int__(
        self,
        hands: Dict[str, Hand] = None,
        dealer: str = "N",
        trump: str = None,
        **kwargs
    ):
        self.table = Table(hands, dealer, trump)
        super().__init__(**kwargs)
