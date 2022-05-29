import sys
from pathlib import Path
from typing import Optional

dir_path = Path(__file__).absolute().parent.parent
sys.path.append(str(dir_path))

from branen.Card import Card


class HistoryFrame:
    def __init__(self, suit: Optional[str] = None, value: Optional[str] = None) -> None:
        if suit is not None and value is not None:
            self.card = Card(suit, value)
        else:
            self.card = None

    def is_claim(self) -> bool:
        return self.card is None

    def get_card(self) -> Card:
        if self.is_claim():
            raise Exception("The round is claimed")

        return self.card
