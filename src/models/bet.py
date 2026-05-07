class Bet:
    def __init__(self, id: str, player_id: str, game: str, value: float, result: float):
        self.__id: str = id
        self.__playerId: str = player_id
        self.__game: str = game
        self.__value: float = value
        self.__result: float = result
