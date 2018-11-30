class Node:

    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def __str__(self, level=0):
        r = "\t"*level + str(self.val) + "\n"
        for child in self.children:
            r += child.__str__(level + 1)
            
        return r

    def __repr__(self):
        return '<Node>'
