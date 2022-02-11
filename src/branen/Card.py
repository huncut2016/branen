import inspect
from functools import total_ordering


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

    def set(self, suit: str, value: str):
        self.suit = suit
        self.value = value

        return self

    def get_suit(self) -> str:
        return self.suit

    def reset(self) -> None:
        self.set_is_played(False)
        self.set_played_turn(0)

    def play(self):
        if self.is_played:
            Exception("This card was played!")

        self.set_is_played(True)

    def set_played_turn(self, turn: int) -> None:
        self.turn = turn

    def get_is_played(self) -> bool:
        return self.is_played

    def set_is_played(self, p):
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

    def __str__(self) -> str:
        return f"{self.suit}{self.value}"

    def __repr__(self):
        return self.__str__()
