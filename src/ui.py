from src.models import User
from src.services import RepoService, GameService

class UI:
    def __init__(self, repo_service: RepoService, game_service: GameService):
        self.__active_user: User | None = None
        self.__repo_service: RepoService = repo_service
        self.__game_service: GameService = game_service

    def start(self) -> None:
        print("--- Witamy w kasynie ---")

        while True:
            print("1 - logowanie | 2 - rejestracja | 0 - wyjdź")
            choice = int(input())
            if choice == 1:
                self.login()
                if self.__active_user is None:
                    print("blad w logowaniu")
                else:
                    print("zalogowano | " + self.__active_user.__str__())
                    if self.__active_user.get_role().upper() == "ADMIN":
                        self.admin_ui()
                    else:
                        self.player_ui()

            elif choice == 2:
                self.register()
            elif choice == 0:
                return
            else:
                print("Nieprawidlowa opcja")

    def register(self) -> bool:
        print("--- rejestracja ---")
        return self.__repo_service.register_user(input("Login: "), input("Haslo: "))

    def login(self) -> None:
        print("--- logowanie ---")
        self.__active_user = self.__repo_service.authenticate_user(input("Login: ") , input("Haslo: "))

    def logout(self) -> None:
        self.__active_user = None
        self.start()

    def player_ui(self) -> None:
        print("--- Kasyno ---")

        while True:
            print("1 - zagraj w gre | 2 - twoj balans | 3 - wplac | 4 - wyplac | 5 - historia zakladow | 0 - wyloguj sie")
            choice = int(input())

            if choice == 1:
                print("podaj nazwe gry: blackjack | wyscig konny | ruletka | 0 - zrezygnuj")
                game = input()
                if game == "0":
                    continue

                print("podaj wartosc zakladu")
                value = float(input())
                bet = self.__game_service.start_game(game, self.__active_user.get_copy(), value)

                if bet is None:
                    print("nie masz tylu srodkow na koncie")

                #                    dodawanie beta do bet repo

                result = bet.get_result() - value
                if self.__repo_service.change_user_balance(self.__active_user.get_id(), result):
                    balance = self.__active_user.get_balance()
                    self.__active_user.set_balance(balance + result)
                else:
                    print("blad przy wyplacaniu")

            elif choice == 2:
                print(self.__active_user.get_balance())

            elif choice == 3:
                self.charge_balance()

            elif choice == 4:
                self.deposit()

            elif choice == 5: pass
                #                  print zakladow
            elif choice == 0:
                return

    def admin_ui(self) -> None:
        print("--- Admin ---")

        while True:
            print("1 - wyswietl zaklady | 2 - wyswietl konie | 3 - dodaj konia | 4 - usun konia | 5 - wyswietl uzytkownikow | 6 - usun uzytkownika | 0 - wyloguj sie")
            choice = int(input())

            if choice == 1: pass
                #         wyswietlanie zakladow
            elif choice == 2: pass
                #         wyswietlanie koni
            elif choice == 3:
                print("podaj imie konia")
                name = input()
                #         dodawanie konia
            elif choice == 4:
                print("podaj id konia")
                id = input()
                #         usuwanie konia
            elif choice == 5:
                users = self.__repo_service.check_users()
                for user in users:
                    print(user)
            elif choice == 6:
                print("podaj id uzytkownika")
                if self.__repo_service.remove_user(input()):
                    print("usunieto uzytkownia")
                else:
                    print("blad przy usuwaniu uzytkownika")
            elif choice == 0:
                return

    def charge_balance(self) -> None:
        print("podaj ilosc wplacanych pieniedzy")
        amount = float(input())
        if self.__repo_service.change_user_balance(self.__active_user.get_id(), amount):
            balance = self.__active_user.get_balance()
            self.__active_user.set_balance(balance + amount)
        else:
            print("blad przy wplacaniu")

    def deposit(self) -> None:
        print("podaj ilosc wyplacanych pieniedzy")
        amount = -float(input())
        if self.__repo_service.change_user_balance(self.__active_user.get_id(), amount):
            balance = self.__active_user.get_balance()
            self.__active_user.set_balance(balance + amount)
        else:
            print("blad przy wyplacaniu")