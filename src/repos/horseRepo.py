from abc import ABC, abstractmethod

from src.models import Horse

class HorseRepo(ABC):
    @abstractmethod
    def add_horse(self, horse) -> bool: pass

    @abstractmethod
    def remove_horse(self, horse_id) -> bool: pass

    @abstractmethod
    def get_horses(self) -> list[Horse]: pass

    @abstractmethod
    def get_horse(self, horse_id) -> Horse: pass

    @abstractmethod
    def _load(self) -> None: pass

    @abstractmethod
    def _save(self) -> None: pass