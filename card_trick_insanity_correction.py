# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:28:19 2025

@author: maure

This algorithm reprodudes a card trick
"""
import time # Useful for stalling the reveal
cards=['K♣', 'K♥', 'K♠', 'K♦','Q♣', 'Q♥', 'Q♠', 'Q♦'] # Aranged cards 

even=[] # Empty list that will contain even indexes (0,2,4,6)
odd=[] # Empty list that will contain even indexes (1,3,5,7)

# For loop to fill the 2 above lists based on the length of the cards list
for i in range(0, len (cards)):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print('Chose a card : ', cards) # Ask the user to pick a card

def present_cards(cards_input, even_round):
    """ Function that presents cards and rearange the cards depending on user answer"""
    
    print([cards_input[j] for j in odd]) # print the odd cards
    spec_answer=input('Is your card here ? yes/no : ') # asks the spec if the card is printed
    
    # split the card into 2 packets odd cards and even cards
    odd_cards=[cards_input[j] for j in odd] 
    even_cards=[cards_input[j] for j in even]
    
    # Prevent user from mispelling yes or no
    while spec_answer!='no'and spec_answer!='yes': 
        print('Didn\'t catch that. Please answer \'yes\' or \'no\' : ')
        spec_answer=input('Is your card here ? yes/no : ')
    
    # If the round is the first or the third (0 or 2) : if the user says yes the odd cards goes on top, else the odd card goes on the bottom
    # If the round is the second (1) : if the user says yes the odd cards goes on the bottom, else the odd card goes on top
    if even_round==True:
        if spec_answer=='yes':
            cards_output=odd_cards+even_cards
            
        else:
            cards_output=even_cards+odd_cards
            
    else:
        if spec_answer=='yes':
            cards_output=even_cards+odd_cards
            
        else:
            cards_output=odd_cards+even_cards
            
    return cards_output # return cards that are rearanged
        
#%% Round 1 
print('\n Round 1 \n')
cards=present_cards(cards, True)
print(cards)
    
#%% Round 2   
print('\n Round 2 \n')  
cards=present_cards(cards, False)

#%% Round3    
print('\n Round 3 \n')    
cards=present_cards(cards, True)

    
#%% Reveal
print(' \n\n Reveal')  
time.sleep(2) # Pause for 2 seconds for dramatic effect

left_pile=[cards[j] for j in even][::-1] # put even cards in the 'left pile' and reverse order with [::-1]
right_pile=[cards[j] for j in odd][::-1] # put odd cards in the 'right pile' and reverse order with [::-1]

# If the first character of the first card in the right pile is 'K', the spectator chose a king, else a queen 
if right_pile[-1][0]=='K':
    head='KING'
else:
    head='QUEEN'
print('\nI sense you chose a ', head)
time.sleep(2)  # Pause for 2 seconds for dramatic effect

left_pile2=[left_pile[j] for j in even[0:2]][::-1] # put even cards from the left pile in the second 'left pile' and reverse order with [::-1]
right_pile2=[left_pile[j] for j in odd[0:2]][::-1] # put odd cards from the left pile in the second 'right pile' and reverse order with [::-1]
if (right_pile2[-1][1]=='♠')or (right_pile2[-1][1]=='♣'): # Check if the fist character of the first card of the second right pile is spade or clubs
    color='BLACK'
else:
    color='RED'    
print('\nSomething tells me it\'s a', color, 'card')
time.sleep(2)  # Pause for 2 seconds
print('\nYour card is : ', left_pile2[0]) # The first card of the second left pile is the card chosen by the spectator
input('\nPress \'Enter\' to close this tab ')
