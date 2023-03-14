from os import system

# used for creating the horizontal lines on the board
def underline(string):
    return '\033[4m' + string + '\033[0m'
ul = underline

def win_determination(board, symbol):
    win_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    simple_board = [0 if spot == ul(" ") else 1 for spot in board.board]

    # creates simple board with x'es and o's
    board_with_symbols = []
    for i in range(len(simple_board)):
        if simple_board[i] == 1:
            board_with_symbols.append("x" if "4mx" in board.board[i] else "o")
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
        else:
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

    def make_move(self, board):
        print(f"{self.name} to move")
        while True:
            choice = input("select a combination (a-c/1-3): ")
            # checks if move is valid
            if choice in Board.moves:
                # checks if move isn't on a filled spot
                if board.board[Board.moves[choice]] == ul(" "):
                    board.board[Board.moves[choice]] = ul(self.symbol)
                    # checks if this move has made you win, returns true if so
                    if win_determination(board, self.symbol):
                        return True
                    else:
                        return False
                else:
                    print("please choose an empty colon")
            else:
                print("please use the correct format")
    
    def win(self):
        print(f"{self.name} has won the game!")

def main(board, player1, player2):
    while True:
        system("cls") # clears output
        print(board)
        # runs make_move and checks if the function returned True at the same time (would mean that player won)
        if player1.make_move(board):
            winner = player1
            break
        system("cls")
        print(board)
        if player2.make_move(board):
            winner = player2
            break
    
    system("cls")
    print(board)
    winner.win()
    choice = input("Press enter to play again, anything else + enter to quit: ")
    if choice == "":
        board.clear_board()
        main(board, player1, player2)

board1 = Board()
player1 = Player(input("player 1 name: "), "x")
# check to make sure it's not the same name as player1
while True:
    player2 = Player(input("player 2 name: "), "o")
    if player2.name != player1.name:
        break
    print("can't use the same name")

# runs the game
main(board1, player1, player2)
