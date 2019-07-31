# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 18:16:39 2019

@author: ngarcia
Python Milestone #1 assignment
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/04-Milestone%20Project%20-%201/01-Milestone%20Project%201%20-%20Assignment.ipynb
"""
#Imports
import time
import logging

#Initiate iterator 
i = 0 

#welcome message
print("Welcome to Tic Tac Toe in Python!")
time.sleep(2)

#intial player setup
player1_choice = input("There are two players, X and O. Enter either X or O for player 1. Player 2 gets the opposite by default.  ")
while player1_choice.lower() not in('x','o'):
    logging.warning("Only X's and O's allowed :/ .... Try Again")
    print(" ")
    player1_choice = input("Enter either X or O for player 1. Player 2 gets the opposite by default.  ")
    
if player1_choice.lower() == 'x':
    player2_choice = 'o'
else:
    player2_choice = 'x'

#Define first move
who_goes_first = input("Who will make the first move, X or O?  ")
while who_goes_first.lower() not in('x','o'):
    logging.warning("Only X's and O's allowed :/ .... Try Again ")
    print(" ")
    who_goes_first = input("Who will make the first move, X or O?  ")

#Quick explanation of game
print('{} moves first!'.format(who_goes_first.upper()))
time.sleep(1)
print(' ')
print("Before making a move, you'll need to familiarize yourself with the board.")
time.sleep(1)
print(' ')
print("  ",1,"  |  ",2,"  |  ",3,"  ")
print(" ---------------------")
print("  ",4,"  |  ",5,"  |  ",6,"  ")
print(" ---------------------")
print("  ",7,"  |  ",8,"  |  ",9,"  ")  
print(' ')
time.sleep(1)
print(' ')
print('In order to move to a particular cell, you need to choose the corresponding number of the board position.')
print(' ')
time.sleep(1)
print('Time to play!')
time.sleep(1)
print(' ')

 
#setting board variables
space1 = ''
space2 = ''
space3 = ''
space4 = ''
space5 = ''
space6 = ''
space7 = ''
space8 = ''
space9 = ''

#mapping board variables to numbers
mapdict = {
1:space1,
2:space2,
3:space3,
4:space4,
5:space5,
6:space6,
7:space7,
8:space8,
9:space9}

#turn tracking
KeepTrackOfTurnWithXStart = ['X','O','X','O','X','O','X','O','X']
KeepTrackOfTurnWithOStart = ['O','X','O','X','O','X','O','X','O']

if who_goes_first.lower() == 'x':
    KeepTrackOfTurn = KeepTrackOfTurnWithXStart
else:
    KeepTrackOfTurn = KeepTrackOfTurnWithOStart 


#begin game
while True:
    if i == 9:
        print("No winner. It's a draw")
        break
    while True:
        try:
            Move = int(input("{}, where do want to move? Enter the number of the location. ".format(KeepTrackOfTurn[i])))  
            break
        except ValueError:
            logging.error('Only integers are valid inputs. Enter a number between 1 and 9.')
            print(" ")
    while True:
         try:
            while Move < 1 or Move > 9:
                Move = int(input("Value must be between 1 and 9. "))
                if Move < 1 or Move > 9:
                    continue
                else:
                    break
            break
         except ValueError:    
            logging.error('Only integers are valid inputs. Enter a number between 1 and 9.')
    #take a space number input and map it to a space_id
    #only if that space is not empty 
    #and print the updated board to the screen
    while True:
        if mapdict[Move] != '':
            logging.error('Space is already taken. Try again.')
            print(' ')
            Move = int(input("Enter a different space. "))
        else:
            break
    mapdict[Move] = KeepTrackOfTurn[i]
    
    #Map and print player move
    if Move == 1:
        space1 = KeepTrackOfTurn[i]
    elif Move == 2:
        space2 = KeepTrackOfTurn[i]
    elif Move == 3:
        space3 = KeepTrackOfTurn[i]
    elif Move == 4:
        space4 = KeepTrackOfTurn[i]
    elif Move == 5:
        space5 = KeepTrackOfTurn[i]
    elif Move == 6:
        space6 = KeepTrackOfTurn[i]
    elif Move == 7:
        space7 = KeepTrackOfTurn[i]
    elif Move == 8:
        space8 = KeepTrackOfTurn[i]
    else:
        space9 = KeepTrackOfTurn[i]
    print(" ")
    print("  ",space1,"  |  ",space2,"  |  ",space3,"  ")
    print(" -------------------")
    print("  ",space4,"  |  ",space5,"  |  ",space6,"  ")
    print(" -------------------")
    print("  ",space7,"  |  ",space8,"  |  ",space9,"  ")        
    
    Win1 = space1 == space2 == space3 != ''
    Win2 = space4 == space5 == space6 != ''
    Win3 = space7 == space8 == space9 != ''
    Win4 = space1 == space5 == space9 != ''
    Win5 = space3 == space5 == space7 != ''
    Win6 = space1 == space4 == space7 != ''
    Win7 = space2 == space5 == space8 != ''
    Win8 = space3 == space6 == space9 != ''
    WinList = [Win1,Win2,Win3,Win4,Win5,Win6,Win7,Win8]

    #define winning moves
    if any(WinList) == True:
        print('{} wins!'.format(KeepTrackOfTurn[i]))
        break
    elif i == 9:
        print("No winner. It's a draw")
        break            
    else:
        i += 1
        continue

    
    
                
        




