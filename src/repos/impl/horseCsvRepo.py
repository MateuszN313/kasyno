from src.models import Horse
from src.repos import HorseRepo

class HorseCsvRepo(HorseRepo):
    def __init__(self, path: str):
        self.__horses: list[Horse] = []
        self.__path: str = path
        self._load()

    def add_horse(self, horse: Horse) -> bool:
        pass

    def remove_horse(self, horse_id: str) -> bool:
        pass

    def get_horses(self) -> list[Horse]:
        pass

    def get_horse(self, horse_id: str) -> Horse:
        pass

    def _load(self) -> None:
        pass

    def _save(self) -> None:
        pass


