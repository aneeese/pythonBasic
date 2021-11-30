#Tic Tac Toe Game
print("\t\t\t ________-------------------------_________")
print("\n \t\t\t\tT I C   T A C   T O E   G A M E ")
print("\t\t\t __________________________________________")
print("\n\t\t\t\t\tW E L C O M E")
print("\t\t\t --------_________________________---------")
print("\n")


    
#Function to display Menu to user
def main():
    choice = eval(input("\nPlease select a mode you want to play.\n\
\n\tPress 1 for Player vs Computer or\n\t\tPress 2 for Player vs Player: "))
    if choice == 1:
        choose = eval(input("\nPress 1 for Easy game or \n\tPress 2 for Medium or \n\t\tPress 3 for Hard game mode: "))
        if choose == 1:
            singleEasygame()
        elif choose == 2:
            singleMediumgame()
        elif choose == 3:
            singleHardgame()
        else:
            singleHardgame()
    elif choice == 2:
        pref = input("\nPress T for a tournament or\nPress S for a single game: ")
        if pref == 'T' or pref == 't':
            tournament()
        else:
            twoPlayers()
    else:
        print("\nWrong Input!")
        main()


    
#Function to display Scoreboard to user
def scoreboard(p1,p2,player1,player2):
    print("\n\t\t\tS C O R E B O A R D")
    print("\t\t ________________________________\n")
    print("\t\t" ,player1, "|", p1)
    print("\n\t\t -----------------------\n")
    print("\t\t" ,player2, "|", p2)
    print("\t\t _______________\n")



#Fuction used to display Grid
board = [1,2,3,4,5,6,7,8,9]
def grid(board,symbol_1,symbol_2):
    print(board[0],"|",board[1],"|",board[2])
    print("-----------")
    print(board[3],"|",board[4],"|",board[5])
    print("-----------")
    print(board[6],"|",board[7],"|",board[8])
    print("-----------\n")


import random
#Function used for Toss
def toss(Toss,player1,player2,symbol_1,symbol_2):
    if Toss == 0:
        print(player1, "won the toss\n")
    else:
        print(player2, "won the toss\n")
        
    print(player1, "symbol is", symbol_1)
    print(player2, "symbol is", symbol_2,"\n")


          
#Function used to insert symbol when player 1 wins the Toss
def putsymbol_1(turn,turn1,board,symbol_1,symbol_2):
    if turn1 == 1:
    #Condition to check if entered number has a free slot or not 
        if board[0] != symbol_1 and board[0] != symbol_2:
        #Condition to insert symbol
            if turn%2 == 0:
                board[0] = symbol_2
            else:
                board[0] = symbol_1
    #Condition if slot is not empty
        else:
            return 5
    elif turn1 == 2:
        if board[1] != symbol_1 and board[1] != symbol_2:
            if turn%2 == 0:
                board[1] = symbol_2
            else:
                board[1] = symbol_1
        else:
            return 5
    elif turn1 == 3:
        if board[2] != symbol_1 and board[2] != symbol_2:
            if turn%2 == 0:
                board[2] = symbol_2
            else:
                board[2] = symbol_1
        else:
            return 5
    elif turn1 == 4:
        if board[3] != symbol_1 and board[3] != symbol_2:
            if turn%2 == 0:
                board[3] = symbol_2
            else:
                board[3] = symbol_1
        else:
            return 5
    elif turn1 == 5:
        if board[4] != symbol_1 and board[4] != symbol_2:
            if turn%2 == 0:
                board[4] = symbol_2
            else:
                board[4] = symbol_1
        else:
            return 5
    elif turn1 == 6:
        if board[5] != symbol_1 and board[5] != symbol_2:
            if turn%2 == 0:
                board[5] = symbol_2
            else:
                board[5] = symbol_1
        else:
            return 5
    elif turn1 == 7:
        if board[6] != symbol_1 and board[6] != symbol_2:
            if turn%2 == 0:
                board[6] = symbol_2
            else:
                board[6] = symbol_1                  
        else:
            return 5
    elif turn1 == 8:
        if board[7] != symbol_1 and board[7] != symbol_2:
            if turn%2 == 0:
                board[7] = symbol_2
            else:
                board[7] = symbol_1                
        else:
            return 5
    elif turn1 == 9:
        if board[8] != symbol_1 and board[8] != symbol_2:
            if turn%2 == 0:
                board[8] = symbol_2
            else:
                board[8] = symbol_1
        else:
            return 5
    #Condition if input is not valid
    else:
        return 6
    #displaying grid after each move
    grid(board,symbol_1,symbol_2)
    #Changing move
    turn += 1




#Function used to insert symbol when player 2 wins the Toss
def putsymbol_2(turn,turn1,board,symbol_1,symbol_2):
    if turn1 == 1:
    #Condition to check if entered number has a free slot or not 
        if board[0] != symbol_1 and board[0] != symbol_2:
            #Condition to insert symbol
            if turn%2 == 0:
                board[0] = symbol_1
            else:
                board[0] = symbol_2
    #Condition if slot is not empty
        else:
            return 5
    elif turn1 == 2:
        if board[1] != symbol_1 and board[1] != symbol_2:
            if turn%2 == 0:
                board[1] = symbol_1
            else:
                board[1] = symbol_2
        else:
            return 5 
    elif turn1 == 3:
        if board[2] != symbol_1 and board[2] != symbol_2:
            if turn%2 == 0:
                board[2] = symbol_1
            else:
                board[2] = symbol_2
        else:
            return 5
    elif turn1 == 4:
        if board[3] != symbol_1 and board[3] != symbol_2:
            if turn%2 == 0:
                board[3] = symbol_1
            else:
                board[3] = symbol_2
        else:
            return 5
    elif turn1 == 5:
        if board[4] != symbol_1 and board[4] != symbol_2:
            if turn%2 == 0:
                board[4] = symbol_1
            else:
                board[4] = symbol_2
        else:
            return 5   
    elif turn1 == 6:
        if board[5] != symbol_1 and board[5] != symbol_2:
            if turn%2 == 0:
                board[5] = symbol_1
            else:
                board[5] = symbol_2
        else:
            return 5
    elif turn1 == 7:
        if board[6] != symbol_1 and board[6] != symbol_2:
            if turn%2 == 0:
                board[6] = symbol_1
            else:
                board[6] = symbol_2                 
        else:
            return 5
    elif turn1 == 8:
        if board[7] != symbol_1 and board[7] != symbol_2:
            if turn%2 == 0:
                board[7] = symbol_1
            else:
                board[7] = symbol_2                
        else:
            return 5
    elif turn1 == 9:
        if board[8] != symbol_1 and board[8] != symbol_2:
            if turn%2 == 0:
                board[8] = symbol_1
            else:
                board[8] = symbol_2
        else:
            return 5
    #Condition if input is not valid
    else:
        return 6
    #displaying grid after each move
    grid(board,symbol_1,symbol_2)
    #changing move
    turn +=1




