import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action



parent = Node((1,2), parent=None, action=None)

state = (2,3)

child = Node(state=state, parent=parent, action="up")

rec_child = child.parent



print(parent.state)
print(parent.action)
print(parent.parent)
print(id(parent))

print(child.state)
print(child.action)
print(child.parent)

print(rec_child.state)
print(rec_child.action)