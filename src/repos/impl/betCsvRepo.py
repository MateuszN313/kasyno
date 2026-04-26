from src.models import Bet
from src.repos import BetRepo

class BetCsvRepo(BetRepo):
    def __init__(self, path):
        self.__bets: list[Bet] = []
        self.__path: str = path
        self._load()

    def add_bet(self, bet) -> bool:
        pass

    def remove_bet(self, bet_id) -> bool:
        pass

    def get_bets(self) -> list[Bet]:
        pass

    def get_bet(self, bet_id) -> Bet:
        pass

    def _load(self) -> None:
        pass

    def _save(self) -> None:
        pass


