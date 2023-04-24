import random                   # This module will be used to shuffle the deck of cards at the beginning of the game.

# Here i create global variables for cards.
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):

        self.all_cards = []

# I create 52 cards, every variation available.
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

# The deck created was created in order. Now the deck has to be shuffled.
    def shuffle(self):
        random.shuffle(self.all_cards)

# This method takes one card from the deck.
    def deal_one(self):
        return self.all_cards.pop()

# I create an instance for class Deck.


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):

            # Adds multiple cards to the list.
            self.all_cards.extend(new_cards)
        else:

            # Adds one card to the list.
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


def game_on():
    if len(deck.all_cards) > 0:
        return True
    else:
        return False


def replay():

    choice = ''

    while choice not in ['Y', 'N', 'y', 'n']:
        choice = input('Do You want to keep playing and start another military operation? (Y or N)')

        if choice not in ['Y', 'N', 'y', 'n']:
            print('Invalid typo. Type Y or N')

    if choice in ['Y', 'y']:
        return True
    else:
        print('OK. See You next time then.')
        return False


'''---------------------------------------------------------------------------------------------------------------------------------------------------------- \
                                                 'Game starts'''

while True:

    player1 = Player('Jedidiah')
    player2 = Player('Bartholomew')
    deck = Deck()
    deck.shuffle()

    for x in range(26):             # I deal the cards to the players. 52 / 2 = 26 per player.

        player1.add_cards(deck.deal_one())
        player2.add_cards(deck.deal_one())

    print('\t The game begins now \n \
    %s and %s.' % (player1, player2))

    play_game = input('\t Are you ready for battle? y or n?     ')  # START

    if play_game in ('y' or 'Y'):
        game_on = True
    else:
        print('Shame on You')
        break

    new_round = 0

    while game_on:
        new_round += 1
        print(f'Round {new_round}:')

        if new_round >= 1000:                           # A draw scenario.
            print('The game cannot be resolved within a 1000 rounds. It\'s a draw')
            break

        # The game ending
        if len(player1.all_cards) == 0:
            print('Player 1 has run out of cards. Player 2 wins. Congrats!!!')
            game_on = False
            break
        elif len(player2.all_cards) == 0:
            print('Player 2 has run out of cards. Player 1 wins. Congrats!!!')
            game_on = False
            break

        # NEW ROUND
        player1_cards = []
        player1_cards.append(player1.remove_one())
        player2_cards = []
        player2_cards.append(player2.remove_one())

        # WAR
        at_war = True

        while at_war:
            # [-1] because we have to draw the card from the end of the list.
            if player1_cards[-1].value > player2_cards[-1].value:
                print('Player 1\'s card power is %d and Player 2\'s card power is %d. Player 1 wins the round.' % (player1_cards[-1].value, player2_cards[-1].value))
                player1.add_cards(player1_cards)
                player1.add_cards(player2_cards)
                at_war = False

            elif player1_cards[-1].value < player2_cards[-1].value:
                print('Player 1\'s card power is %d and Player 2\'s card power is %d. Player 2 wins the round.' % (player1_cards[-1].value, player2_cards[-1].value))
                player2.add_cards(player1_cards)
                player2.add_cards(player2_cards)
                at_war = False

            else:
                # Cards are equal, so it is war.
                print('  \t\t\t\t\t\t   THIS IS WAR:')

                if len(player1.all_cards) < 5:
                    print('  \t\t\t\t\t\t   Player 1 is unable to fight the war, because he has less than 5 cards left.')
                    print('  \t\t\t\t\t\t   Player 2 wins. Congrats!!!')
                    game_on = False
                    break
                elif len(player2.all_cards) < 5:
                    print('  \t\t\t\t\t\t   Player 2 is unable to fight the war, because he has less than 5 cards left.')
                    print('  \t\t\t\t\t\t   Player 1 wins. Congrats!!!')
                    game_on = False
                    break
                else:
                    print('  \t\t\t\t\t\t   The power of both cards are: %d.' % player1_cards[-1].value)
                    print('  \t\t\t\t\t\t   The war consumed 5 cards from each player.')
                    print(' \
                          Player 1 is now left with %d cards, \n \
                          Player 2 is now left with %d cards.' % (len(player1.all_cards), len(player2.all_cards)))

                    for x in range(5):
                        player1_cards.append(player1.remove_one())
                        player2_cards.append(player2.remove_one())
                    continue

# REPLAY?
    if replay():
        new_round = 0
        deck = Deck()
        deck.shuffle()
    else:
        print('Thanks for the game.')
        break
