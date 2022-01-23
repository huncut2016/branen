from ..branen.Card import Card
from manim import SVGMobject
import os

class m_Card (SVGMobject, Card):
    """Card is one of the basic building block of branen.
    This object represents the french card in bridge, not the bidding card!
    
    Examples
    --------
    .. code-block:: python
        my_card = m_Card()
    
    Parameters
    --------
    suit : :class:`str`        
        This is the suit of the card. It can be: `S`, `H`, `C`, `D`
    value : :class:`str`
        This is the value of the card. It can be: `A`, `K`, `Q`, `J`, `T`, `9`, `...` , `2`
    """
    def __init__(self, suit:str, value:str, **kwargs):
        
        self.set_value(value)
        self.set_suit(suit)
        
        file_path = os.path.join(os.path.dirname(__file__),
                                 "..",
                                 "media",
                                 "cards",
                                 f"{self.suit}{self.value}.svg")
        
        super().__init__(file_name = file_path, **kwargs)