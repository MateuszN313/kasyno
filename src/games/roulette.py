from src.games import Game
from src.models import Field

class Roulette(Game):
    def __init__(self):
        self.__fields: list[Field] = []

    def play(self) -> float:
        pass
