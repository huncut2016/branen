from typing import NewType, NoReturn
import inspect


class Card():
    def get_suit (self) -> str:
        return self.suit
    
    def get_value (self) -> str:
        return self.value

    def set_value (self, value: str) -> None:
        if len(value) != 1:
            raise Exception(f"The length of Card value name must be 1! (value name = {value})")
        
        self.value = value.upper()

    def set_suit (self, suit: str) -> None:
        if len(suit) != 1:
            raise Exception(f"The length of Card suit name must be 1! (suit name = {suit})")
        
        self.suit = suit.upper()

    def get_card (self):
        func_name = inspect.stack()[0][3] # the name of this function
        raise NotImplementedError(f"{func_name} is not implemented yet!")