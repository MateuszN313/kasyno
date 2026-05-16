class Bet:

    def __init__(self, id: str, player_id: int, game: str, value: float, result: bool):
        self.__id: str = id
        self.__playerId: int = player_id
        self.__game: str = game
        self.__value: float = value
        self.__result: bool = result

    @classmethod
    def from_csv_line (cls, line: str) -> Bet:
        words = line.split(";")
        return Bet(words[0], int(words[1]), words[2], float(words[3]), bool(words[4]))

    def to_csv_line(self) -> str:
        return f'{self.__id};{self.__playerId};{self.__game};{self.__value};{self.__result}'


    def __str__(self) -> str:
        result = f'{self.__id}: grasz {self.__playerId} w grze {self.__game}, warotść - {self.__value}, '
        if self.__result is True:
            result = result + "wygrany"
        else:
            result = result + "przegrany"
        return result

    def get_id(self) -> str:
        return self.__id