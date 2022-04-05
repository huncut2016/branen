from branen.Card import Card
from typing import List


class Hand:
    CARD_TO_HCP = {
        "A": 4,
        "K": 3,
        "Q": 2,
        "J": 1,
        "T": 0,
        **{str(i): 0 for i in range(2, 11)},
        "11": 1,
        "12": 2,
        "13": 3,
        "14": 4,
    }

    def __init__(self, hand: List[Card]):
        if hand is None:
            Exception("You have to tell the cards in hand")
        if len(hand) != 13:
            Exception("Length of the hand must be 13!")

        self.hand = hand
        self.sort()

    def has_suit(self, suit: str) -> bool:
        """
        Find the suit exist in hand.

        Parameters
        ----------
        suit :class: `str`
            suit, that you want to find
        Returns
        -------
        Suit exist in hand,
        """
        for i in self.hand:
            if i.get_suit() == suit and not i.get_is_played():
                return True

        return False

    def has_card(self, card: Card) -> bool:
        for i in self.hand:
            if i == card:
                return True

        return False

    def get_hcp(self) -> int:
        """
        Returns
        -------
            Returns the HCP's of the card.
        """
        counter = 0
        for i in self.hand:
            counter += self.CARD_TO_HCP[i.get_value()]

        return counter

    def play_card(self, card: Card) -> None:
        for c in self.hand:
            if c == card:
                c.play()
        # for i in range(len(self.hand)):
        #     if self.hand[i].is_same(card):
        #         self.hand[i].play()

    def get_card_index(self, card: Card) -> int:
        for i in range(len(self.hand)):
            if self.hand[i].is_same(card):
                return i
        raise Exception(f"{card} has not been found in {self}")

    def sort(self, reverse: bool = False):
        self.hand.sort(reverse=reverse)

    def __getitem__(self, item: int) -> Card:
        return self.hand[item]

    def __copy__(self):
        return Hand(self.hand.copy())

    def copy(self):
        return self.__copy__()

    def __str__(self):
        return " ".join(str(card) for card in self.hand)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return iter(self.hand)
