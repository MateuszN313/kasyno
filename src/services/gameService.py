from src.games import Game
from src.models import Bet, User


class GameService:
    def __init__(self, games):
        self.__games: dict[str, Game] = games

    def start_game(self, game: str, user: User, value: float) -> Bet:
        multiplayer = self.__games[game.lower()].play(value, user.get_balance())
        result = value * multiplayer
        return Bet("", user.get_id(), game.lower(), value, result)