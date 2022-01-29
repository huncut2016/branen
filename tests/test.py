import unittest
from random import shuffle
from typing import List

from src.branen.Card import Card
from src.branen.Table import Table
from src.branen.Hand import Hand


# from manim_branen.m_Card import m_Card


class TestCard(unittest.TestCase):
    def test_sort(self):
        cards = [
            ("S", "K"),
            ("S", "T"),
            ("S", "7"),
            ("S", "5"),
            ("S", "2"),
            ("H", "Q"),
            ("H", "2"),
            ("D", "Q"),
            ("D", "7"),
            ("D", "3"),
            ("C", "J"),
            ("C", "T"),
            ("C", "3"),
        ]

        cs = []

        for i in cards:
            c = Card()
            c.set_suit(i[0])
            c.set_value(i[1])

            cs.append(c)

        cs2 = cs.copy()
        shuffle(cs2)
        cs2.sort(reverse=True)

        self.assertEqual(cs2, cs, "Two hands are not equal")


#         self.assertTrue(m_Card("H", "A") > m_Card("H", "K"))
class TestTable(unittest.TestCase):
    def testTablePlay(self):
        suits: List[str] = ["S", "H", "D", "C"]
        values: List[str] = [
            *["A", "K", "Q", "J", "T"],
            *[str(i) for i in range(2, 10)],
        ]

        hands = [Card().set(suit, value) for suit in suits for value in values]
        shuffle(hands)
        hands_input = {
            "E": Hand(hands[:13]),
            "W": Hand(hands[14:26]),
            "N": Hand(hands[27:39]),
            "S": Hand(hands[38:]),
        }

        table = Table(hands=hands_input, dealer="S")
        self.assertEqual(table.current, "S", "Dealers are not equal!")

        table.play_card_index(0)

        self.assertEqual(
            table.current,
            "W",
            "After card playing, the next card player is not correct",
        )
        self.assertEqual(
            table.get_hands()["S"][0].get_is_played(),
            True,
            "After playing, card wont bacome passive",
        )


#         self.assertEqual ()

if __name__ == "__main__":
    unittest.main()
