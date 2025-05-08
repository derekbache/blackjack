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
        self.dealer = Player(True)
        self.player = Player(False)
        self.round = 0
        self.shoe = Shoe(1)
        self.shoe.shuffle()
        self.discard = DiscardPile()

    def start_game(self):
        while self.player.money > 0:
            self.draw(self.player, 2)
            self.draw(self.dealer, 2)
            self.display_hands()
            self.bet()
            self.turn_actions()

    def draw(self, player, num_cards):
        player.hand.card_list.extend(self.shoe.draw(num_cards))

    def display_hands(self):
        print(self.player)
        print(self.dealer)

    def bet(self):
        amount = input('Enter your bet:')
        self.player.money - int(amount)

    def turn_actions(self):
        chosen_action = input('1 to hit, 2 to check')
        if chosen_action == '1':
            self.draw(self.player, 1)
            self.display_hands()
            self.turn_actions()
        if chosen_action == '2':
            while score_hand(self.dealer.hand) < 17:
                self.draw(self.dealer, 1)
            if score_hand(self.dealer.hand) > 21:
                print('Dealer busts!')
                self.display_hands()
            else:
                self.display_hands()
                if score_hand(self.player.hand) > score_hand(self.dealer.hand):
                    print('Player wins!')
                elif score_hand(self.player.hand) == score_hand(self.dealer.hand):
                    print('Tie!')
                else: 
                    print('Dealer wins!')
        self.end_round()

    def end_round(self):
        for i in range(len(self.player.hand.card_list)):
            self.discard.card_list.append(self.player.hand.card_list.pop())
        for i in range(len(self.dealer.hand.card_list)):
            self.discard.card_list.append(self.dealer.hand.card_list.pop())
        print('End of round, starting next round')


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
    game.start_game()

main()
