# -*- coding: utf-8 -*-

import unittest

from Entity.Player import Player
from Entity.TennisGame import TennisGame
from Tests import test_cases


class TestTennis(unittest.TestCase):
    def test_new_game(self):
        party = TennisGame(Player("Jean-Pierre"), Player("Stephane"))
        self.assertEqual(party.score(), "Love-All")

    def test_Score_Game(self):
        for testcase in test_cases:
            (p1_points, p2_points, score, p1_name, p2_name) = testcase
            p1 = Player(p1_name)
            p2 = Player(p2_name)
            party = TennisGame(p1, p2)
            p1.score = p1_points
            p2.score = p2_points
            if p1_points < 0 or p2_points < 0:
                self.assertRaises(TennisGame.ScoreUnderZeroException, party.score())
            try:
                self.assertEqual(score, party.score())
            except Exception as err:
                raise self.failureException()


if __name__ == "__main__":
    unittest.main()
