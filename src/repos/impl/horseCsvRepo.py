import os
from src.models import Horse
from src.repos import HorseRepo


class HorseCsvRepo(HorseRepo):
    def __init__(self, path: str):
        self.__horses: list[Horse] = []
        self.__path: str = path
        self._load()

    def add_horse(self, horse: Horse) -> bool:
        existing = [h for h in self.__horses if h.get_id() == horse.get_id()]
        if existing:
            self.__horses.remove(existing[0])
        self.__horses.append(horse)
        self._save()
        return True

    def remove_horse(self, id: str) -> bool:
        horse = [h for h in self.__horses if h.get_id() == id]
        if horse:
            self.__horses.remove(horse[0])
            self._save()
            return True
        return False

    def get_horses(self) -> list[Horse]:
        return [h.get_copy() for h in self.__horses]

    def get_horse(self, id: str) -> Horse | None:
        horse = [h for h in self.__horses if h.get_id() == id]
        return horse[0].get_copy() if horse else None

    def _load(self) -> None:
        if not os.path.exists(self.__path):
            self._create_default_horses()
            return
        try:
            with open(self.__path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    tokens = line.split(";")
                    if len(tokens) >= 5:
                        self.__horses.append(
                            Horse(tokens[0], tokens[1], int(tokens[2]), int(tokens[3]), int(tokens[4]))
                        )
        except Exception:
            self._create_default_horses()

    def _save(self) -> None:
        os.makedirs(os.path.dirname(self.__path), exist_ok=True)
        with open(self.__path, "w") as file:
            for horse in self.__horses:
                file.write(horse.to_csv() + "\n")

    def _create_default_horses(self) -> None:
        for _ in range(6):
            self.__horses.append(Horse())  # losowe konie
        self._save()
