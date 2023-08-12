#!/usr/bin/env python
# coding: utf-8

# In[30]:


def player_input():
    marker=''
    while marker!="X" and marker !='O':
        marker=input('player1, choose X or O:')
    player1=marker
    if player1=="X":
        player2="O"
    else:
        player2="X"
    return(player1,player2)


# In[31]:


(player1,player2)=player_input()


# In[32]:


def place_marker(board,marker,position):
    board[position]=marker


# In[33]:


test_board


# In[34]:


place_marker(test_board,'$',2)


# In[35]:


def win_check(board,mark):
    #WIN TIC TAC TOE
    #ALL ROWS 
    return ((board[7]==board[8]==board[9]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[1]==board[2]==board[3]==mark) or
    (board[1]==board[4]==board[7]==mark) or
    (board[2]==board[5]==board[8]==mark) or
    (board[3]==board[6]==board[9]==mark) or
    (board[7]==board[5]==board[3]==mark) or
    (board[1]==board[5]==board[9]==mark))
    #ALL COLUMNS
    #ALL DIAGONALS


# In[36]:


win_check(test_board,'X')


# In[37]:


display_board(test_board)


# In[38]:


import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return "PLayer 1"
    else:
        return "Player 2"


# In[39]:


def space_check(board,position): 
    return board[position]==" "


# In[40]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #BOARD IS FULL IF WE RETURN TRUE
    return True
        


# In[41]:


def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose a position:(1-9)"))
    return position


# In[42]:


def replay():
    choice=input("Play again? Enter Yes or No")
    return choice=='Yes'

    


# In[43]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:




