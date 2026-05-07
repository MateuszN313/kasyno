from src.games import Game
from src.models import Bet, User


class GameService:
    def __init__(self, games):
        self.__games: dict[str, Game] = games

    def start_game(self, game: str, user: User, value: float) -> Bet: #**kwargs
        game_obj = self.__games[game.lower()]
        #from src.games.horseRace import HorseRace
        #if isinstance(game_obj, HorseRace):
        #    chosen_horse_id = kwargs.get("chosen_horse_id", "")
        #    winner, multiplier = game_obj.race(chosen_horse_id)
        #    result = value * multiplier if multiplier > 0 else -value
        #    return Bet("", user.get_id(), game.lower(), value, result)
        #else:
        multiplayer = game_obj.play(value, user.get_balance())
        result = value * multiplayer
        return Bet("", user.get_id(), game.lower(), value, result)