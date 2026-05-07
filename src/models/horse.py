import random
import uuid

class Horse:
    NAMES = ["Pierun", "Gzrmot", "Błysk", "Tornado", "Gwiazda", "Piorun", "Srebro", "Złoto"]
    #to jeszcze bedzie zmieniane jak kon bedzie mial retirment to ma nazywac sie inaczej przynajmniej przez 3 tury wyscigow ale cos mi nie dziala w gameservice i to ogarne kiedys

    def __init__(self, id: str = "", name: str = "", age: int = 0, weight: int = 0, races_won: int = 0):
        self.__id: str = id if id else str(uuid.uuid4())
        self.__name: str = name if name else random.choice(self.NAMES)
        self.__age: int = age if age else random.randint(1, 8)
        self.__weight: int = weight if weight else random.randint(400, 1000)
        self.__races_won: int = races_won if races_won else random.randint(0, 5)

    def calculate_winrate(self) -> int:
        winrate = 50  # baza
        #mlodszy jest szybszy wieksza szansa na wygrana
        winrate += (8 - self.__age) * 5
        #lzejszy ma wieksza szanse na wygrana
        winrate += int((1000 - self.__weight) / 20)
        #wieksze doswiadczenie w wyscigach tez zwieksza winrate
        winrate += self.__races_won * 3
        return max(5, min(winrate, 95))  # zawsze między 5 a 95

    def needs_retirement(self) -> bool:
        return self.__races_won >= 6

    def after_race_won(self) -> None:
        self.__races_won += 1

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_weight(self) -> int:
        return self.__weight

    def get_races_won(self) -> int:
        return self.__races_won

    def to_csv(self) -> str:
        return f"{self.__id};{self.__name};{self.__age};{self.__weight};{self.__races_won}"

    def __str__(self) -> str:
        return (f"[{self.__name}] wiek: {self.__age}, "
                f"waga: {self.__weight}kg, "
                f"wygrane: {self.__races_won}/6, "
                f"szansa: {self.calculate_winrate()}%")

    def get_copy(self) -> "Horse":
        return Horse(self.__id, self.__name, self.__age, self.__weight, self.__races_won)
