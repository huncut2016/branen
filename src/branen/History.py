from __future__ import annotations

import sys
from pathlib import Path

dir_path = Path(__file__).absolute().parent.parent
sys.path.append(str(dir_path))


from branen.Card import Card
from branen_tools.HistoryFrame import HistoryFrame
from typing import List, Union


class History:
    def __init__(self, history: List[HistoryFrame]) -> None:
        self.history = history
        self.index = 0

    def next(self) -> HistoryFrame:
        self.index += 1

        if self.index >= len(self.history):
            raise StopIteration

        return self.get_current_card()

    def get_current_card(self) -> HistoryFrame:
        card = self.history[self.index]

        return card

    def __iter__(self):
        return iter(self.history)

    def __next__(self):
        return self.next()

    def reset(self) -> None:
        self.index = 0

    def set_index(self, index: int) -> None:
        self.index = index

    def move_to_card(self, card: HistoryFrame) -> None:
        for i, c in enumerate(self.history):
            if c == card:
                self.index = i
                return

    def __str__(self) -> str:
        return str(self.history)

    def __repr__(self) -> str:
        return self.__str__()
