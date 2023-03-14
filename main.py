class Format:
    end = '\033[0m'
    underline = '\033[4m'

def underline(string):
    return Format.underline + string + Format.end
ul = underline

def win_determination(board):
    pass

class Board:
    moves = {"a/1": 0, "b/1": 1, "c/1": 2, "a/2": 3, "b/2": 4, "c/2": 5, "a/3": 6, "b/3": 7, "c/3": 8}

    def __init__(self):
        self.board = [ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" "), ul(" ")]
    
    def __repr__(self):
        return "  a b c\n1 {one}\n2 {two}\n3 {three}".format(one = "|".join(self.board[:3]), two = "|".join(self.board[3:6]), three = "|".join(self.board[6:]))
    
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        while True:
            choice = input("select a combination (a-c/1-3): ")
            if choice in Board.moves:
                if board.board[Board.moves[choice]] == ul(" "):
                    board.board[Board.moves[choice]] = ul(self.symbol)
                    print(board)
                    break
                else:
                    print("please choose an empty colon")
            else:
                print("please use the correct format")


board1 = Board()
player1 = Player("x")
print(board1)
player1.make_move(board1)
