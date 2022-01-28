import inspect
from typing import Dict, List
from warnings import warn

from .Card import Card
from .Hand import Hand


class Table:
    NEXT = {"N": "E", "E": "S", "S": "W", "W": "N"}

    def __init__(
        self, hands: Dict[str, Hand] = None, dealer: str = "N", trump: str = None
    ):
        if hands is None:
            raise Exception("Hands are empty, you need to set some cards!")

        self.hands = hands
        self.dealer = dealer
        self.current = dealer
        self.starting_suit: str = None
        self.round = 1
        self.in_play: List[Card] = []
        self.trump = trump

    def play_card_index(self, card_index: int) -> None:
        """
        Play a card depend on an index.

        Parameters
        ----------
        card_index: :class: `int`
            The index of the card, that you want to play.
        """
        func_name = inspect.stack()[0][3]  # the name of this function
        warn(f"{func_name} is not implemented fully yet!")

        if self.is_end_of_round():
            # TODO self.current = self.win_the_trick()
            self.round = 1
            self.starting_suit = None
            self.in_play = []

        playing_hand = self.hands[self.current]  # the hand who are coming
        card = playing_hand[card_index]

        if self.starting_suit is None:
            self.starting_suit = card.get_suit()

        self.is_valid_play(card)  # Check that playing the card is meets the rules

        card.play()

        self.current = self.NEXT[self.current]
        self.in_play.append(card)

        self.round += 1

    def is_end_of_round(self) -> bool:
        return self.round == 4

    def win_the_trick(self) -> str:
        # TODO
        func_name = inspect.stack()[0][3]  # the name of this function
        raise NotImplementedError(f"{func_name} is not implemented yet!")

    def is_valid_play(self, card: Card) -> None:
        """
        Check that playing the card is meets the rules
        Parameters
        ----------
        card
            The card, that you want to play

        Returns
        -------
            Nothing
        """
        playing_hand = self.hands[self.current]

        if self.round != 1:  # not the first round
            if (
                playing_hand.has_suit(self.starting_suit)
                and card.get_suit() != self.starting_suit
            ):
                raise Exception(
                    f"{self.current} has {self.starting_suit} suit, but the card is {card.get_suit()}"
                )

        if not playing_hand.has_card(card):
            raise Exception(f"{self.current} has no card {card}")

    def play_card(self, card: Card) -> None:
        # TODO
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
            cards: Hand = self.hands[key]

            for card in cards:
                card.reset()

    def set_dealer(self, dealer: str = "N") -> None:
        self.dealer = dealer

    def get_hands(self) -> Dict[str, Hand]:
        return self.hands.copy()

    def set_E(self, E: Hand) -> None:
        self.hands["E"] = E

    def set_W(self, W: Hand) -> None:
        self.hands["W"] = W

    def set_N(self, N: Hand) -> None:
        self.hands["N"] = N

    def set_S(self, S: Hand) -> None:
        self.hands["S"] = S
