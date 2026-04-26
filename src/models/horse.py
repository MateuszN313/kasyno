class Horse:
    def __init__(self, id: str, name: str, wins: int, loses: int):
        self.__id: str = id
        self.__name: str = name
        self.__wins: int = wins
        self.__loses: int = loses