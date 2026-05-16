from src.models import Bet
from src.repos import BetRepo

class BetCsvRepo(BetRepo):
    def __init__(self, path: str):
        self.__bets: list[Bet] = []
        self.__path: str = path
        self._load()

    def __del__(self) -> None:
        self._save()

    def add_bet(self, bet: Bet) -> bool:
        if bet.get_id() not in self.__bets:
            self.__bets.append(bet)
            return True
        return False

    def remove_bet(self, id: str) -> bool:
        for bet in self.__bets:
            if bet.get_id() == id:
                self.__bets.remove(bet)
                return True
        return False

    def get_bets(self) -> list[Bet]:
        return self.__bets

    def get_bet(self, id: str) -> Bet | None:
        for bet in self.__bets:
            if bet.get_id() == id:
                return bet
        else :
            return None

    def _load(self) -> None:
        try:
            file = open(self.__path, 'r')
            file.readline()
            for line in file:
                self.__bets.append(Bet.from_csv_line(line))
        except FileNotFoundError:
            print("Nie znleziono pliku - stworzono nową pustą baze zakładów")



    def _save(self) -> None:
        file = open(self.__path, 'w')
        for bet in self.__bets:
            file.write(bet.to_csv_line())




