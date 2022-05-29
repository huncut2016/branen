import sys
from pathlib import Path


dir_path = Path(__file__).absolute().parent.parent / "src"
sys.path.append(str(dir_path))

TEST_DATAS: Path = Path(__file__).absolute().parent / "test_datas"

import unittest
from branen_tools.lin_parser import LinParser
from branen.Table import Table
from branen.History import History
from branen.Card import Card
from typing import Union


class TestLinParser(unittest.TestCase):
    def test_basicParser(self):
        for i in range(21):
            lp: LinParser = LinParser(
                path=str(TEST_DATAS / "much test" / "{}.lin".format(i + 1))
            ).parse()

            board, deal, vulnerable, play = lp.get_all()

            # Check types
            self.assertIsInstance(board, int)
            self.assertIsInstance(deal, Table)
            self.assertIsInstance(vulnerable, str)
            self.assertIsInstance(play, History)

            # Check all hands are valid
            self.assertEqual(
                len(deal.get_hands()),
                4,
                f"In a deal N, S, E, W must be known! ({deal.get_hands().keys()})",
            )
            quarters = ["N", "S", "E", "W"]

            for quarter, hand in deal.get_hands().items():
                self.assertIn(quarter, quarters, f"{quarter} is not in {quarters}")
                self.assertEqual(len(hand), 13)

            for historyframe in play:
                if historyframe.is_claim():
                    break
                deal.play_card(historyframe.get_card())

    def test_history(self):
        for i in range(21):
            lp: LinParser = LinParser(
                path=str(TEST_DATAS / "much test" / "{}.lin".format(i + 1))
            ).parse()
            history = lp.get_play()

            string_counter = 0

            for card in history:
                if isinstance(card, str):
                    string_counter += 1
                self.assertIsInstance(card, (Card, str))

            self.assertLessEqual(
                string_counter,
                1,
                f"History contains more than 1 claims ({string_counter})",
            )


if __name__ == "__main__":
    unittest.main()
