import os

class Board():
    """Represents the game-board"""
    def __init__(self):
        self.board = [i for i in range(10)]
        self._win_combinations = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 5, 9),
            (3, 5, 7),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9)]
        self.game_over = False

    def draw_board(self):
        """Draws the board to the terminal"""
        print("=========")
        print(self.board[7], "|", self.board[8], "|", self.board[9])
        print(self.board[4], "|", self.board[5], "|", self.board[6])
        print(self.board[1], "|", self.board[2], "|", self.board[3])
        print("=========")

    def check_if_won(self, player):
        """Checks if the move the player just made, made him/her win the game"""
        for a, b, c in self._win_combinations:
            if self.board[a] == self.board[b] == self.board[c]:
                print(f"Game over, player {player} won the game")
                self.game_over = True

    def update(self, input, choice):
        """Update the current board"""
        self.board[input] = choice
        os.system("clear")
        self.draw_board()
        self.check_if_won(choice)

    def reset_board(self):
        """Resets the board"""
        self.board = [i for i in range(10)]

    def tie(self):
        """Stops the game if tie"""
        list_ = list(filter(lambda x: type(x) != int, self.board))
        return len(list_) == 9


class TicTacToe():
    def __init__(self):
        os.system("clear")
        self.board = Board()
        self.player_1_char = ""
        self.player_2_char = ""
        self.corret_choice = False
        self.get_player_char()

    def reset(self):
        """Resets the internal state to prepare for a new game"""
        self.player_1_char = ""
        self.player_2_char = ""
        self.board.reset_board()

    def get_player_char(self):
        """Ask the player what character he wants to use and verify choice"""
        while True:
            player_1_char = input("Do you want to play X or O? ")
            print()
            if player_1_char == "X":
                self.player_1_char = "X"
                self.player_2_char = "O"
                print("Starting player selected X")
                break
            elif player_1_char == "O":
                self.player_1_char = "O"
                self.player_2_char = "X"
                print("Starting player selected O")
                break
            else:
                print("ERROR - input has to be either X or O!")
        os.system("clear")

    def get_player_input(self, player_char):
        while True:
            while True:
                x = input(f"{player_char} Where do you want to place your piece?")
                if x.isdigit():
                    x = int(x)
                    break
                else:
                    print("Input has to be a number, try again")

            if x > 0 and x < 10 and type(self.board.board[x]) != str:
                self.board.update(x, player_char)
                break
            elif x == 10:
                quit()
            else: 
                print("Spot is taken, try again: ")

    def check_tie(self):
        if self.board.tie():
            self.board.game_over = True
            print("Game is a tie")
            return True
        return False

    def run(self):
        self.board.draw_board()

        while not self.board.game_over:
            self.correct_player_1 = False
            self.correct_player_2 = False

            self.get_player_input(self.player_1_char)
            if self.board.game_over:
                break
            if self.check_tie():
                break

            self.get_player_input(self.player_2_char)
            if self.board.game_over:
                break
            if self.check_tie():
                break


while True:
    TicTacToe().run()

    user_input = "a"
    while user_input not in "ny":
        user_input = input("Play again? (y/n)").lower()

    if user_input == "y":
        continue
    else:
        break