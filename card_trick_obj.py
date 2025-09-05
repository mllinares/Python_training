# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 09:09:27 2025

@author: maure
"""

import time

class CardTrick:
    def __init__(self):
        self.cards = ['K♣', 'K♥', 'K♠', 'K♦', 'Q♣', 'Q♥', 'Q♠', 'Q♦'];
        self.even = [i for i in range(len(self.cards)) if i % 2 == 0]
        self.odd = [i for i in range(len(self.cards)) if i % 2 != 0]
        return

    def present_cards(self, even_round):
        
        print([self.cards[j] for j in self.odd])
        spec_answer = input('Is your card here? yes/no: ').strip().lower()

        while spec_answer not in ['yes', 'no']:
            print("Didn't catch that. Please answer 'yes' or 'no'.")
            spec_answer = input('Is your card here? yes/no: ').strip().lower()

        odd_cards = [self.cards[j] for j in self.odd]
        even_cards = [self.cards[j] for j in self.even]

        if even_round:
            self.cards = odd_cards + even_cards if spec_answer == 'yes' else even_cards + odd_cards
        else:
            self.cards = even_cards + odd_cards if spec_answer == 'yes' else odd_cards + even_cards
        return

    def reveal_card(self):
        print('\n\nReveal...')
        time.sleep(2)

        left_pile = [self.cards[j] for j in self.even][::-1]
        right_pile = [self.cards[j] for j in self.odd][::-1]

        head = 'KING' if right_pile[-1][0] == 'K' else 'QUEEN'
        print(f'\nI sense you chose a {head}')
        time.sleep(2)

        left_pile2 = [left_pile[j] for j in self.even[0:2]][::-1]
        right_pile2 = [left_pile[j] for j in self.odd[0:2]][::-1]

        color = 'BLACK' if right_pile2[-1][1] in ['♠', '♣'] else 'RED'
        print(f"\nSomething tells me it's a {color} card")
        time.sleep(2)

        print('\nYour card is:', left_pile2[0])
        input("\nPress 'Enter' to close this tab")
        return

    def run(self):
        print('\nChose a card:', self.cards)
        
        print('\nRound 1')
        self.present_cards(even_round=True)

        print('\nRound 2')
        self.present_cards(even_round=False)

        print('\nRound 3')
        self.present_cards(even_round=True)

        self.reveal_card()
        return

# Run the trick
if __name__ == "__main__":
    
    trick = CardTrick()
    trick.run()
