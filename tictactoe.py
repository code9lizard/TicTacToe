import random
from ascii import ascii
class Game:
    def __init__(self):
        self.grid = [[" "] * 3 for i in range(3)]

    def display(self):
        for row in self.grid:
            print("-" * 13)
            print("|", end="")
            for col in row:
                print(f" {col} |", end="")
            print()
        print("-" * 13)

    def insert(self, letter: str, row: int, col: int):
        if self.grid[row - 1][col - 1] != " ":
            return False
        else:
            self.grid[row - 1][col - 1] = letter
            return True

    def check_win(self):
        # check row
        for i in range(3):
            if " " != self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                return True

        for i in range(3):
            if " " != self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                return True

        if " " != self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return True

        if " " != self.grid[2][0] == self.grid[1][1] == self.grid[0][2]:
            return True

        return False

    def check_full(self):
        for row in self.grid:
            for col in row:
                if col == " ":
                    return False
        print("It is a tie!")
        return True


class Interface:
    def __init__(self):
        print(ascii)
    def validate_move(self, letter: str):
        done = False
        while not done:
            move = input("Enter your move (Row column): ")
            move = move.split(" ")
            try:
                if game.insert(letter, int(move[0]), int(move[1])):
                    print(f"Player {letter} inserted into ({move[0]}, {move[1]})")
                    return True
                print("Sorry, it is occupied!")
            except IndexError:
                print("Enter a valid move in the format (Row column)")

    def start(self):
        print("Welcome to my Tic-Tac-Toe Game!")
        is_computer = input("Do you want to play against a computer? (y/n): ")
        game.display()

        if is_computer == "y":
            while not game.check_full():
                print("It is your turn")
                self.validate_move("O")
                game.display()
                if game.check_win():
                    print("You wins!")
                    break

                if game.check_full():
                    break

                while not game.insert("X", random.randint(1, 3), random.randint(1, 3)):
                    pass
                game.display()
                if game.check_win():
                    print("Computer wins!")
                    break

        else:
            while not game.check_full():
                print("It is Player O turn.")
                self.validate_move("O")
                game.display()
                if game.check_win():
                    print("Player O wins!")
                    break

                print("It is Player X turn.")
                self.validate_move("X")
                game.display()
                if game.check_win():
                    print("Player X wins!")
                    break


game = Game()
interface = Interface()
interface.start()