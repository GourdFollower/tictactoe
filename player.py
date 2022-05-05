from board import State


class Player:
    def __init__(self):
        pass

    """Takes input of location where player would like to play"""
    def get_place(self):
        accepted = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        num = input("Please enter the number of the location in which you would like to play: ")
        if num not in accepted:
            raise AssertionError("Invalid input")
        return int(num)

    """Takes input of whether player would like to be X or O"""
    def x_or_o(self):
        accepted = ["X", "O"]
        char = input("If you would like to play X, enter X. Otherwise, enter O. ")
        char = char.upper()
        if char not in accepted:
            raise AssertionError("Invalid input")
        if char == "X":
            return State.X
        return State.O