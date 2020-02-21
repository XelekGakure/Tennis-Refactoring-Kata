class Player:
    class Exception:
        pass

    RESULTS = ["Love", "Fifteen", "Thirty", "Forty"]

    name: str = "Player"
    score: int = 0
    result: str = ""

    def __init__(self, name: str) -> None:
        self.name = name

    def earn_point(self):
        self.score += 1
        return self.score

    def set_result(self):
        if self.score <= 3:
            self.result = self.RESULTS[self.score]
        return self.result

