import time

from src.games import Game
from src.models import Card
from src.services import DeckOfCards

class Blackjack(Game):
    def __init__(self, deck_of_cards: DeckOfCards):
        self.__deck_of_cards: DeckOfCards = deck_of_cards
        self.__croupier: list[Card] = []
        self.__player: list[Card] = []
        self.__croupier_value: int = 0
        self.__player_value: int = 0
        self.__doubled: bool = False

    def play(self, value: float, user_balance: float) -> float:
        self.__doubled = False
        self.__deck_of_cards.shuffle()

        self.__croupier = [self.__deck_of_cards.get_card(), self.__deck_of_cards.get_card()]
        self.__croupier_value = self.__get_cards_value(self.__croupier)

        self.__player = [self.__deck_of_cards.get_card(), self.__deck_of_cards.get_card()]
        self.__player_value = self.__get_cards_value(self.__player)

        if self.__player_value == 21:
            self.__print_cards()
            print("blackjack!!!, wygrales :)")
            return 2.5

        self.__print_cards(True)

        player_round = self.__player_round(value, user_balance)
        if player_round <= 0:
            print("twoj wynik jest powyzej 21, przegrales :(")
            return player_round

        if self.__croupier_round():
            if self.__player_value > self.__croupier_value:
                print("wygrales :)")
                return player_round
            elif self.__player_value == self.__croupier_value:
                print("remis :/")
                return 1
            elif self.__player_value < self.__croupier_value:
                print("przegrales :(")
                if self.__doubled:
                    return -1
                return 0

        print("wygrales :)")
        return player_round


    def __player_round(self, value: float, user_balance: float) -> float:
        print("-------------------------------------------")
        print("twoja runda")
        print("-------------------------------------------")
        choice = int(input("akcje: 1. dobierz karte | 2. zakoncz ture | 3. podwoj stawke\n"))

        if choice == 3 and user_balance >= value:
            self.__doubled = True
            self.__player.append(self.__deck_of_cards.get_card())
            self.__player_value = self.__get_cards_value(self.__player)
        elif choice == 3 and user_balance < value:
            print("nie masz budzetu na podwajanie :(")
            choice = 4

        if choice == 1 or choice == 4:
            while True:
                if choice == 1:
                    self.__player.append(self.__deck_of_cards.get_card())
                    self.__player_value = self.__get_cards_value(self.__player)

                if self.__player_value > 21:
                    break

                self.__print_cards(True)
                choice = int(input("akcje: 1. dobierz karte | 2. zakoncz ture\n"))
                if choice == 2:
                    break

        self.__print_cards()

        if self.__player_value > 21:
            if choice == 3:
                return -1
            return 0
        else:
            if choice == 3:
                return 3
            return 2


    def __croupier_round(self) -> bool:
        if self.__croupier_value >= 17:
            return True
        print("-------------------------------------------")
        print("runda krupiera")
        print("-------------------------------------------")
        while self.__croupier_value < 17:
            time.sleep(1.5)
            self.__croupier.append(self.__deck_of_cards.get_card())
            self.__croupier_value = self.__get_cards_value(self.__croupier)
            self.__print_cards()

        return self.__croupier_value <= 21


    def __print_cards(self, covered: bool = False) -> None:
        print("-------------------------------------------")
        if covered:
            print(f"krupier: {self.__croupier[0].get_figure()} ? | punkty: {self.__get_cards_value(self.__croupier[0:1])}")
        else:
            print(f"krupier: ", end=" ")
            for card in self.__croupier:
                print(card.get_figure(), end=" ")
            print(f"| punkty: {self.__croupier_value}")

        print(f"ty: ", end=" ")
        for card in self.__player:
            print(card.get_figure(), end=" ")
        print(f"| punkty: {self.__player_value}")
        print("-------------------------------------------")


    def __get_cards_value(self, cards: list[Card]) -> int:
        card_values: dict[str, int] = \
            {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
        value = 0
        aces = 0
        for card in cards:
            if card.get_figure() == "A":
                    value += 11
                    aces += 1
            else:
                value += card_values[card.get_figure()]

        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value
