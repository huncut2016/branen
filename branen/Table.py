from Card import Card
import inspect


class Table:
    dealer: str = "N"
    current: str = dealer
    NEXT = {"N": "E", "E": "S", "S": "W", "W": "N"}

    def __init__(self, hands: dict[str, list[Card]] = None):
        self.hands = hands

    def play_card_index(self, card_index: int) -> None:
        """
        Play a card depend on an index.

        Parameters
        ----------
        card_index: :class: `int`
            The index of the card, that you want to play.
        """
        if self.hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.hands[self.current][card_index].play()

    def play_card(self, card: Card) -> None:
        func_name = inspect.stack()[0][3]  # the name of this function
        raise NotImplementedError(f"{func_name} is not implemented yet!")
        # if self.hands is None:
        #     raise Exception("Hands are empty, you need to set some cards!")

    def reset(self, dealer: str = "N") -> None:
        if self.hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.dealer = dealer
        self.current = dealer

        for key in self.hands:
            cards: list[Card] = self.hands[key]

            for card in cards:
                card.reset()

    def get_hands(self) -> dict[str, list[Card]]:
        if self.hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        return self.hands.copy()

    def set_E(self, E: list[Card]) -> None:
        if self.hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.hands["E"] = E

    def set_W(self, W: list[Card]) -> None:
        if self.hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.hands["W"] = W

    def set_N(self, N: list[Card]) -> None:
        if self.hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.hands["N"] = N

    def set_S(self, S: list[Card]) -> None:
        if self.hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.hands["S"] = S
