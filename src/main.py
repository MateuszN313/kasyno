from src.config.paths import RESOURCES_DIR
from src.games import Blackjack, Game, Roulette, HorseRace
from src.repos import BetRepo, HorseRepo, UserRepo
from src.repos.impl import BetCsvRepo, HorseCsvRepo, UserCsvRepo
from src.services import GameService, DeckOfCards, RepoService
from src.ui import UI


class Main:
    @staticmethod
    def main() -> None:
        bet_repo: BetRepo = BetCsvRepo(RESOURCES_DIR / "bets.csv")
        horse_repo: HorseRepo = HorseCsvRepo(RESOURCES_DIR / "horses.csv")
        user_repo: UserRepo = UserCsvRepo(RESOURCES_DIR / "users.csv")
        repo_service: RepoService = RepoService(user_repo, horse_repo, bet_repo)

        deck_of_cards: DeckOfCards = DeckOfCards()
        games: dict[str, Game] = {"Blackjack": Blackjack(deck_of_cards),
                                  "Horse Race": HorseRace(repo_service.check_horses()),
                                  "Roulette": Roulette()}
        game_service: GameService = GameService(games)

        ui: UI = UI(repo_service, game_service)
        ui.start()

if __name__ == "__main__":
    Main.main()