#Function to check winning or draw conditions
def windrawcondi(board,turn,symbol_1,symbol_2):
    if (board[0] == symbol_1 and board[1] == symbol_1 and board[2] == symbol_1) or \
        (board[3] == symbol_1 and board[4] == symbol_1 and board[5] == symbol_1) or \
        (board[6] == symbol_1 and board[7] == symbol_1 and board[8] == symbol_1) or \
        (board[0] == symbol_1 and board[3] == symbol_1 and board[6] == symbol_1) or \
        (board[1] == symbol_1 and board[4] == symbol_1 and board[7] == symbol_1) or \
        (board[2] == symbol_1 and board[5] == symbol_1 and board[8] == symbol_1) or \
        (board[0] == symbol_1 and board[4] == symbol_1 and board[8] == symbol_1) or \
        (board[2] == symbol_1 and board[4] == symbol_1 and board[6] == symbol_1):
        return 1
    elif (board[0] == symbol_2 and board[1] == symbol_2 and board[2] == symbol_2) or \
        (board[3] == symbol_2 and board[4] == symbol_2 and board[5] == symbol_2) or \
        (board[6] == symbol_2 and board[7] == symbol_2 and board[8] == symbol_2) or \
        (board[0] == symbol_2 and board[3] == symbol_2 and board[6] == symbol_2) or \
        (board[1] == symbol_2 and board[4] == symbol_2 and board[7] == symbol_2) or \
        (board[2] == symbol_2 and board[5] == symbol_2 and board[8] == symbol_2) or \
        (board[0] == symbol_2 and board[4] == symbol_2 and board[8] == symbol_2) or \
        (board[2] == symbol_2 and board[4] == symbol_2 and board[6] == symbol_2):
        return 2
    elif turn == 9:
        return 3




#Function for single player easy mode
def singleEasygame():
    #variable for counting wins
    p1 = 0
    p2 = 0
    #players info
    player1 = str(input("\nPlayer name: "))
    symbol_1 = 'O'
    player2 = 'System'
    symbol_2 = 'X'
    #loop for repition of game
    menu = 'Y'
    while menu == 'Y' or menu == 'y':
        #list for Grid
        board = [1,2,3,4,5,6,7,8,9]
        grid(board,symbol_1,symbol_2)
        #Toss
        Toss = random.randint(0,1)
        toss(Toss,player1,player2,symbol_1,symbol_2)

#If player wins the toss
        if Toss == 0:
            #Loop for moves of game untill someone wins or game is drawn
            turn = 1
            while turn <= 10:
                #Using number of moves for changing the turn
                if turn%2 == 0:
                    print("System turn")
                #Conditions for 1st column
                    if ((board[0] == symbol_1 and board[3] == symbol_1) and (board[6] != symbol_1 and board[6] != symbol_2)):
                        turn1  = 7
                    elif ((board[3] == symbol_1 and board[6] == symbol_1) and (board[0] != symbol_1 and board[0] != symbol_2)):                     
                        turn1 = 1
                    elif ((board[0] == symbol_1 and board[6] == symbol_1) and (board[3] != symbol_1 and board[3] != symbol_2)):
                        turn1 = 4
                #Conditions for 2nd column
                    elif ((board[1] == symbol_1 and board[4] == symbol_1) and (board[7] != symbol_1 and board[7] != symbol_2)):
                        turn1 = 8
                    elif ((board[4] == symbol_1 and board[7] == symbol_1) and (board[1] != symbol_1 and board[1] != symbol_2)):
                        turn1 = 2
                    elif ((board[1] == symbol_1 and board[7] == symbol_1) and (board[4] != symbol_1 and board[4] != symbol_2)):
                        turn1 = 5
                #Conditions for 3rd column
                    elif ((board[2] == symbol_1 and board[5] == symbol_1) and (board[8] != symbol_1 and board[8] != symbol_2)):
                        turn1 = 9
                    elif ((board[5] == symbol_1 and board[8] == symbol_1) and (board[2] != symbol_1 and board[2] != symbol_2)):
                        turn1 = 3                
                    elif ((board[2] == symbol_1 and board[8] == symbol_1) and (board[5] != symbol_1 and board[5] != symbol_2)):
                        turn1 = 6
                #Conditions for left to right diagonal
                    elif ((board[0] == symbol_1 and board[4] == symbol_1) and (board[8] != symbol_1 and board[8] != symbol_2)):
                        turn1 = 9
                    elif ((board[4] == symbol_1 and board[8] == symbol_1) and (board[0] != symbol_1 and board[0] != symbol_2)):
                        turn1 = 1
                    elif ((board[0] == symbol_1 and board[8] == symbol_1) and (board[4] != symbol_1 and board[4] != symbol_2)):
                        turn1 = 5
                #Conditions for right to left diagonal
                    elif ((board[2] == symbol_1 and board[4] == symbol_1) and (board[6] != symbol_1 and board[6] != symbol_2)):
                        turn1 = 7
                    elif ((board[4] == symbol_1 and board[6] == symbol_1) and (board[2] != symbol_1 and board[2] != symbol_2)):
                        turn1 = 3               
                    elif ((board[2] == symbol_1 and board[6] == symbol_1) and (board[4] != symbol_1 and board[4] != symbol_2)):
                        turn1 = 5
                #Conditions for 1st row
                    elif ((board[0] == symbol_1 and board[1] == symbol_1) and (board[2] != symbol_1 and board[2] != symbol_2)):
                        turn1 = 3
                    elif ((board[1] == symbol_1 and board[2] == symbol_1) and (board[0] != symbol_1 and board[0] != symbol_2)):
                        turn1 = 1
                    elif ((board[0] == symbol_1 and board[2] == symbol_1) and (board[1] != symbol_1 and board[1] != symbol_2)):
                        turn1 = 2
                #Conditions for 2nd row
                    elif ((board[3] == symbol_1 and board[4] == symbol_1) and (board[5] != symbol_1 and board[5] != symbol_2)):
                        turn1 = 6
                    elif ((board[4] == symbol_1 and board[5] == symbol_1) and (board[3] != symbol_1 and board[3] != symbol_2)):
                        turn1 = 4
                    elif ((board[3] == symbol_1 and board[5] == symbol_1) and (board[4] != symbol_1 and board[4] != symbol_2)):
                        turn1 = 5
                #Conditions for 3rd row
                    elif ((board[6] == symbol_1 and board[7] == symbol_1) and (board[8] != symbol_1 and board[8] != symbol_2)):
                        turn1 = 9
                    elif ((board[7] == symbol_1 and board[8] == symbol_1) and (board[6] != symbol_1 and board[6] != symbol_2)):
                        turn1 = 7
                    elif ((board[6] == symbol_1 and board[8] == symbol_1) and (board[7] != symbol_1 and board[7] != symbol_2)):
                        turn1 = 8
                    else:
                        #If above conditions are not fulfilled
                        if ((board[0] != symbol_1) and (board[0] != symbol_2)):
                            turn1 = 1
                        elif ((board[1] != symbol_1) and (board[1] != symbol_2)):
                            turn1 = 2
                        elif ((board[2] != symbol_1) and (board[2] != symbol_2)):
                            turn1 = 3
                        elif ((board[3] != symbol_1) and (board[3] != symbol_2)):
                            turn1 = 4
                        elif ((board[6] != symbol_1) and (board[6] != symbol_2)):
                            turn1 = 5
                        elif ((board[5] != symbol_1) and (board[5] != symbol_2)):
                            turn1 = 6
                        elif ((board[6] != symbol_1) and (board[6] != symbol_2)):
                            turn1 = 7
                        elif ((board[7] != symbol_1) and (board[7] != symbol_2)):
                            turn1 = 8
                        elif ((board[8] != symbol_1) and (board[8] != symbol_2)):
                            turn1 = 9
                else:
                    turn1 = eval(input(player1 +" turn: "))
                    
            #Conditions for putting symbols 
                diff = putsymbol_1(turn,turn1,board,symbol_1,symbol_2)
                if diff == 5:
                    turn -= 1
                    print("\nBox is already occupied.\nPlease enter another box\n")
                    grid(board,symbol_1,symbol_2)
                elif diff == 6:
                    turn -= 1
                    print("\nEntered number is invalid.\nEnter a valid number\n")
                    grid(board,symbol_1,symbol_2)
                    
            #Winning and draw conditions
                check = windrawcondi(board,turn,symbol_1,symbol_2)
                if check == 1:
                    print(player1, "wins this match")
                    p1 += 1
                    break
                elif check == 2:
                    print(player2, "wins this match")
                    p2 += 1
                    break
                elif check == 3:
                    print("Match Drawn!")
                    break
                turn +=1


