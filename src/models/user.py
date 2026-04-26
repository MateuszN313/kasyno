class User:
    def __init__(self, id: str, login: str, password_hash: str, role: str, balance: float):
        self.__id: str = id
        self.__login: str = login
        self.__password_hash: str = password_hash
        self.__role: str = role
        self.__balance: float = balance