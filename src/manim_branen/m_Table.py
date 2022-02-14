from src.branen.Table import Table
from src.branen.Hand import Hand

from warnings import warn
from manim import VGroup
from manim.constants import UP, DOWN, RIGHT, LEFT
from typing import Dict
import inspect

warn("This module is not implemented yet!")

TABLE_TYPE = ["CARD", "DIAGRAM"]
quarter_to_dir = {"N": UP, "S": DOWN, "E": RIGHT, "W": LEFT}


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

    def diagram_view(self):
        # TODO create table
        pass

    def card_view(self):
        func_name = inspect.stack()[0][3]  # the name of this function
        raise NotImplementedError(f"{func_name} is not implemented yet!")
