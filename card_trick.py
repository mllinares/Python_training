# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:28:19 2025

@author: maure

This algorithm reprodudes a card trick 
"""

import time # useful to stall the reveal

cards=['K♣', 'K♥', 'K♠', 'K♦','Q♣', 'Q♥', 'Q♠', 'Q♦'] # Aranged cards 

print('Chose a card : ', cards) # Ask the spectator to pick a card
even=[] # Empty list that will contain even indexes (0,2,4,6)
odd=[] # Empty list that will contain even indexes (1,3,5,7)

# For loop to fill the 2 above lists based on the length of the cards list
for i in range(0, len (cards)):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

#%% Round 1
print('\n Round 1 \n')
print([cards[j] for j in odd]) # print odd cards
answer1=input('Is your card here ? yes/no : ')

# split the card into 2 packets odd cards and even cards
odd_cards=[cards[j] for j in odd]
even_cards=[cards[j] for j in even]

# If the user says yes the odd cards goes on top, else the odd card goes on the bottom
if answer1=='yes':
    cards=odd_cards+even_cards
    
else:
    cards=even_cards+odd_cards
    
#%% Round 2    
print('\n Round 2 \n')  
print([cards[j] for j in odd])
answer2=input('Is your card here ? yes/no : ')

# split the card into 2 packets odd cards and even cards
odd_cards=[cards[j] for j in odd]
even_cards=[cards[j] for j in even]

# If the user says yes the odd cards goes on the bottom, else the odd card goes on top
if answer1=='yes':
    cards=odd_cards+even_cards
    
else:
    cards=even_cards+odd_cards
    

#%% Round3
print('\n Round 3 \n')    
print([cards[j] for j in odd])
answer3=input('Is your card here ? yes/no : ')

# split the card into 2 packets odd cards and even cards
odd_cards=[cards[j] for j in odd]
even_cards=[cards[j] for j in even]

# If the user says yes the odd cards goes on top, else the odd card goes on the bottom
if answer1=='yes':
    cards=odd_cards+even_cards
    
else:
    cards=even_cards+odd_cards
    
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