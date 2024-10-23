
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

    @classmethod
    def from_json(cls, json):
        obj = None
        if not json:
            return obj

        if "val" in json.keys() and "id" in json.keys():
            obj = cls(json["val"], json["id"])
        else:
            return obj

        if "children" in json.keys() and json["children"] is not None:
            for subtree in json["children"]:
                obj.children.append(cls.from_json(subtree))

        return obj