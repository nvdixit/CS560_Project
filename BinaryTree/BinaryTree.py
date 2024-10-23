
class BinaryTree:
    def __init__(self, val, id_):
        self.val = val
        self.id = id_
        self.children = [] # this will be used for an invalid bt (more than two children)

    def flatten(self):
        return {
            "val": self.val,
            "id": self.id,
            "children": [node.flatten() if node else None for node in self.children],
            #"right": self.right.flatten() if self.right else None,
        }