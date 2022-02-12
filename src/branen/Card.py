from __future__ import annotations
import inspect
from functools import total_ordering
from typing import Optional


@total_ordering
class Card:
    SUIT_MAP = {"S": 3, "H": 2, "D": 1, "C": 0}
    VALUE_MAP = {
        **{"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10},
        **{str(i): i for i in range(2, 15)},
    }

    is_played = False

    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def set(self, suit: str, value: str) -> Card:
        self.suit = suit
        self.value = value

        return self

    def get_suit(self) -> str:
        return self.suit

    def reset(self) -> None:
        self.set_is_played(False)
        self.set_played_turn(0)

    def play(self) -> None:
        if self.is_played:
            Exception("This card was played!")

        self.set_is_played(True)

    def set_played_turn(self, turn: int) -> None:
        self.turn = turn

    def get_is_played(self) -> bool:
        return self.is_played

    def set_is_played(self, p) -> None:
        self.is_played = p

    def get_value(self) -> str:
        return self.value

    def set_value(self, value: str) -> None:
        if len(value) != 1:
            raise Exception(
                f"The length of Card value name must be 1! (value name = {value})"
            )

        if not value in self.VALUE_MAP:
            raise Exception(f"Unknown value type (value name = {value})")

        self.value = value.upper()

    def set_suit(self, suit: str) -> None:
        if len(suit) != 1:
            raise Exception(
                f"The length of Card suit name must be 1! (suit name = {suit})"
            )

        if not suit in self.SUIT_MAP:
            raise Exception(f"Unknown suit type (suit name = {suit})")

        self.suit = suit.upper()

    def get_card(self):
        func_name = inspect.stack()[0][3]  # the name of this function
        raise NotImplementedError(f"{func_name} is not implemented yet!")

    def __lt__(self, other) -> bool:

        oval = self.VALUE_MAP[other.get_value()]
        osu = self.SUIT_MAP[other.get_suit()]

        sval = self.VALUE_MAP[self.value]
        ssu = self.SUIT_MAP[self.suit]

        if ssu < osu:
            return True
        if ssu == osu and sval < oval:
            return True
        return False

    def is_trick(
        self, other: Card, starting_suit: str, trump: Optional[str] = None
    ) -> bool:
        """
        Returns if the card tricks the other.
        """
        # if both of them is a trump

        if self.get_suit() == trump and other.get_suit() == trump:
            return self.VALUE_MAP[self.get_value()] < other.VALUE_MAP[other.get_value()]

        if self.get_suit() == trump:
            return True

        if other.get_suit() == trump:
            return True

        # if btoth of them is from the starting suit

        if self.get_suit() == starting_suit and other.get_suit() == starting_suit:
            return self.VALUE_MAP[self.get_value()] < other.VALUE_MAP[other.get_value()]

        if self.get_suit() == starting_suit:
            return True

        if other.get_suit() == starting_suit:
            return True

        return False

        # func_name = inspect.stack()[0][3]  # the name of this function
        # raise NotImplementedError(f"{func_name} is not implemented yet!")

    def is_same(self, other: Card):
        if self.get_suit() != other.get_suit():
            return False
        if self.get_value() != other.get_value():
            return False
        return True

    def __str__(self) -> str:
        return f"{self.suit}{self.value}"

    def __repr__(self):
        return self.__str__()
