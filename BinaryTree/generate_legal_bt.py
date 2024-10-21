import random
import string

import dump_to_file



def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


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



def generate_legal_bt(id_, node_count=100):
    if node_count <= 0:
        return None

    left_count = random.randint(0, node_count)
    right_count = node_count - left_count - 1

    left_subtree = generate_legal_bt(node_count=left_count, id_=id_ + 1)
    right_subtree = generate_legal_bt(node_count=right_count,id_=id_ + left_count + 1)

    root = BinaryTree(val=generate_random_string(), id_=id_)

    root.children.append(left_subtree)
    root.children.append(right_subtree)

    return root


def print_inorder_traversal(tree):
    if not tree:
        return

    print_inorder_traversal(tree=tree.children[0])
    print(tree.id, tree.val, tree.children, len(tree.children))
    print_inorder_traversal(tree=tree.children[1])







if __name__ == '__main__':
    random.seed(26) # temporarily have this for debug/testing purposes
    for i in range(5):
        tree = generate_legal_bt(node_count=random.randint(0,150), id_=0)
        dump_to_file.dump_to_json_file(tree.flatten(), 'Legal_BT/legal_bt_{0}.json'.format(i + 1))
    #print_inorder_traversal(tree)