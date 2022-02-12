from src.branen.Table import Table
from src.branen.Hand import Hand

from warnings import warn
from manim import VGroup
from typing import Dict

warn("This module is not implemented yet!")

TABLE_TYPE = ["CARD", "DIAGRAM"]


class m_Table(VGroup):
    def __init__(
        self,
        hands: Dict[str, Hand] = None,
        dealer: str = "N",
        trump: str = None,
        table_type: str = TABLE_TYPE[0],
        **kwargs,
    ):
        table_type = table_type.upper()
        self.table_type = table_type

        if not table_type in TABLE_TYPE:
            raise ValueError(f"Table type must be {', or'.join(TABLE_TYPE)}")

        self.table = Table(hands, dealer, trump)
        super().__init__(**kwargs)
