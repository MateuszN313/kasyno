class User:
    def __init__(self, id: str, login: str, password_hash: str, role: str, balance: float):
        self.__id: str = id
        self.__login: str = login
        self.__password_hash: str = password_hash
        self.__role: str = role
        self.__balance: float = balance

    def to_csv(self) -> str:
        return f"{self.__id};{self.__login};{self.__password_hash};{self.__role};{self.__balance}"

    def __str__(self) -> str:
        return f"id: {self.__id}, login: {self.__login}, role: {self.__role}, balance: {self.__balance}"

    def get_copy(self):
        return User(self.__id, self.__login, self.__password_hash, self.__role, self.__balance)

    def get_id(self) -> str:
        return self.__id

    def set_id(self, id: str):
        self.__id = id

    def get_login(self) -> str:
        return self.__login