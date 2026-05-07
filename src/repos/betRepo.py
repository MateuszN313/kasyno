from abc import ABC, abstractmethod

from src.models import Bet

class BetRepo(ABC):
    @abstractmethod
    def add_bet(self, bet: Bet) -> bool: pass

    @abstractmethod
    def remove_bet(self, id: str) -> bool: pass

    @abstractmethod
    def get_bets(self) -> list[Bet]: pass

    @abstractmethod
    def get_bet(self, id: str) -> Bet: pass

    @abstractmethod
    def _load(self) -> None: pass

    @abstractmethod
    def _save(self) -> None: pass