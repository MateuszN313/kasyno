class Bet:
    def __init__(self, player_id, game, value, result):
        self.__id: str = ""
        self.__playerId: str = player_id
        self.__game: str = game
        self.__value: float = value
        self.__result: float = result
