from enum import Enum


class State(Enum):
    U = 0
    X = 1
    O = 2


class Board:
    def __init__(self):
        self.spaces = []
        for i in range(9):
            self.spaces.append(State.U)

    def __str__(self):
        toPrint = ""
        for i in range(9):
            temp = self.spaces[i].name
            toPrint += temp
            if i == 2 or i == 5:
                toPrint += "\n"
            elif i == 8:
                toPrint += "\n-----"
            else:
                toPrint += " "
        return toPrint

    def copy_self(self):
        ret = Board()
        for i in range(9):
            ret.spaces[i] = self.spaces[i]
        return ret

    """Update board to reflect played move.
    Input must be of either X or O."""
    def play_move(self, index, state):
        assert state == State.X or state == State.O
        if self.spaces[index] != State.U:
            raise Exception('Cannot play on existing X or O')
        self.spaces[index] = state

    """Returns a list of possible boards for moves for the given player"""
    def get_possible_boards(self, player):
        assert player == State.X or player == State.O
        gen = []
        for i in range(len(self.spaces)):
            if self.spaces[i] == State.U:
                temp = self.copy_self()
                temp.play_move(i, player)
                gen.append(temp)
        return gen

    """Checks if either player has won or the board is full. Returns tuple: boolean and X/O/U."""
    def is_win(self):
        a = (False, State.U)
        if self.spaces[0] == self.spaces[1] and self.spaces[0] == self.spaces[2]:
            a = (True, self.spaces[0])
        elif self.spaces[0] == self.spaces[3] and self.spaces[0] == self.spaces[6]:
            a = (True, self.spaces[0])
        elif self.spaces[0] == self.spaces[4] and self.spaces[0] == self.spaces[8]:
            a = (True, self.spaces[0])
        elif self.spaces[3] == self.spaces[4] and self.spaces[3] == self.spaces[5]:
            a = (True, self.spaces[3])
        elif self.spaces[1] == self.spaces[4] and self.spaces[1] == self.spaces[7]:
            a = (True, self.spaces[1])
        elif self.spaces[2] == self.spaces[4] and self.spaces[2] == self.spaces[6]:
            a = (True, self.spaces[2])
        elif self.spaces[6] == self.spaces[7] and self.spaces[6] == self.spaces[8]:
            a = (True, self.spaces[6])
        elif self.spaces[2] == self.spaces[5] and self.spaces[2] == self.spaces[8]:
            a = (True, self.spaces[2])
        if a[1] == State.U:
            a = (False, State.U)

        count = 0
        if not a[0]: # check if board is full
            for i in self.spaces:
                if i == State.U:
                    break
                count += 1
            if count == 9:
                a = (True, State.U)

        return a
