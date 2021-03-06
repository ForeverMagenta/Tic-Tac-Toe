
#test comment
import random

class Tictac:
    def __init__(self, name):
        self.name = "name" #not done finish initializing

    def drawBoard(board):
            # This function prints out the board that it was passed


            # "board" is a list of 10 strings representing the board (ignore index 0)
            print('   |   |')
            print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
            print('   |   |')


    def whoGoesFirst(): #not sure how to randomly select user when both are players not computers, let me know if you know how
        if random.randint(0, 1) == 0:
            return 'X'
        else:
            return 'O'


    def inputPlayerLetter(): #do we need this, how would it be fixed for 2 players?
            # Returns a list with the player's letter as the first item, and the computer's letter as the second.
            # the first element in the tuple is the player's letter, the second is the computer's letter.
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']



    def playAgain(): #we can remove this or both players would have to say yes, this might get complicated
            # This function returns True if the player wants to play again, otherwise it returns False.
            print('Do you want to play again? (yes or no)')
            return input().lower().startswith('y')


    def makeMove(board, letter, move):
            board[move] = letter


    def isWinner(bo, le):
            # Given a board and a player's letter, this function returns True if that player has won.
            # We use bo instead of board and le instead of letter so we don't have to type as much.
            return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


    def getBoardCopy(board):
            # Make a duplicate of the board list and return it the duplicate
            dupeBoard = []


            for i in board:
                dupeBoard.append(i)


            return dupeBoard


    def isSpaceFree(board, move):
            # Return true if the passed move is free on the passed board.
            return board[move] == ' '


    def isBoardFull(board):
            # Return True if every space on the board has been taken. Otherwise return False.
            for i in range(1, 10):
                if isSpaceFree(board, i):
                    return False
            return True


    print('Welcome to Tic Tac Toe!')


    while True:
            # Reset the board
            theBoard = [' '] * 10
            playerLetter, computerLetter = inputPlayerLetter()
            turn = whoGoesFirst()
            print(turn + ' will go first.')
            gameIsPlaying = True


            while gameIsPlaying:
                if turn == 'player':
                    # Player's turn.
                    drawBoard(theBoard)
                    move = getPlayerMove(theBoard)
                    makeMove(theBoard, playerLetter, move)


                    if isWinner(theBoard, playerLetter):
                        drawBoard(theBoard)
                        print('Hooray! You have won the game!')
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'other user' #switch to their username


                else:
                    if isWinner(theBoard, computerLetter):
                        drawBoard(theBoard)
                        print('other player has beaten you! You lose.') #other player name
                        gameIsPlaying = False
                    else:
                        if isBoardFull(theBoard):
                            drawBoard(theBoard)
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player'


            if not playAgain():
                break