#If system wins the toss
        if Toss == 1:
        #Loop for moves of game untill someone wins or game is drawn
            turn = 1
            while turn <= 10:
        #Using number of moves for changing the turn
                if turn%2 == 0:
                    turn1 = eval(input(player1 +" turn: "))
                else:
                    print("System Turn")
            #Conditions for 1st column in grid
                    if ((board[0] == symbol_2 and board[3] == symbol_2) and (board[6] != symbol_1 and board[6] != symbol_2)):
                        turn1 = 7
                    elif ((board[3] == symbol_2 and board[6] == symbol_2) and (board[0] != symbol_1 and board[0] != symbol_2)):                     
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[6] == symbol_2) and (board[3] != symbol_1 and board[3] != symbol_2)):
                        turn1 = 4
            #Conditions for 2nd column
                    elif ((board[1] == symbol_2 and board[4] == symbol_2) and (board[7] != symbol_1 and board[7] != symbol_2)):
                        turn1 = 8
                    elif ((board[4] == symbol_2 and board[7] == symbol_2) and (board[1] != symbol_1 and board[1] != symbol_2)):
                        turn1 = 2
                    elif ((board[1] == symbol_2 and board[7] == symbol_2) and (board[4] != symbol_1 and board[4] != symbol_2)):
                        turn1 = 5
            #Conditions for 3rd column
                    elif ((board[2] == symbol_2 and board[5] == symbol_2) and (board[8] != symbol_1 and board[8] != symbol_2)):
                        turn1 = 9
                    elif ((board[5] == symbol_2 and board[8] == symbol_2) and (board[2] != symbol_1 and board[2] != symbol_2)):
                        turn1 = 3                
                    elif ((board[2] == symbol_2 and board[8] == symbol_2) and (board[5] != symbol_1 and board[5] != symbol_2)):
                        turn1 = 6
            #Conditions for left to right diagonal
                    elif ((board[0] == symbol_2 and board[4] == symbol_2) and (board[8] != symbol_1 and board[8] != symbol_2)):
                        turn1 = 9
                    elif ((board[4] == symbol_2 and board[8] == symbol_2) and (board[0] != symbol_1 and board[0] != symbol_2)):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[8] == symbol_2) and (board[4] != symbol_1 and board[4] != symbol_2)):
                        turn1 = 5
            #Conditions for right to left diagonal
                    elif ((board[2] == symbol_2 and board[4] == symbol_2) and (board[6] != symbol_1 and board[6] != symbol_2)):
                        turn1 = 7
                    elif ((board[4] == symbol_2 and board[6] == symbol_2) and (board[2] != symbol_1 and board[2] != symbol_2)):
                        turn1 = 3               
                    elif ((board[2] == symbol_2 and board[6] == symbol_2) and (board[4] != symbol_1 and board[4] != symbol_2)):
                        turn1 = 5
            #Conditions for 1st row
                    elif ((board[0] == symbol_2 and board[1] == symbol_2) and (board[2] != symbol_1 and board[2] != symbol_2)):
                        turn1 = 3
                    elif ((board[1] == symbol_2 and board[2] == symbol_2) and (board[0] != symbol_1 and board[0] != symbol_2)):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[2] == symbol_2) and (board[1] != symbol_1 and board[1] != symbol_2)):
                        turn1 = 2
            #Conditions for 2nd row
                    elif ((board[3] == symbol_2 and board[4] == symbol_2) and (board[5] != symbol_1 and board[5] != symbol_2)):
                        turn1 = 6
                    elif ((board[4] == symbol_2 and board[5] == symbol_2) and (board[3] != symbol_1 and board[3] != symbol_2)):
                        turn1 = 4
                    elif ((board[3] == symbol_2 and board[5] == symbol_2) and (board[4] != symbol_1 and board[4] != symbol_2)):
                        turn1 = 5
            #Conditions for 3rd row
                    elif ((board[6] == symbol_2 and board[7] == symbol_2) and (board[8] != symbol_1 and board[8] != symbol_2)):
                        turn1 = 9
                    elif ((board[7] == symbol_2 and board[8] == symbol_2) and (board[6] != symbol_1 and board[6] != symbol_2)):
                        turn1 = 7
                    elif ((board[6] == symbol_2 and board[8] == symbol_2) and (board[7] != symbol_1 and board[7] != symbol_2)):
                        turn1 = 8
                    else:
                        #Conditions for 1st turn of system
                        if ((board[0] != symbol_1) and (board[0] != symbol_2)):
                            turn1 = 1
                        elif ((board[1] != symbol_1) and (board[1] != symbol_2)):
                            turn1 = 2
                        elif ((board[2] != symbol_1) and (board[2] != symbol_2)):
                            turn1 = 3
                        elif ((board[3] != symbol_1) and (board[3] != symbol_2)):
                            turn1 = 4
                        elif ((board[6] != symbol_1) and (board[6] != symbol_2)):
                            turn1 = 5
                        elif ((board[5] != symbol_1) and (board[5] != symbol_2)):
                            turn1 = 6
                        elif ((board[6] != symbol_1) and (board[6] != symbol_2)):
                            turn1 = 7
                        elif ((board[7] != symbol_1) and (board[7] != symbol_2)):
                            turn1 = 8
                        elif ((board[8] != symbol_1) and (board[8] != symbol_2)):
                            turn1 = 9
                            
            #Conditions for putting symbols
                diff = putsymbol_2(turn,turn1,board,symbol_1,symbol_2)
                if diff == 5:
                    turn -= 1
                    print("\nBox is already occupied.\nPlease enter another box\n")
                    grid(board,symbol_1,symbol_2)
                elif diff == 6:
                    print("\nEntered number is invalid.\nEnter a valid number\n")
                    turn -= 1
                    grid(board,symbol_1,symbol_2)
                    
            #Winning and draw conditions
                check = windrawcondi(board,turn,symbol_1,symbol_2)
                if check == 1:
                    print(player1, "wins this match")
                    p1 += 1
                    break
                elif check == 2:
                    print(player2, "wins this match")
                    p2 += 1
                    break
                elif check == 3:
                    print("Match Drawn!")
                    break
                #Changing turn
                turn += 1
        #Displaying Scoreboard
        scoreboard(p1,p2,player1,player2)
        #Displaying menu at the end of game
        menu = str(input("\nEnter Y to continue game or\
\n\tEnter M to go to main menu or\n\t\tEnter E to exit the game: "))
        if menu == 'M' or menu == 'm':
            main()



