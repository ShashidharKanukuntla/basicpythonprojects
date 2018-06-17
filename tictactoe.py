#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:52:09 2018

@author: shashidhar

Tic Tac Toe Game
"""

# Defining a function to print the board

def printboard(a):    
    print('                     --- --- --- ')
    print('                    | '+a[0][0]+' | '+a[0][1]+' | '+a[0][2]+' |') 
    print('                     --- --- --- ') 
    print('                    | '+a[1][0]+' | '+a[1][1]+' | '+a[1][2]+' |') 
    print('                     --- --- --- ') 
    print('                    | '+a[2][0]+' | '+a[2][1]+' | '+a[2][2]+' |') 
    print('                     --- --- --- ')

# This function returns 1 if player is won and 0 if not
    
def iswon(a,n): # Trying all different combinations to win the game
    if a[0][:]==[n,n,n] or a[1][:]==[n,n,n] or a[2][:]==[n,n,n]: # Checking all row combinations
        return 1 # If Won
    elif [a[0][0],a[1][0],a[2][0]] == [n,n,n] or [a[0][1],a[1][1],a[2][1]] == [n,n,n] or [a[0][2],a[1][2],a[2][2]] == [n,n,n]: # Checking all Column Combinations
        return 1 # If Won
    elif [a[0][0],a[1][1],a[2][2]] == [n,n,n] or [a[0][2],a[1][1],a[2][0]] == [n,n,n]: # Checking all diagonal combinations
        return 1 # If Won
    else:
        return 0 # If not Won

print('***************************WELCOME**********************************')
print('***************GET READY TO PLAY TIC TAC TOE************************')    
A = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] # Empty Board
printboard(A) # Printing the board
p1 = 1 # Intilaizing player 1 as default 1st player
p2 = 0
lst = [] # To store entered positions
Y = [0,0]
draw = 1 # Defines draw status of the game
chances = 9 # Initializing Maximum number of Chances
while True: # Infinite loop
    if (p1 == 1 and chances != 0): # Player 1 turn
        print('player 1 Turn')
        x = input('Enter position in row,col =') # Player 1 to enter his position
        if x in lst: # checking if the position entered is empty or not
            print('Sorry, that position is occupied')
            print('Please try another position')
            continue 
        # Splitting the entered string and seperating in terms of row and column
        y = x.split(',')
        try:
            Y[0] = int(y[0]) # Row position
            Y[1] = int(y[1]) # Column position
            A[Y[0]-1][Y[1]-1] = 'X' # Placing the symbol X at entered position
        except ValueError:
            print('Please enter only in terms of row,col  Eg. 2,2')
            continue
        except IndexError:
            print('Please enter values from 0,0 to 2,2')
            continue
        lst.append(x) # Appending the position to the list, if not present
        printboard(A) # Printing the updated board
        if (iswon(A,'X') == 1): # Checking whether the player 1 has won the game
            print('******Player 1 Won the Game********')
            print('>>>>>>>>>Congratulations<<<<<<<<<<<')
            draw = 0
            chances = 0
            continue
        # Giving next chance to player 2
        p1 = 0
        p2 = 1
        chances = chances -1 # Decreasing the number of remaining positions
    elif (p2 ==1 and chances !=0): # Player 2 turn
        print('player 2 Turn')
        x = input('Enter position (row,col) =') # Player 2 to enter his position
        if x in lst: # checking if the position entered is empty or not
            print('Sorry, that position is occupied')
            print('Please try another position')
            continue
        # Splitting the entered string and seperating in terms of row and column
        y = x.split(',')
        try:
            Y[0] = int(y[0]) # Row Position
            Y[1] = int(y[1]) # Column position
            A[Y[0]-1][Y[1]-1] = 'O' # Placing the symbol O at entered position
        except ValueError:
            print('Please enter only in terms of row,col  Eg 2,2')
            continue
        except IndexError:
            print('Please enter values from 0,0 to 2,2')
            continue
        lst.append(x) # Appending the position to the list, if not present
        printboard(A) # Printing the updated board
        if (iswon(A,'O') == 1): # Checking whether the player 2 has won the game
            print('******Player 2 Won the Game********')
            print('>>>>>>>>>Congratulations<<<<<<<<<<<')
            draw = 0
            chances = 0
            continue
        # Giving next chance to player 1
        p1 = 1
        p2 = 0
        chances = chances -1 # Decreasing the number of remaining positions
    if (chances == 0): # If gameplay is completed
        if draw == 1: # If game is drawn
            print('******Match Drawn**********')
        print('*************Well Played**************')
        print('********Wanna Play Once Again*******')
        print('''Press 1 to Play Again
              else Press any other key to exit''')
        sel = input() # Taking user input to play again or to exit
        if sel == '1':
            print('*********Welcome Back************')
            # Initilaizing all credentials for new game
            p1 = 1
            p2 = 0
            lst = []
            chances = 9
            draw = 1
            A = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
            printboard(A)
        else: # Exiting Game
            print('>>>>>>>>>SHUTTING DOWN............')
            break
        
        