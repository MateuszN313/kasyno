from src.config.paths import RESOURCES_DIR
from src.models import User
from src.repos import UserRepo

class UserCsvRepo(UserRepo):
    def __init__(self, path: str):
        self.__users: list[User] = []
        self.__path: str = path
        self._load()

    def add_user(self, user: User) -> bool:
        pass

    def remove_user(self, user_id: str) -> bool:
        pass

    def get_users(self) -> list[User]:
        pass

    def get_user(self, user_id: str) -> User:
        pass

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

if __name__ == "__main__":
    user_csv_repo: UserCsvRepo = UserCsvRepo(RESOURCES_DIR / "users.csv")
