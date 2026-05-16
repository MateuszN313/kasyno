from src.models import Horse
from src.repos import HorseRepo

class HorseCsvRepo(HorseRepo):
    def __init__(self, path: str):
        self.__horses: list[Horse] = []
        self.__path: str = path
        self._load()

    def __del__(self) -> None:
        self._save()

    def add_horse(self, horse: Horse) -> bool:
        if horse not in self.__horses:
            self.__horses.append(horse)
            return True
        return False

    def remove_horse(self, id: str) -> bool:
         for horse in self.__horses:
             if horse.get_id() == id:
                self.__horses.remove(horse)
                return True
         return False

    def get_horses(self) -> list[Horse]:
        return self.__horses

    def get_horse(self, id: str) -> Horse | None:
        for horse in self.__horses:
            if horse.get_id() == id:
                return horse
        return None

    def _load(self) -> None:
        try:
            file = open(self.__path, 'r')
            file.readline()
            for line in file:
                self.__horses.append(Horse.from_csv(line))
        except FileNotFoundError:
            print("Nie znleziono pliku - stworzono nową pustą baze koni")

    def _save(self) -> None:
        file = open(self.__path, 'w')
        for horse in self.__horses:
            file.write(horse.to_csv())



