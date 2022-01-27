import inspect
from typing import Dict, List

from .Card import Card


class Table:
    NEXT = {"N": "E", "E": "S", "S": "W", "W": "N"}

    def __init__(self, hands: Dict[str, List[Card]] = None, dealer: str = "N"):
        if hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.hands = hands
        self.dealer = dealer
        self.current = dealer

    def play_card_index(self, card_index: int) -> None:
        """
        Play a card depend on an index.

        Parameters
        ----------
        card_index: :class: `int`
            The index of the card, that you want to play.
        """
        self.hands[self.current][card_index].play()
        self.current = self.NEXT[self.current]

    def play_card(self, card: Card) -> None:
        func_name = inspect.stack()[0][3]  # the name of this function
        raise NotImplementedError(f"{func_name} is not implemented yet!")
        # if self.hands is None:
        #     raise Exception("Hands are empty, you need to set some cards!")

    def reset(self, dealer: str = "N") -> None:
        """
        Reset the table
        """

        self.dealer = dealer
        self.current = dealer

        for key in self.hands:
            cards: list[Card] = self.hands[key]

            for card in cards:
                card.reset()

    def set_dealer(self, dealer: str = "N") -> None:
        self.dealer = dealer

    def get_hands(self) -> Dict[str, List[Card]]:
        return self.hands.copy()

    def set_E(self, E: List[Card]) -> None:
        self.hands["E"] = E

    def set_W(self, W: List[Card]) -> None:
        self.hands["W"] = W

    def set_N(self, N: List[Card]) -> None:
        self.hands["N"] = N

    def set_S(self, S: List[Card]) -> None:
        self.hands["S"] = S
