# under construction

from functools import partial


class Condition:

    def __init__(self):
        self.cond: partial = None


class Node:

    def __init__(self):
        self.left = None
        self.right = ''
        self.cond = None


class FFTClassifier:

    def __init__(self, tree=None):
        self.tree = tree
        # self.depth = depth

# def fit(data):
#     for
