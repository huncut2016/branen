from __future__ import annotations

import sys
from pathlib import Path

dir_path = Path(__file__).absolute().parent.parent
sys.path.append(str(dir_path))


from branen.Card import Card
from typing import List


class History:
    def __init__(self, history: List[Card]) -> None:
        self.history = history
