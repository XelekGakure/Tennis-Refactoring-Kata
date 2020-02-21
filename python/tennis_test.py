# -*- coding: utf-8 -*-

import pytest

from tennis import TennisGame1, TennisGame2, TennisGame3
from tennis_unittest import test_cases, play_game


class TestTennis:

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game1(self, p1_points, p2_points, score, p1_name, p2_name):
        game = play_game(TennisGame1, p1_points, p2_points, p1_name, p2_name)
        assert score == game.score()

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game2(self, p1_points, p2_points, score, p1_name, p2_name):
        game = play_game(TennisGame2, p1_points, p2_points, p1_name, p2_name)
        assert score == game.score()

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game3(self, p1_points, p2_points, score, p1_name, p2_name):
        game = play_game(TennisGame3, p1_points, p2_points, p1_name, p2_name)
        assert score == game.score()
