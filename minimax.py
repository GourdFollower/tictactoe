from board import Board, State


class MiniMax:
    def __init__(self, max_state):
        self.tree = None
        self.max_state = max_state

    """Takes in current game state, returns updated state after chosen move"""
    def compute_move(self, board):
        if self.tree is not None:
            for i in self.tree.root.get_children():
                if i == board:
                    self.tree.root = i
                else:
                    self.make_tree(board)
                    self.check_win()
        else:
            self.make_tree(board)
            self.check_win()
        ret = self.choose_branch()
        return ret.board

    """Creates tree of possible boards"""
    def make_tree(self, board):
        root = Node(board, True)
        self.tree = Tree(root)
        self.fill_tree(root)

    def fill_tree(self, parent_node):
        if (parent_node.isMax and self.max_state == State.X) or\
                (not parent_node.isMax and self.max_state == State.O):
            c = parent_node.board.get_possible_boards(State.X)
        else:
            c = parent_node.board.get_possible_boards(State.O)

        isChildMax = not parent_node.isMax

        for q in c:
            new_node = Node(q, isChildMax)
            parent_node.add_child(new_node)

            if new_node.board.is_win()[0]:  # branch has ended
                continue

            if (isChildMax and self.max_state == State.X) or\
                    (not isChildMax and self.max_state == State.O):
                num = new_node.board.get_possible_boards(State.X)
            else:
                num = new_node.board.get_possible_boards(State.O)

            if len(num) > 0:
                self.fill_tree(new_node)

    """Assigns scores recursively to each node"""
    def check_win(self):
        root = self.tree.get_root()
        self.check_branch(root)

    def check_branch(self, node):
        c = node.get_children()
        for i in c:
            if len(i.get_children()) == 0: # did this get messed up?
                win = i.board.is_win()
                if win[0] and win[1] == self.max_state:
                    i.set_score(1)
                elif win[0] and win[1] != State.U:
                    i.set_score(-1)
                    # else default to 0
            else:
                self.check_branch(i)

        ret_node = self.find_best_child(node)
        node.set_score(ret_node.get_score())

    def find_best_child(self, node):
        children = node.get_children()
        is_max = node.is_max()

        if len(children) == 0: # although I don't think it ever gets called on a leaf
            return node.get_score()

        i_node = children[0]
        for i in children:
            if is_max:
                if i.get_score() > i_node.get_score():
                    i_node = i
                if i.board.is_win()[0] and i.board.is_win()[1] == self.max_state:
                    i_node = i
                    break

            if not is_max:
                if i.get_score() < i_node.get_score():
                    i_node = i
                if i.board.is_win()[0] and i.board.is_win()[1] != self.max_state:
                    i_node = i
                    break
        return i_node

    """Chooses best child"""
    def choose_branch(self):
        ret_node = self.find_best_child(self.tree.get_root())
        self.tree.root = ret_node
        return ret_node


class Node:
    def __init__(self, board, isMax):
        self.board = board
        self.isMax = isMax
        self.children = []
        self.score = 0 # is this correct default?

    def add_child(self, node):
        self.children.append(node)

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_children(self):
        return self.children

    def is_max(self):
        return self.isMax

    """Prints tree from node.
    Indentation currently not working with board str method."""
    def __str__(self, level=0):
        ret = "\t" * level + repr(self) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self):
        return self.board.__str__()


class Tree:
    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root
