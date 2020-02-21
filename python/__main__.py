from Entity.Player import Player
from Entity.TennisGame import TennisGame
import sys
from Tests import tennis_unittest


player1 = Player("Jean-Pierre")
player2 = Player("Stephane")

party = TennisGame(player1, player2)

print(party.score())


party.won_point(player1)

print("P1", player1.score)
print("P2", player2.score)
print(party.score())
