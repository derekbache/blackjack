import random

class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return f"PlayingCard({self.rank},{self.suit})"

class StandardDeck:
    def __init__(self):
        self.card_list = []

        all_ranks = (2,3,4,5,6,7,8,9,10,'J','Q','K','A')
        clubs = "\u2663"
        diamonds = "\u2666"
        hearts = "\u2665"
        spades = "\u2660"
        suits = (clubs, diamonds, hearts, spades)

        for suit in suits:
            for rank in all_ranks:
                self.card_list.append(PlayingCard(rank, suit))

    def __str__(self):
        return '[' + ', '.join(str(card) for card in self.card_list) + ']'

class Shoe:
    def __init__(self, num_decks):
        self.card_list = []
        for i in range(num_decks):
            deck = StandardDeck()
            self.card_list.extend(deck.card_list)

    def __str__(self):
        return '[' + ', '.join(str(card) for card in self.card_list) + ']'

    def shuffle(self):
        random.shuffle(self.card_list)

    def draw(self, num_cards):
        drawn_cards = []
        for i in range(num_cards):
            drawn_cards.append(self.card_list.pop())
        return drawn_cards

class Hand:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        return ', '.join(str(card) for card in self.card_list)

class DiscardPile:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        return ', '.join(str(card) for card in self.card_list)

class Player:
    def __init__(self, isDealer):
        self.isDealer = isDealer
        self.money = 100
        self.hand = Hand()

    def __str__(self):
        if self.isDealer:
            return f"Dealer: {self.hand}"
        else:
            return f"Player: {self.hand}"

class GameState:
    def __init__(self):
        players = []
        dealer = Player(True)
        player = Player(False)
        players.append(dealer)
        players.append(player)

        shoe = Shoe(1)
        shoe.shuffle()

        discard = DiscardPile()

        player.hand.card_list.extend(shoe.draw(2))
        dealer.hand.card_list.extend(shoe.draw(2))
        print(shoe)
        print(player)
        print(score_hand(player.hand))
        print(dealer)

def score_hand(hand):
    score = 0
    for card in hand.card_list:
        if card.rank in ['A', 'K', 'Q', 'J']:
            score += 10
        else:
            score += card.rank
    return score

def main():
    game = GameState()

main()
