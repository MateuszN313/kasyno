from src.games import Game
from src.models import Horse

class HorseRace(Game):
    def __init__(self, horses: list[Horse]):
        self.__horses: list[Horse] = horses

    def play(self) -> float:
        pass
