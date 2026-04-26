from enum import Enum

class User:
    def __init__(self, login, password_hash):
        self.__id: str = ""
        self.__login: str = login
        self.__password_hash: str = password_hash
        self.__role: str = "PLAYER"
        self.__balance: float = 0