#Function for single player medium mode
def singleMediumgame():
    #variable for counting wins
    p1 = 0
    p2 = 0
    #players info
    player1 = str(input("\nPlayer name: "))
    symbol_1 = 'O'
    player2 = 'System'
    symbol_2 = 'X'
    #loop for repition of game
    menu = 'Y'
    while menu == 'Y' or menu == 'y':
        #list for Grid
        board = [1,2,3,4,5,6,7,8,9]
        grid(board,symbol_1,symbol_2)
        #Toss
        Toss = random.randint(0,1)
        toss(Toss,player1,player2,symbol_1,symbol_2)

#If player wins the toss
        if Toss == 0:
            #Loop for moves of game untill someone wins or game is drawn
            turn = 1
            while turn <= 10:
                #Using number of moves for changing the turn
                if turn%2 == 0:
                    print("System turn")
            #Conditions for 1st column in grid
                    if ((board[0] == symbol_2 and board[3] == symbol_2) or (board[0] == symbol_1 and board[3] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1  = 7
                    elif ((board[3] == symbol_2 and board[6] == symbol_2) or (board[3] == symbol_1 and board[6] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):                     
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[6] == symbol_2) or (board[0] == symbol_1 and board[6] == symbol_1)) and \
                         (board[3] != symbol_1 and board[3] != symbol_2):
                        turn1 = 4
            #Conditions for 2nd column
                    elif ((board[1] == symbol_2 and board[4] == symbol_2) or (board[1] == symbol_1 and board[4] == symbol_1)) and \
                         (board[7] != symbol_1 and board[7] != symbol_2):
                        turn1 = 8
                    elif ((board[4] == symbol_2 and board[7] == symbol_2) or (board[4] == symbol_1 and board[7] == symbol_1)) and \
                         (board[1] != symbol_1 and board[1] != symbol_2):
                        turn1 = 2
                    elif ((board[1] == symbol_2 and board[7] == symbol_2) or (board[1] == symbol_1 and board[7] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 3rd column
                    elif ((board[2] == symbol_2 and board[5] == symbol_2) or (board[2] == symbol_1 and board[5] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[5] == symbol_2 and board[8] == symbol_2) or (board[5] == symbol_1 and board[8] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3                
                    elif ((board[2] == symbol_2 and board[8] == symbol_2) or (board[2] == symbol_1 and board[8] == symbol_1)) and \
                         (board[5] != symbol_1 and board[5] != symbol_2):
                        turn1 = 6
            #Conditions for left to right diagonal
                    elif ((board[0] == symbol_2 and board[4] == symbol_2) or (board[0] == symbol_1 and board[4] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[4] == symbol_2 and board[8] == symbol_2) or (board[4] == symbol_1 and board[8] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[8] == symbol_2) or (board[0] == symbol_1 and board[8] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for right to left diagonal
                    elif ((board[2] == symbol_2 and board[4] == symbol_2) or (board[2] == symbol_1 and board[4] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[4] == symbol_2 and board[6] == symbol_2) or (board[4] == symbol_1 and board[6] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3               
                    elif ((board[2] == symbol_2 and board[6] == symbol_2) or (board[2] == symbol_1 and board[6] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 1st row
                    elif ((board[0] == symbol_2 and board[1] == symbol_2) or (board[0] == symbol_1 and board[1] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3
                    elif ((board[1] == symbol_2 and board[2] == symbol_2) or (board[1] == symbol_1 and board[2] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[2] == symbol_2) or (board[0] == symbol_1 and board[2] == symbol_1)) and \
                         (board[1] != symbol_1 and board[1] != symbol_2):
                        turn1 = 2
            #Conditions for 2nd row
                    elif ((board[3] == symbol_2 and board[4] == symbol_2) or (board[3] == symbol_1 and board[4] == symbol_1)) and \
                         (board[5] != symbol_1 and board[5] != symbol_2):
                        turn1 = 6
                    elif ((board[4] == symbol_2 and board[5] == symbol_2) or (board[4] == symbol_1 and board[5] == symbol_1)) and \
                         (board[3] != symbol_1 and board[3] != symbol_2):
                        turn1 = 4
                    elif ((board[3] == symbol_2 and board[5] == symbol_2) or (board[3] == symbol_1 and board[5] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 3rd row
                    elif ((board[6] == symbol_2 and board[7] == symbol_2) or (board[6] == symbol_1 and board[7] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[7] == symbol_2 and board[8] == symbol_2) or (board[7] == symbol_1 and board[8] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[6] == symbol_2 and board[8] == symbol_2) or (board[6] == symbol_1 and board[8] == symbol_1)) and \
                         (board[7] != symbol_1 and board[7] != symbol_2):
                        turn1 = 8
                    else:
                        #If above conditions are not fulfilled 
                        if (board[1] != symbol_1 and board[1] != symbol_2):
                            turn1 = 2
                        elif (board[3] != symbol_1 and board[3] != symbol_2):
                            turn1 = 4
                        elif (board[5] != symbol_1 and board[5] != symbol_2):
                            turn1 = 6
                        elif (board[7] != symbol_1 and board[7] != symbol_2):
                            turn1 = 8
                        elif (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 5
                        elif (board[0] != symbol_1 and board[0] != symbol_2):
                            turn1 = 1
                        elif (board[2] != symbol_1 and board[2] != symbol_2):
                            turn1 = 3
                        elif (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 7
                        elif (board[8] != symbol_1 and board[8] != symbol_2):
                            turn1 = 9
                else:
                    turn1 = eval(input(player1 +" turn: "))
                    
            #Conditions for putting symbols 
                diff = putsymbol_1(turn,turn1,board,symbol_1,symbol_2)
                if diff == 5:
                    turn -= 1
                    print("\nBox is already occupied.\nPlease enter another box\n")
                    grid(board,symbol_1,symbol_2)
                elif diff == 6:
                    turn -= 1
                    print("\nEntered number is invalid.\nEnter a valid number\n")
                    grid(board,symbol_1,symbol_2)
                    
            #Winning and draw conditions
                check = windrawcondi(board,turn,symbol_1,symbol_2)
                if check == 1:
                    print(player1, "wins this match")
                    p1 += 1
                    break
                elif check == 2:
                    print(player2, "wins this match")
                    p2 += 1
                    break
                elif check == 3:
                    print("Match Drawn!")
                    break
                #changing turn
                turn +=1

                
#If system wins the toss
        if Toss == 1:
        #Loop for moves of game untill someone wins or game is drawn
            turn = 1
            while turn <= 10:
        #Using number of moves for changing the turn
                if turn%2 == 0:
                    turn1 = eval(input(player1 +" turn: "))
                else:
                    print("System Turn")
            #Conditions for 1st column
                    if ((board[0] == symbol_2 and board[3] == symbol_2) or (board[0] == symbol_1 and board[3] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[3] == symbol_2 and board[6] == symbol_2) or (board[3] == symbol_1 and board[6] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):                     
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[6] == symbol_2) or (board[0] == symbol_1 and board[6] == symbol_1)) and \
                         (board[3] != symbol_1 and board[3] != symbol_2):
                        turn1 = 4
           #Conditions for 2nd column
                    elif ((board[1] == symbol_2 and board[4] == symbol_2) or (board[1] == symbol_1 and board[4] == symbol_1)) and \
                        (board[7] != symbol_1 and board[7] != symbol_2):
                        turn1 = 8
                    elif ((board[4] == symbol_2 and board[7] == symbol_2) or (board[4] == symbol_1 and board[7] == symbol_1)) and \
                         (board[1] != symbol_1 and board[1] != symbol_2):
                        turn1 = 2
                    elif ((board[1] == symbol_2 and board[7] == symbol_2) or (board[1] == symbol_1 and board[7] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 3rd column
                    elif ((board[2] == symbol_2 and board[5] == symbol_2) or (board[2] == symbol_1 and board[5] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[5] == symbol_2 and board[8] == symbol_2) or (board[5] == symbol_1 and board[8] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3                
                    elif ((board[2] == symbol_2 and board[8] == symbol_2) or (board[2] == symbol_1 and board[8] == symbol_1)) and \
                         (board[5] != symbol_1 and board[5] != symbol_2):
                        turn1 = 6
            #Conditions for left to right diagonal
                    elif ((board[0] == symbol_2 and board[4] == symbol_2) or (board[0] == symbol_1 and board[4] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[4] == symbol_2 and board[8] == symbol_2) or (board[4] == symbol_1 and board[8] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[8] == symbol_2) or (board[0] == symbol_1 and board[8] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for right to left diagonal
                    elif ((board[2] == symbol_2 and board[4] == symbol_2) or (board[2] == symbol_1 and board[4] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[4] == symbol_2 and board[6] == symbol_2) or (board[4] == symbol_1 and board[6] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3               
                    elif ((board[2] == symbol_2 and board[6] == symbol_2) or (board[2] == symbol_1 and board[6] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 1st row
                    elif ((board[0] == symbol_2 and board[1] == symbol_2) or (board[0] == symbol_1 and board[1] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3
                    elif ((board[1] == symbol_2 and board[2] == symbol_2) or (board[1] == symbol_1 and board[2] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[2] == symbol_2) or (board[0] == symbol_1 and board[2] == symbol_1)) and \
                         (board[1] != symbol_1 and board[1] != symbol_2):
                        turn1 = 2
            #Conditions for 2nd row
                    elif ((board[3] == symbol_2 and board[4] == symbol_2) or (board[3] == symbol_1 and board[4] == symbol_1)) and \
                         (board[5] != symbol_1 and board[5] != symbol_2):
                        turn1 = 6
                    elif ((board[4] == symbol_2 and board[5] == symbol_2) or (board[4] == symbol_1 and board[5] == symbol_1)) and \
                         (board[3] != symbol_1 and board[3] != symbol_2):
                        turn1 = 4
                    elif ((board[3] == symbol_2 and board[5] == symbol_2) or (board[3] == symbol_1 and board[5] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 3rd row
                    elif ((board[6] == symbol_2 and board[7] == symbol_2) or (board[6] == symbol_1 and board[7] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[7] == symbol_2 and board[8] == symbol_2) or (board[7] == symbol_1 and board[8] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[6] == symbol_2 and board[8] == symbol_2) or (board[6] == symbol_1 and board[8] == symbol_1)) and \
                         (board[7] != symbol_1 and board[7] != symbol_2):
                        turn1 = 8
                    else:
                        #Conditions for 1st turn of system      
                        if (board[1] != symbol_1 and board[1] != symbol_2):
                            turn1 = 2
                        elif (board[3] != symbol_1 and board[3] != symbol_2):
                            turn1 = 4
                        elif (board[5] != symbol_1 and board[5] != symbol_2):
                            turn1 = 6
                        elif (board[7] != symbol_1 and board[7] != symbol_2):
                            turn1 = 8
                        elif (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 5
                        elif (board[0] != symbol_1 and board[0] != symbol_2):
                            turn1 = 1
                        elif (board[2] != symbol_1 and board[2] != symbol_2):
                            turn1 = 3
                        elif (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 7
                        elif (board[8] != symbol_1 and board[8] != symbol_2):
                            turn1 = 9
                            
            #Conditions for putting symbols
                diff = putsymbol_2(turn,turn1,board,symbol_1,symbol_2)
                if diff == 5:
                    turn -= 1
                    print("\nBox is already occupied.\nPlease enter another box\n")
                    grid(board,symbol_1,symbol_2)
                elif diff == 6:
                    print("\nEntered number is invalid.\nEnter a valid number\n")
                    turn -= 1
                    grid(board,symbol_1,symbol_2)
                    
            #Winning and draw conditions
                check = windrawcondi(board,turn,symbol_1,symbol_2)
                if check == 1:
                    print(player1, "wins this match")
                    p1 += 1
                    break
                elif check == 2:
                    print(player2, "wins this match")
                    p2 += 1
                    break
                elif check == 3:
                    print("Match Drawn!")
                    break
                #changing turn
                turn += 1
                
        #Displaying Scoreboard
        scoreboard(p1,p2,player1,player2)
        #Displaying menu at the end of game
        menu = str(input("\nEnter Y to continue game or\
\n\tEnter M to go to main menu or\n\t\tEnter E to exit the game: "))
        if menu == 'M' or menu == 'm':
            main()


            
#Function for Single player hard mode game 
def singleHardgame():
    #variable for counting wins
    p1 = 0
    p2 = 0
    #players info
    player1 = str(input("\nPlayer name: "))
    symbol_1 = 'O'
    player2 = 'System'
    symbol_2 = 'X'
    #loop for repition of game
    menu = 'Y'
    while menu == 'Y' or menu == 'y':
        #list for Grid
        board = [1,2,3,4,5,6,7,8,9]
        grid(board,symbol_1,symbol_2)
        #Toss
        Toss = random.randint(0,1)
        toss(Toss,player1,player2,symbol_1,symbol_2)
        
#If player wins the toss
        if Toss == 0:
            #Loop for moves of game untill someone wins or game is drawn
            turn = 1
            while turn <= 10:
                #Using number of moves for changing the turn
                if turn%2 == 0:
                    print("System turn")
            #Condition if player occupy any side of the grid 
                    if (board[1] == symbol_1 or board[3] == symbol_1 or board[5] == symbol_1 or board[7] == symbol_1) and \
                       (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Condition if player occupy any corner of the grid
                    elif (board[0] == symbol_1 or board[2] == symbol_1 or board[6] == symbol_1 or board[8] == symbol_1) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 1st column in grid
                    elif ((board[0] == symbol_2 and board[3] == symbol_2) or (board[0] == symbol_1 and board[3] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1  = 7
                    elif ((board[3] == symbol_2 and board[6] == symbol_2) or (board[3] == symbol_1 and board[6] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):                     
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[6] == symbol_2) or (board[0] == symbol_1 and board[6] == symbol_1)) and \
                         (board[3] != symbol_1 and board[3] != symbol_2):
                        turn1 = 4
            #Conditions for 2nd column
                    elif ((board[1] == symbol_2 and board[4] == symbol_2) or (board[1] == symbol_1 and board[4] == symbol_1)) and \
                         (board[7] != symbol_1 and board[7] != symbol_2):
                        turn1 = 8
                    elif ((board[4] == symbol_2 and board[7] == symbol_2) or (board[4] == symbol_1 and board[7] == symbol_1)) and \
                         (board[1] != symbol_1 and board[1] != symbol_2):
                        turn1 = 2
                    elif ((board[1] == symbol_2 and board[7] == symbol_2) or (board[1] == symbol_1 and board[7] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
             #Conditions for 3rd column
                    elif ((board[2] == symbol_2 and board[5] == symbol_2) or (board[2] == symbol_1 and board[5] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[5] == symbol_2 and board[8] == symbol_2) or (board[5] == symbol_1 and board[8] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3                
                    elif ((board[2] == symbol_2 and board[8] == symbol_2) or (board[2] == symbol_1 and board[8] == symbol_1)) and \
                         (board[5] != symbol_1 and board[5] != symbol_2):
                        turn1 = 6
            #Conditions for left to right diagonal
                    elif ((board[0] == symbol_2 and board[4] == symbol_2) or (board[0] == symbol_1 and board[4] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[4] == symbol_2 and board[8] == symbol_2) or (board[4] == symbol_1 and board[8] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[8] == symbol_2) or (board[0] == symbol_1 and board[8] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for right to left diagonal
                    elif ((board[2] == symbol_2 and board[4] == symbol_2) or (board[2] == symbol_1 and board[4] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[4] == symbol_2 and board[6] == symbol_2) or (board[4] == symbol_1 and board[6] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3               
                    elif ((board[2] == symbol_2 and board[6] == symbol_2) or (board[2] == symbol_1 and board[6] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 1st row
                    elif ((board[0] == symbol_2 and board[1] == symbol_2) or (board[0] == symbol_1 and board[1] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3
                    elif ((board[1] == symbol_2 and board[2] == symbol_2) or (board[1] == symbol_1 and board[2] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[2] == symbol_2) or (board[0] == symbol_1 and board[2] == symbol_1)) and \
                         (board[1] != symbol_1 and board[1] != symbol_2):
                        turn1 = 2
            #Conditions for 2nd row
                    elif ((board[3] == symbol_2 and board[4] == symbol_2) or (board[3] == symbol_1 and board[4] == symbol_1)) and \
                         (board[5] != symbol_1 and board[5] != symbol_2):
                        turn1 = 6
                    elif ((board[4] == symbol_2 and board[5] == symbol_2) or (board[4] == symbol_1 and board[5] == symbol_1)) and \
                         (board[3] != symbol_1 and board[3] != symbol_2):
                        turn1 = 4
                    elif ((board[3] == symbol_2 and board[5] == symbol_2) or (board[3] == symbol_1 and board[5] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 3rd row
                    elif ((board[6] == symbol_2 and board[7] == symbol_2) or (board[6] == symbol_1 and board[7] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[7] == symbol_2 and board[8] == symbol_2) or (board[7] == symbol_1 and board[8] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[6] == symbol_2 and board[8] == symbol_2) or (board[6] == symbol_1 and board[8] == symbol_1)) and \
                         (board[7] != symbol_1 and board[7] != symbol_2):
                        turn1 = 8
                    else:
                #Conditions to ocuppy corners 
                        if (board[1] == symbol_1 and board[3] == symbol_1) and (board[0] != symbol_1 and board[0] != symbol_2):
                            turn1 = 1
                        elif (board[1] == symbol_1 and board[5] == symbol_1) and (board[2] != symbol_1 and board[2] != symbol_2):
                            turn1 = 3
                        elif (board[3] == symbol_1 and board[7] == symbol_1) and (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 7
                        elif (board[5] == symbol_1 and board[7] == symbol_1) and (board[8] != symbol_1 and board[8] != symbol_2):
                            turn1 = 9
                #Conditions if user occupy grid center(5)
                        elif (board[4] == symbol_1) and (board[0] != symbol_1 and board[0] != symbol_2):
                            turn1 = 1
                        elif (board[4] == symbol_1) and (board[2] != symbol_1 and board[2] != symbol_2):
                            turn1 = 3
                        elif (board[4] == symbol_1) and (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 7
                        elif (board[4] == symbol_1) and (board[8] != symbol_1 and board[8] != symbol_2):
                            turn1 = 9
                #If above conditions are not fulfilled 
                        elif (board[1] != symbol_1 and board[1] != symbol_2):
                            turn1 = 2
                        elif (board[3] != symbol_1 and board[3] != symbol_2):
                            turn1 = 4
                        elif (board[5] != symbol_1 and board[5] != symbol_2):
                            turn1 = 6
                        elif (board[7] != symbol_1 and board[7] != symbol_2):
                            turn1 = 8
                        elif (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 5
                        elif (board[0] != symbol_1 and board[0] != symbol_2):
                            turn1 = 1
                        elif (board[2] != symbol_1 and board[2] != symbol_2):
                            turn1 = 3
                        elif (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 7
                        elif (board[8] != symbol_1 and board[8] != symbol_2):
                            turn1 = 9
                else:
                    turn1 = eval(input(player1 +" turn: "))
                    
            #Conditions for putting symbols 
                diff = putsymbol_1(turn,turn1,board,symbol_1,symbol_2)
                if diff == 5:
                    turn -= 1
                    print("\nBox is already occupied.\nPlease enter another box\n")
                    grid(board,symbol_1,symbol_2)
                elif diff == 6:
                    turn -= 1
                    print("\nEntered number is invalid.\nEnter a valid number\n")
                    grid(board,symbol_1,symbol_2)
                        
            #Winning and draw conditions
                check = windrawcondi(board,turn,symbol_1,symbol_2)
                if check == 1:
                    print(player1, "wins this match")
                    p1 += 1
                    break
                elif check == 2:
                    print(player2, "wins this match")
                    p2 += 1
                    break
                elif check == 3:
                    print("Match Drawn!")
                    break
                #Changing turn
                turn +=1

                
#If system wins the toss
        if Toss == 1:
        #Loop for moves of game untill someone wins or game is drawn
            turn = 1
            while turn <= 10:
        #Using number of moves for changing the turn
                if turn%2 == 0:
                    turn1 = eval(input(player1 +" turn: "))
                else:
                    print("System Turn")
            #Condition if player occupy side of the grid
                    if (board[1] == symbol_2 or board[3] == symbol_2 or board[5] == symbol_2 or board[7] == symbol_2) and \
                       (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Condition if player occupy corner of the grid
                    elif (board[0] == symbol_2 or board[2] == symbol_2 or board[6] == symbol_2 or board[8] == symbol_2) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 1st column in grid
                    elif ((board[0] == symbol_2 and board[3] == symbol_2) or (board[0] == symbol_1 and board[3] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[3] == symbol_2 and board[6] == symbol_2) or (board[3] == symbol_1 and board[6] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):                     
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[6] == symbol_2) or (board[0] == symbol_1 and board[6] == symbol_1)) and \
                         (board[3] != symbol_1 and board[3] != symbol_2):
                        turn1 = 4
            #Conditions for 2nd column
                    elif ((board[1] == symbol_2 and board[4] == symbol_2) or (board[1] == symbol_1 and board[4] == symbol_1)) and \
                        (board[7] != symbol_1 and board[7] != symbol_2):
                        turn1 = 8
                    elif ((board[4] == symbol_2 and board[7] == symbol_2) or (board[4] == symbol_1 and board[7] == symbol_1)) and \
                         (board[1] != symbol_1 and board[1] != symbol_2):
                        turn1 = 2
                    elif ((board[1] == symbol_2 and board[7] == symbol_2) or (board[1] == symbol_1 and board[7] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 3rd column
                    elif ((board[2] == symbol_2 and board[5] == symbol_2) or (board[2] == symbol_1 and board[5] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[5] == symbol_2 and board[8] == symbol_2) or (board[5] == symbol_1 and board[8] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3                
                    elif ((board[2] == symbol_2 and board[8] == symbol_2) or (board[2] == symbol_1 and board[8] == symbol_1)) and \
                         (board[5] != symbol_1 and board[5] != symbol_2):
                        turn1 = 6
            #Conditions for left to right diagonal
                    elif ((board[0] == symbol_2 and board[4] == symbol_2) or (board[0] == symbol_1 and board[4] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[4] == symbol_2 and board[8] == symbol_2) or (board[4] == symbol_1 and board[8] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[8] == symbol_2) or (board[0] == symbol_1 and board[8] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for right to left diagonal
                    elif ((board[2] == symbol_2 and board[4] == symbol_2) or (board[2] == symbol_1 and board[4] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[4] == symbol_2 and board[6] == symbol_2) or (board[4] == symbol_1 and board[6] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3               
                    elif ((board[2] == symbol_2 and board[6] == symbol_2) or (board[2] == symbol_1 and board[6] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 1st row
                    elif ((board[0] == symbol_2 and board[1] == symbol_2) or (board[0] == symbol_1 and board[1] == symbol_1)) and \
                         (board[2] != symbol_1 and board[2] != symbol_2):
                        turn1 = 3
                    elif ((board[1] == symbol_2 and board[2] == symbol_2) or (board[1] == symbol_1 and board[2] == symbol_1)) and \
                         (board[0] != symbol_1 and board[0] != symbol_2):
                        turn1 = 1
                    elif ((board[0] == symbol_2 and board[2] == symbol_2) or (board[0] == symbol_1 and board[2] == symbol_1)) and \
                         (board[1] != symbol_1 and board[1] != symbol_2):
                        turn1 = 2
            #Conditions for 2nd row
                    elif ((board[3] == symbol_2 and board[4] == symbol_2) or (board[3] == symbol_1 and board[4] == symbol_1)) and \
                         (board[5] != symbol_1 and board[5] != symbol_2):
                        turn1 = 6
                    elif ((board[4] == symbol_2 and board[5] == symbol_2) or (board[4] == symbol_1 and board[5] == symbol_1)) and \
                         (board[3] != symbol_1 and board[3] != symbol_2):
                        turn1 = 4
                    elif ((board[3] == symbol_2 and board[5] == symbol_2) or (board[3] == symbol_1 and board[5] == symbol_1)) and \
                         (board[4] != symbol_1 and board[4] != symbol_2):
                        turn1 = 5
            #Conditions for 3rd row
                    elif ((board[6] == symbol_2 and board[7] == symbol_2) or (board[6] == symbol_1 and board[7] == symbol_1)) and \
                         (board[8] != symbol_1 and board[8] != symbol_2):
                        turn1 = 9
                    elif ((board[7] == symbol_2 and board[8] == symbol_2) or (board[7] == symbol_1 and board[8] == symbol_1)) and \
                         (board[6] != symbol_1 and board[6] != symbol_2):
                        turn1 = 7
                    elif ((board[6] == symbol_2 and board[8] == symbol_2) or (board[6] == symbol_1 and board[8] == symbol_1)) and \
                         (board[7] != symbol_1 and board[7] != symbol_2):
                        turn1 = 8
                    else:
                #Conditions to ocuppy corners
                        if (board[1] == symbol_2 and board[3] == symbol_2) and (board[0] != symbol_1 and board[0] != symbol_2):
                            turn1 = 1
                        elif (board[1] == symbol_2 and board[5] == symbol_2) and (board[2] != symbol_1 and board[2] != symbol_2):
                            turn1 = 3
                        elif (board[3] == symbol_2 and board[7] == symbol_2) and (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 7
                        elif (board[5] == symbol_2 and board[7] == symbol_2) and (board[8] != symbol_1 and board[8] != symbol_2):
                            turn1 = 9
                #Conditions if user occupy grid center(5)
                        elif (board[4] == symbol_2) and (board[0] != symbol_1 and board[0] != symbol_2):
                            turn1 = 1
                        elif (board[4] == symbol_2) and (board[2] != symbol_1 and board[2] != symbol_2):
                            turn1 = 3
                        elif (board[4] == symbol_2) and (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 7
                        elif (board[4] == symbol_2) and (board[8] != symbol_1 and board[8] != symbol_2):
                            turn1 = 9
                #Conditions for 1st turn of system
                        elif (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 5
                        elif (board[1] != symbol_1 and board[1] != symbol_2):
                            turn1 = 2
                        elif (board[3] != symbol_1 and board[3] != symbol_2):
                            turn1 = 4
                        elif (board[5] != symbol_1 and board[5] != symbol_2):
                            turn1 = 6
                        elif (board[7] != symbol_1 and board[7] != symbol_2):
                            turn1 = 8
                        elif (board[0] != symbol_1 and board[0] != symbol_2):
                            turn1 = 1
                        elif (board[2] != symbol_1 and board[2] != symbol_2):
                            turn1 = 3
                        elif (board[6] != symbol_1 and board[6] != symbol_2):
                            turn1 = 7
                        elif (board[8] != symbol_1 and board[8] != symbol_2):
                            turn1 = 9
                            
            #Conditions for putting symbols
                diff = putsymbol_2(turn,turn1,board,symbol_1,symbol_2)
                if diff == 5:
                    turn -= 1
                    print("\nBox is already occupied.\nPlease enter another box\n")
                    grid(board,symbol_1,symbol_2)
                elif diff == 6:
                    print("\nEntered number is invalid.\nEnter a valid number\n")
                    turn -= 1
                    grid(board,symbol_1,symbol_2)
                    
            #Winning and draw conditions
                check = windrawcondi(board,turn,symbol_1,symbol_2)
                if check == 1:
                    print(player1, "wins this match")
                    p1 += 1
                    break
                elif check == 2:
                    print(player2, "wins this match")
                    p2 += 1
                    break
                elif check == 3:
                    print("Match Drawn!")
                    break
                #Changing turn
                turn += 1
                
        #Displaying Scoreboard
        scoreboard(p1,p2,player1,player2)
        #Displaying menu at the end of game
        menu = str(input("\nEnter Y to continue game or\
\n\tEnter M to go to main menu or\n\t\tEnter E to exit the game: "))
        if menu == 'M' or menu == 'm':
            main()



#Function for two players game
def twoPlayers():
    #variable for counting wins
    p1 = 0
    p2 = 0
    #players info
    player1 = str(input("\nPlayer 1 name: "))
    symbol_1 = 'O'
    player2 = str(input("Player 2 name: "))
    symbol_2 = 'X'
    #loop for repition of game
    menu = 'Y'
    while menu == 'Y' or menu == 'y':
    #list for Grid
        board = [1,2,3,4,5,6,7,8,9]
        grid(board,symbol_1,symbol_2)
    #Toss
        Toss = random.randint(0,1)
        if Toss == 0:
            print(player1, "won the toss\n")
        else:
            print(player2, "won the toss\n")
            
            #Swaping player names and symbols if player_2 wins the toss
            symbol_1, symbol_2 = symbol_2, symbol_1
            player1, player2 = player2, player1
            
        print(player1, "your symbol is", symbol_1)
        print(player2, "your symbol is", symbol_2,"\n")
        
        #Loop for moves of game untill someone wins or game is drawn
        turn = 1
        while turn <= 10:
        #Using number of moves for changing the turn
            if turn%2 == 0:
                turn1 = eval(input(player2 +" turn: "))
            else:
                turn1 = eval(input(player1 +" turn: "))
                
        #Conditions for putting symbols
            diff = putsymbol_1(turn,turn1,board,symbol_1,symbol_2)
            if diff == 5:
                turn -= 1
                print("\nBox is already occupied.\nPlease enter another box\n")
                grid(board,symbol_1,symbol_2)
            elif diff == 6:
                print("\nEntered number is invalid.\nEnter a valid number\n")
                turn -= 1
                grid(board,symbol_1,symbol_2)
                
        #Winning and draw conditions
            check = windrawcondi(board,turn,symbol_1,symbol_2)
            if check == 1:
                print(player1, "wins this match")
                p1 += 1
                break
            elif check == 2:
                print(player2, "wins this match")
                p2 += 1
                break
            elif check == 3:
                print("Match Drawn!")
                break
            #changing turn
            turn += 1
            
        #Displaying Scoreboard
        scoreboard(p1,p2,player1,player2)
    #Displaying menu at the end of game
        menu = str(input("\nEnter Y to continue game or\
\n\tEnter M to go to main menu or\n\t\tEnter E to exit game: "))
        if menu == 'M' or menu == 'm':
            main()
            


#Function for tournament of two players
def tournament():
    #variable for counting wins
    p1 = 0
    p2 = 0
    #players info
    player1 = str(input("\nPlayer 1 name: "))
    symbol_1 = 'O'
    player2 = str(input("Player 2 name: "))
    symbol_2 = 'X'
    #loop for repition of game
    menu = 'Y'
    while menu == 'Y' or menu == 'y':
        #Asking player for number of games in a tournament
        num = eval(input("\nEnter the number of games you want to play in a Tournament: "))
        #loop for tournament
        for i in range(num):            
        #list for Grid
            board = [1,2,3,4,5,6,7,8,9]
            grid(board,symbol_1,symbol_2)
        #Toss
            Toss = random.randint(0,1)
            toss(Toss,player1,player2,symbol_1,symbol_2)
            
#if 1st player wins the toss
            if Toss == 0:
            #Loop for moves of game untill someone wins or game is drawn
                turn = 1
                while turn <= 10:  
                #Using number of moves for changing the turn
                    if turn%2 == 0:
                        turn1 = eval(input(player2 +" turn: "))
                    else:
                        turn1 = eval(input(player1 +" turn: "))
                        
                #Conditions for putting symbols
                    diff = putsymbol_1(turn,turn1,board,symbol_1,symbol_2)
                    if diff == 5:
                        turn -= 1
                        print("\nBox is already occupied.\nPlease enter another box\n")
                        grid(board,symbol_1,symbol_2)
                    elif diff == 6:
                        print("\nEntered number is invalid.\nEnter a valid number\n")
                        turn -= 1
                        grid(board,symbol_1,symbol_2)
                        
                #Winning and draw conditions
                    check = windrawcondi(board,turn,symbol_1,symbol_2)
                    if check == 1:
                        print(player1, "wins this match")
                        p1 += 1
                        break
                    elif check == 2:
                        print(player2, "wins this match")
                        p2 += 1
                        break
                    elif check == 3:
                        print("Match Drawn!")
                        break
                    #changing turn
                    turn += 1
                    
#When 2nd player wins the toss
            if Toss == 1:
             #Loop for moves of game untill someone wins or game is drawn
                turn = 1
                while turn <= 10:  
                #Using number of moves for changing the turn
                    if turn%2 == 0:
                        turn1 = eval(input(player1 +" turn: "))
                    else:
                        turn1 = eval(input(player2 +" turn: "))
                        
                #Conditions for putting symbols
                    diff = putsymbol_2(turn,turn1,board,symbol_1,symbol_2)
                    if diff == 5:
                        turn -= 1
                        print("\nBox is already occupied.\nPlease enter another box\n")
                        grid(board,symbol_1,symbol_2)
                    elif diff == 6:
                        print("\nEntered number is invalid.\nEnter a valid number\n")
                        turn -= 1
                        grid(board,symbol_1,symbol_2)
                        
                #Winning and draw conditions
                    check = windrawcondi(board,turn,symbol_1,symbol_2)
                    if check == 1:
                        print(player1, "wins this match")
                        p1 += 1
                        break
                    elif check == 2:
                        print(player2, "wins this match")
                        p2 += 1
                        break
                    elif check == 3:
                        print("Match Drawn!")
                        break
                    turn += 1
            #Scoreboard for tournament
            scoreboard(p1,p2,player1,player2)
            
        #Conditions to check who wins the tournament
        if p1 > p2:
            print("\n\n\t\t", player1, "wins the tournament\n\n")
            p1 = 0
            p2 = 0
        elif p2 > p1:
            print("\n\n\t\t", player2, "wins the tournament\n\n")
            p1 = 0
            p2 = 0
        else:
            print("\n\n\t\tTournament Drawn\n\n")
            p1 = 0
            p2 = 0
        #Displaying menu at the end of game
        menu = str(input("\nEnter Y to continue game or\
\n\tEnter M to go to main menu or\n\t\tEnter E to exit game: "))
        if menu == 'M' or menu == 'm':
            main()
main()
