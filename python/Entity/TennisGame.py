from Entity.Player import Player


class TennisGame:
    p1: Player
    p2: Player

    result: str = ""

    class NotAGamePlayerException(Exception):
        pass

    class ScoreUnderZeroException(Exception):
        pass

    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def won_point(self, player: Player):
        if player in [self.p1, self.p2]:
            print(player.name + " earn points !")
            return player.earn_point()
        raise self.NotAGamePlayerException()

    def score(self):
        if self.p1.score < 0 or self.p2.score < 0:
            raise self.ScoreUnderZeroException()

        if self.p1.score == self.p2.score:
            if self.p1.score < 3:
                self.result = Player.RESULTS[self.p1.score] + "-All"
            else:
                self.result = "Deuce"
        if self.__set_player_results():
            pass
        elif self.__check_advantage():
            pass
        elif self.__check_won():
            pass

        return self.result


    def get_players(self):
        return [self.p2, self.p1]

    def __set_player_results(self):
        return self.p1.set_result() + "-" + self.p2.set_result()

    def __check_advantage(self) -> Player or False:
        winner = False
        if self.p1.score > self.p2.score >= 3:
            winner = self.p1
        elif self.p2.score > self.p1.score >= 3:
            winner = self.p2
        if winner:
            self.__set_result("Advantage ", winner)
        return winner

    def __check_won(self) -> Player or False:
        winner = False
        if abs(self.p1.score - self.p2.score) < 2:
            if self.p1.score >= 4:
                winner = self.p1
            elif self.p2.score >= 4:
                winner = self.p2
        if winner:
            self.__set_result("Win for ", winner)
        return winner

    def __set_result(self, message: str, player: Player = None):
        if player is None:
            self.result = message
            return
        if player not in self.get_players():
            raise self.NotAGamePlayerException()
        self.result = message + player.name
