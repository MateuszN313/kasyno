import os
import uuid
from src.models import Bet
from src.repos import BetRepo


class BetCsvRepo(BetRepo):
    def __init__(self, path: str):
        self.__bets: list[Bet] = []
        self.__path: str = path
        self._load()

    def add_bet(self, bet: Bet) -> bool:
        to_save = Bet(
            bet.get_id() if bet.get_id() else str(uuid.uuid4()),
            bet.get_player_id(),
            bet.get_game(),
            bet.get_value(),
            bet.get_result()
        )
        self.__bets.append(to_save)
        self._save()
        return True

    def remove_bet(self, id: str) -> bool:
        bet = [b for b in self.__bets if b.get_id() == id]
        if bet:
            self.__bets.remove(bet[0])
            self._save()
            return True
        return False

    def get_bets(self) -> list[Bet]:
        return list(self.__bets)

    def get_bet(self, id: str) -> Bet | None:
        bet = [b for b in self.__bets if b.get_id() == id]
        return bet[0] if bet else None

    def get_bets_by_player(self, player_id: str) -> list[Bet]:
        return [b for b in self.__bets if b.get_player_id() == player_id]

    def _load(self) -> None:
        if not os.path.exists(self.__path):
            return
        try:
            with open(self.__path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    tokens = line.split(";")
                    if len(tokens) >= 5:
                        self.__bets.append(Bet(tokens[0], tokens[1], tokens[2], float(tokens[3]), float(tokens[4])))
        except Exception:
            pass

    def _save(self) -> None:
        os.makedirs(os.path.dirname(self.__path), exist_ok=True)
        with open(self.__path, "w") as file:
            for bet in self.__bets:
                file.write(bet.to_csv() + "\n")
