from src.models import User
from src.services import RepoService, GameService

class UI:
    def __init__(self, repo_service: RepoService, game_service: GameService):
        self.__active_user: User | None = None
        self.__repo_service: RepoService = repo_service
        self.__game_service: GameService = game_service

    def start(self) -> None:
        print("hello")