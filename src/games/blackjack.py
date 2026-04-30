from src.games import Game
from src.models import Card
from src.services import DeckOfCards

class Blackjack(Game):
    def __init__(self, deck_of_cards: DeckOfCards):
        self.__deck_of_cards: DeckOfCards = deck_of_cards

    def play(self) -> float:
        self.__deck_of_cards.shuffle()
        croupier = [self.__deck_of_cards.get_card(), self.__deck_of_cards.get_card()]
        player = [self.__deck_of_cards.get_card(), self.__deck_of_cards.get_card()]

        print(f"krupier:\n {croupier[0].get_figure()} ?")
        print(f"ty:\n")
        self.__print_cards(player)

        print("akcje:")
        print("1. dobierz karte")
        print("2. zakoncz ture")

    def __print_cards(self, cards: list[Card]):
        for card in cards:
            print(card.get_figure(), end=" ")
        print("")
