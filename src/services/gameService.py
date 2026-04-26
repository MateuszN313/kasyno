from src.games import Game

class GameService:
    def __init__(self, games):
        self.__games: dict[str, Game] = games