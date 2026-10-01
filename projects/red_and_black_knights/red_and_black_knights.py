import math

class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
        self.knights = {}

    def __repr__(self):
        return f"size = {self.size} | board = {self.board} | knights = {self.knights}"

    def board_creation(self):
        max_number = self.size**2
        for i in range(max_number):
            self.board.append(i)

    def m(self, k): # Helper function
        return (2*k+1)**2-1

    def number_to_cords(self, n):
        if (n == 1):
            x = 0
            y = 1
            cords = (x,y)
            return cords
        k = math.ceil((math.sqrt(n) - 1) / 2)
        m = self.m(k)
        d = m - n

        if (0 <= d <= 2*k or 0 > d): #From 0 towrads 7 - Case 1
            x = -k
            y = k - d
        elif (2*k < d <= 4*k): # From 0 torwards 5 - Case 2
            x = -k + (d - 2*k)
            y = -k
        elif (4*k < d <= 6*k): # From 0 torwards 3 - Case 3
            x = k
            y = -k + (d - 4*k)
        elif (6*k < d <= 8*k): # From 0 towards 1 - Case 4
            x = k - (d - 6*k)
            y = k
        else:
            x = None
            y = None

        cords = (x, y)

        return cords

    def cords_to_number(self, cords):
        if (cords):
            x, y = cords
        else:
            print("Rember value")
            return

        if (x < 0 and abs(x) >= abs(y)): #From 0 towrads 7 - Case 1
            k = abs(x)
            n = -k + self.m(k) + y
        elif (y < 0 and abs(y) >= abs(x)): # From 0 torwards 5 - Case 2
            k = abs(y)
            n = -k + self.m(k) - 2*k -x
        elif (abs(x) >= abs(y)): # From 0 torwards 3 - Case 3
            k = abs(x)
            n = -5*k + self.m(k) -y
        else: # (abs(y) > abs(x)): # From 0 towards 1 - Case 4
            k = abs(y)
            n = self.m(k) - 7*k + x

        return n

    def can_place_knight(self, square, color):
        if square in self.knights:
            return False

        position = self.number_to_cords(square)

        moves = [
            (position[0] + dx, position[1] + dy)
            for dx, dy in (
                (2, 1), (2, -1),
                (-2, 1), (-2, -1),
                (1, 2), (1, -2),
                (-1, 2), (-1, -2)
            )
        ]

        for move in moves:
            number = self.cords_to_number(move)

            if number in self.knights:
                knight = self.knights[number]

                if knight.color != color:
                    return False

        return True

    def add_knight(self, square, color):
        if self.can_place_knight(square, color):
            self.knights[square] = Knight(color, square)
            return True

        return False

    def print_knight(self):
        for square, knight in self.knights.items():
            print(f"Square {square:4} | {knight.color}")

class Knight:
    def __init__(self, color, postion):
        self.color = color
        self.postion = postion

    def __repr__(self):
        return f"{self.color} knight at square {self.postion}"

class Game:
    def __init__(self, number_of_knights, board):
        self.board = board
        self.number_of_knights = number_of_knights
        self.turn = 0
        self.knight_colors = []
        self.knights_next_move = {}

        self.init_number_of_knights()
        self.init_next_moves()

    def __repr__(self):
        return f"number of knights = {self.number_of_knights} | turn = {self.turn} | colors = {self.knight_colors} | next moves = {self.knights_next_move}"

    def init_next_moves(self):
        for color in self.knight_colors:
            self.knights_next_move[color] = 0

    def init_number_of_knights(self):
        for i in range(self.number_of_knights):
            if i == 0:
                self.knight_colors.append("red")
            elif i == 1:
                self.knight_colors.append("black")
            elif i == 2:
                self.knight_colors.append("green")
            elif i == 3:
                self.knight_colors.append("blue")
            else:
                print("That is a lot of knights, I am gonna stop you here")
                self.knight_colors.append("pink")
                return

    def next_turn(self):
        self.turn += 1

        if self.turn >= len(self.knight_colors):
            self.turn = 0

    def try_place_knight(self):
        color = self.knight_colors[self.turn]
        square = self.knights_next_move[color]

        while square < len(self.board.board):

            if self.board.add_knight(square, color):
                self.knights_next_move[color] = square + 1
                self.next_turn()
                return True

            square += 1

        return False

"""
#This tjeks if the number to cordinates works in both ways
def tjekker():
    list_of_mistakes = []
    for i in range (len(board.board)):
        cords = board.number_to_cords(i)
        tjek = board.cords_to_number(cords)
        if tjek[0] != i:
            print(f"number={i} cords={cords} got={tjek}")
            list_of_mistakes.append(i)
    print(list_of_mistakes)
"""

if __name__ == "__main___":
    board = Board(89) #Any odd number and it would give you the amount from 0 to the number^2 - 1
    board.board_creation()

    game = Game(2, board)
    while game.try_place_knight():
     pass

    print(board)
    print(game)

    board.print_knight()