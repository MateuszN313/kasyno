import uuid

from src.config.paths import RESOURCES_DIR
from src.models import User
from src.repos import UserRepo

class UserCsvRepo(UserRepo):
    def __init__(self, path: str):
        self.__users: list[User] = []
        self.__path: str = path
        self._load()

    def save_user(self, user: User) -> bool:
        to_save = user.get_copy()
        if not to_save.get_id():
            to_save.set_id(str(uuid.uuid4()))
        else:
            from_users = [u for u in self.__users if u.get_id() == to_save.get_id()]
            if len(from_users) == 1:
                self.__users.remove(from_users[0])
            else:
                return False

        self.__users.append(to_save)
        self._save()
        return True

    def remove_user(self, user_id: str) -> bool:
        user = [user for user in self.__users if user.get_id() == user_id]
        if len(user) == 1:
            self.__users.remove(user[0])
            self._save()
            return True
        else:
            return False

    def get_users(self) -> list[User]:
        copy = [user.get_copy() for user in self.__users]
        return copy

    def get_user_by_id(self, user_id: str) -> User | None:
        user = [user.get_copy() for user in self.__users if user.get_id() == user_id]
        if len(user) == 1:
            return user[0]
        else:
            return None

    def get_user_by_login(self, user_login: str) -> User | None:
        user = [user.get_copy() for user in self.__users if user.get_login() == user_login]
        if len(user) == 1:
            return user[0]
        else:
            return None

    def _load(self) -> None:
        file = open(self.__path, "r")
        for line in file:
            string = line.strip()
            tokens = string.split(";")
            self.__users.append(User(tokens[0], tokens[1], tokens[2], tokens[3], float(tokens[4])))
        file.close()

    def _save(self) -> None:
        file = open(self.__path, "w")
        to_write = []
        for user in self.__users:
            to_write.append(user.to_csv() + '\n')
        file.writelines(to_write)
        file.close()
