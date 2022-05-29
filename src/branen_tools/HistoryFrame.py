import sys
from pathlib import Path
from typing import Optional

dir_path = Path(__file__).absolute().parent.parent
sys.path.append(str(dir_path))

from branen.Card import Card


class HistoryFrame:
    def __init__(
        self,
        claimed: Optional[str] = None,
        suit: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        self.claimed = claimed

        if suit is not None and value is not None:
            self.card = Card(suit, value)
        elif claimed is not None:
            self.card = None

    def is_claim(self) -> bool:
        return self.claimed is not None

    def get_card(self) -> Card:
        if self.is_claim():
            raise Exception("The round is claimed")

        return self.card

    def __str__(self) -> str:
        if self.is_claim():
            return self.claimed

        return str(self.card)

    def __repr__(self) -> str:
        return self.__str__()
