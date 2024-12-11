import random
import string
from BinaryTree import BinaryTree
import dump_to_file

# size = # nodes in tree,
# returns list of strings of length size * fraction
# by the pigeon hole principle, it guarantees that some must duplicate when we construct the tree
def generate_random_strings(size=150, fraction=.9) -> list:
    string_cnt = int(size * fraction)
    strings = []
    for i in range(string_cnt):
        str_len = random.randint(1, 50)
        generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
        strings.append(generated_str)

    return strings





def generate_illegal_bt(id_, vals, node_count=100):
    if node_count <= 0:
        return None

    left_count = random.randint(0, node_count - 1)
    right_count = node_count - left_count - 1

    left_subtree = generate_illegal_bt(node_count=left_count, id_=id_ + 1, vals=vals)
    right_subtree = generate_illegal_bt(node_count=right_count, id_=id_ + left_count + 1, vals=vals)


    index = random.randint(0, len(vals) - 1)
    root = BinaryTree(val=vals[index], id_=id_)

    root.children.append(left_subtree)
    root.children.append(right_subtree)

    return root



# Error Types:
# 1: More than 2 children at one node
# 2: The Tree contains one loop/cycle
# 3: The tree contains a node with itself as a child

if __name__ == '__main__':
    #random.seed(26) # temporarily have this for debug/testing purposes
    size = 150
    for i in range(6):
        rndmInt = random.randint(0, size)
        vals = generate_random_strings(rndmInt, fraction=.9)
        tree = generate_illegal_bt(id_=0, node_count=rndmInt, vals = vals)
        dump_to_file.dump_to_json_file(tree.flatten(), 'Illegal_BT_DV/illegal_bt_{0}.json'.format(i + 1))
