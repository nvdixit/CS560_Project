import random
import string
from BinaryTree import BinaryTree
import dump_to_file

ERROR_PERCENT = 0.05 # chance that the minheap value will be wrong

def generate_random_int(min_value, period) -> str:
    random_val = random.randint(0, period)
    rndm = random.random()
    return min_value + random_val if rndm > ERROR_PERCENT else min_value -random_val

def generate_illegal_bt(id_, min_value, period, node_count=100):
    if node_count <= 0:
        return None

    random_int = generate_random_int(min_value=min_value, period=period)
    root = BinaryTree(val=random_int, id_=id_)

    left_count = random.randint(0, node_count - 1)
    right_count = node_count - left_count - 1

    left_subtree = generate_illegal_bt(node_count=left_count, min_value=random_int, period=period, id_=id_ + 1)
    right_subtree = generate_illegal_bt(node_count=right_count, min_value=random_int, period=period,
                                      id_=id_ + left_count + 1)

    root.children.append(left_subtree)
    root.children.append(right_subtree)

    return root


# Error Types:
# 1: More than 2 children at one node
# 2: The Tree contains one loop/cycle
# 3: The tree contains a node with itself as a child

if __name__ == '__main__':
    random.seed(26) # temporarily have this for debug/testing purposes
    total_errs = 3
    size = 150
    for i in range(6):
        rndmInt = random.randint(0, size)
        err_node = random.randint(0, rndmInt - 1)
        period = random.randint(5, 30)
        min_value = random.randint(0, 250)
        tree = generate_illegal_bt(node_count=rndmInt, period=period, min_value=min_value,  id_=0)
        dump_to_file.dump_to_json_file(tree.flatten(), 'Illegal_BT_MH/illegal_bt_{0}.json'.format(i + 1))
