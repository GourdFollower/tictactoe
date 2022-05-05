from player import Player
from minimax import MiniMax
from board import State, Board


class Controller:
    def __init__(self):
        self.comp = None
        self.player = Player()
        self.board = Board()
        self.player_state = None

    """Game logic"""
    def play(self):
        self.set_x_o()
        if self.player_state == State.O:
            self.comp_move()
            print(self.board)

        while not self.board.is_win()[0]:
            self.player_move()
            print(self.board)
            if self.board.is_win()[0]:
                break
            self.comp_move()
            print(self.board)
        a = self.board.is_win()
        if a[1] == State.X:
            print("The X's have it!")
        elif a[1] == State.O:
            print("The O's have it!")
        else:
            print("Alas, cat's game.")

    def player_move(self):
        num = self.player.get_place()
        self.board.play_move(num, self.player_state)

    def comp_move(self):
        self.board = self.comp.compute_move(self.board)

    def set_x_o(self):
        xo = self.player.x_or_o()
        self.player_state = xo
        if xo == State.X:
            self.comp = MiniMax(State.O)
        else:
            self.comp = MiniMax(State.X)
