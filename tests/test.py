import unittest
from random import shuffle
from typing import List

import sys
from pathlib import Path

dir_path = Path(__file__).absolute().parent.parent / "src"
sys.path.append(str(dir_path))


from branen.Card import Card
from branen.Table import Table
from branen.Hand import Hand
from branen_tools.lin_parser import LinParser


# from manim_branen.m_Card import m_Card

TEST_DATAS: Path = Path(__file__).absolute().parent / "test_datas"


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
            c = Card(i[0], i[1])

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

        hands = [
            Card(suit, value) for suit in suits for value in values
        ]  # creating random hands
        shuffle(hands)
        hands_input = {
            "E": Hand(hands[:13]),
            "W": Hand(hands[14:26]),
            "N": Hand(hands[27:39]),
            "S": Hand(hands[38:]),
        }

        table = Table(hands=hands_input, dealer="S")
        self.assertEqual(table.current_player, "S", "Dealers are not equal!")

        table.play_card_index(0)

        self.assertEqual(
            table.current_player,
            "W",
            "After card playing, the next card player is not correct",
        )
        self.assertEqual(
            table.get_hands()["S"][0].get_is_played(),
            True,
            "After playing, card won't bacome passive",
        )

        p = 0
        for index, val in enumerate(table.get_hands()["W"]):
            if val.get_suit() != table.in_play[0].get_suit():
                p = index
                break

        def test_wrong_play(i, table):
            return lambda: table.play_card_index(i)

        self.assertRaises(Exception, test_wrong_play(p, table))

    # def test_play (self) :
    #     lp: LinParser = LinParser(path=str(TEST_DATAS / "test1.lin")).parse()

    #     board, deal, vulnerable, play = lp.get_all()

    #     for i in range(5):
    #         t.play_card(play.get_current_card()))
    #         play.next()


#         self.assertEqual ()

# lp: LinParser = LinParser(path=str(TEST_DATAS / "test1.lin")).parse()

# board, deal, vulnerable, play = lp.get_all()

# for i in range(20):
#     deal.play_card(play.get_current_card())
#     play.next()


if __name__ == "__main__":
    unittest.main()
