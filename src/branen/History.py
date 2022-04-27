from __future__ import annotations

import sys
from pathlib import Path

dir_path = Path(__file__).absolute().parent.parent
sys.path.append(str(dir_path))


from branen.Card import Card
from typing import List, Union


class History:
    def __init__(self, history: List[Union[Card, str]]) -> None:
        self.history = history
        self.index = 0

    def next(self) -> Union[Card, str]:
        ++self.index

        if self.index >= len(self.history):
            raise StopIteration

        return self.get_current_card()

    def get_current_card(self) -> Union[Card, str]:
        return self.history[self.index]

    def __iter__(self):
        return iter(self.history)

    def __next__(self):
        return self.next()

    def reset(self) -> None:
        self.index = 0

    def set_index(self, index: int) -> None:
        self.index = index

    def move_to_card(self, card: Union[Card, str]) -> None:
        for i, c in enumerate(self.history):
            if c == card:
                self.index = i
                return
