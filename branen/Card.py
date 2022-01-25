import inspect
from functools import total_ordering


@total_ordering
class Card:
    SUIT_MAP = {"S": 3, "H": 2, "D": 1, "C": 0}
    VALUE_MAP = {
        **{"A": 12, "K": 11, "Q": 12, "J": 11, "T": 10},
        **{str(i): i for i in range(2, 11)},
    }

    is_passive = False

    def get_suit(self) -> str:
        return self.suit

    def reset(self) -> None:
        self.set_passivity(False)
        self.set_played_turn(0)

    def play(self):
        if self.is_passive:
            Exception("This card was playd!")

        self.set_passivity(True)

    def set_played_turn(self, turn: int) -> None:
        self.turn = turn

    def set_passivity(self, p):
        self.is_passive = p

    def get_value(self) -> str:
        return self.value

    def set_value(self, value: str) -> None:
        if len(value) != 1:
            raise Exception(
                f"The length of Card value name must be 1! (value name = {value})"
            )

        self.value = value.upper()

    def set_suit(self, suit: str) -> None:
        if len(suit) != 1:
            raise Exception(
                f"The length of Card suit name must be 1! (suit name = {suit})"
            )

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
