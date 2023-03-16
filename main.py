from os import system
import random

# used for creating the horizontal lines on the board
def underline(string):
    return '\033[4m' + string + '\033[0m'
ul = underline

def check_choice(choice_str, check1, check2):
    while True:
        choice = input(choice_str)
        if choice in [check1, check2]:
            break
        print("Please choose one of the options")
    return choice

def win_determination(board, symbol):
    win_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    simple_board = [0 if spot == ul(" ") else 1 for spot in board]

    # creates simple board with x'es and o's
    board_with_symbols = []
    for i in range(len(simple_board)):
        if simple_board[i] == 1:
            board_with_symbols.append("x" if "4mx" in board[i] else "o")
        else:
            board_with_symbols.append("-")

    # creates list with possible win combinations from win_indexes
    possible_wins = []
    for combo in win_indexes:
        count = 0
        for index in combo:
            if simple_board[index] == 1:
                count += 1
        if count == 3:
            possible_wins.append(combo)
    
    # returns false if there are no possible win combinations
    if len(possible_wins) == 0:
        return False

    # for every possible win combination, checks if they are all the current players symbol (x or o)
    for possible_win in possible_wins:
        count = 0
        for index in possible_win:
            if board_with_symbols[index] == symbol:
                count += 1
        if count == 3:
            return True
    
    return False

class Board:
    # convert the move input to the corresponding index
    moves = {"a/1": 0, "b/1": 1, "c/1": 2, "a/2": 3, "b/2": 4, "c/2": 5, "a/3": 6, "b/3": 7, "c/3": 8}

    def __init__(self):
        self.board = [ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" ")]
    
    def __repr__(self):
        return "  a b c\n1 {one}\n2 {two}\n3 {three}".format(one = "|".join(self.board[:3]), two = "|".join(self.board[3:6]), three = "|".join(self.board[6:]))
    
    def clear_board(self):
        self.board = [ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" ")]
    
class Player:
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name
        self.points = 0

    def make_move(self, board):
        # prints (name) to move if in 2 player mode
        if mode == "1":
            print(f"{self.name} to move")
        while True:
            choice = input("select a combination (a-c/1-3): ")
            # checks if move is valid
            if choice in Board.moves:
                # checks if move isn't on a filled spot
                if board.board[Board.moves[choice]] == ul(" "):
                    board.board[Board.moves[choice]] = ul(self.symbol)
                    # checks if this move has made you win, returns true if so
                    return win_determination(board.board, self.symbol)
                else:
                    print("please choose an empty colon")
            else:
                print("please use the correct format")
    
    def win(self, player2):
        self.points += 1
        print(f'{self.name} has won the game! {self.name} now has {self.points} {"point" if self.points == 1 else "points"} and {player2.name} has {player2.points} points.')

def computer_play(board, symbol):
    # selects index to place a symbol on the board and makes sure it's empty
    while True:
        play_index = random.randint(0, 8)
        if board[play_index] == ul(" "):
            break
    
    # places symbol on the board
    board[play_index] = ul(symbol)
    # returns True or False depending if it was a winning move
    return win_determination(board, comp_symbol)

def main_2p(board, first_move, second_move):
    while True:
        system("cls") # clears output
        print(board)
        # runs make_move and checks if the function returned True at the same time (would mean that player won)
        if first_move.make_move(board):
            winner = player1
            loser = player2
            break
        system("cls")
        print(board)
        if second_move.make_move(board):
            winner = player2
            loser = player1
            break
    
    system("cls")
    print(board)
    winner.win(player2)
    choice = input("Press enter to play again, anything else + enter to quit: ")
    if choice == "":
        board.clear_board()
        main_2p(board, winner, loser)

def main_comp(board, player1):
    while True:
        system("cls") # clears output
        print(board)
        # runs make_move and checks if the function returned True at the same time (would mean that player won)
        if player1.make_move(board):
            system("cls")
            print(board)
            print("You won!")
            break
        system("cls")
        print(board)
        # does a computer move, while checking if it was a winning move
        if computer_play(board.board, comp_symbol):
            system("cls")
            print(board)
            print("You lost..")
            break
    
    choice = input("Press enter to play again, anything else + enter to quit: ")
    if choice == "":
        board.clear_board()
        main_comp(board, player1)

mode = check_choice("1: 2 players\n2: Play against computer\n", "1", "2")

board1 = Board()
if mode == "2":
    player1 = Player(None, check_choice("Choose 'x' or 'o': ", "x", "o"))
    # sets the computer's symbol to the opposite of the player's
    comp_symbol = ul("x") if player1.symbol == "o" else ul("o")

    main_comp(board1, player1)
elif mode == "1":  
    player1 = Player(input("player 1 name: "), "x")
    # check to make sure it's not the same name as player1
    while True:
        player2 = Player(input("player 2 name: "), "o")
        if player2.name != player1.name:
            break
        print("can't use the same name")
    
    main_2p(board1, player1, player2)