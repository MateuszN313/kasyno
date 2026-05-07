from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def play(self, value: float, user_balance: float) -> float: pass