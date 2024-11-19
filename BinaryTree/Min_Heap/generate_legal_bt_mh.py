import random
import string
from BinaryTree import BinaryTree
import dump_to_file


# instead of strings, we'll use ints for ease of testing
# The int generated will be between 0 and the specified period (aka [0, period])
# 0 because a minheap can contain the same values
def generate_random_int(min_value, period) -> str:
    random_val = random.randint(0, period)
    return min_value + random_val


def generate_legal_bt(id_, min_value, period, node_count=100):
    if node_count <= 0:
        return None

    random_int = generate_random_int(min_value=min_value, period=period)
    root = BinaryTree(val=random_int, id_=id_)

    left_count = random.randint(0, node_count - 1)
    right_count = node_count - left_count - 1

    left_subtree = generate_legal_bt(node_count=left_count, min_value=random_int, period=period, id_=id_ + 1)
    right_subtree = generate_legal_bt(node_count=right_count, min_value=random_int, period=period,
                                      id_=id_ + left_count + 1)

    root.children.append(left_subtree)
    root.children.append(right_subtree)

    return root


def print_inorder_traversal(tree):
    if not tree:
        return 0

    left = print_inorder_traversal(tree=tree.children[0])
    print(tree.id, tree.val, tree.children, len(tree.children))
    right = print_inorder_traversal(tree=tree.children[1])

    return left + right + 1


def check_unique_ids(tree) -> list:
    if not tree:
        return []

    left = check_unique_ids(tree=tree.children[0])
    right = check_unique_ids(tree=tree.children[1])
    combined = left + right
    combined.append(tree.id)

    if len(combined) != len(set(combined)):
        print("ERROR: DUPLICATE IDS FOUND!!!")

    return combined


if __name__ == '__main__':
    random.seed(26)  # temporarily have this for debug/testing purposes
    for i in range(5):
        rndmInt = random.randint(0, 150)
        period = random.randint(5, 30)
        min_value = random.randint(0,250)
        tree = generate_legal_bt(node_count=rndmInt,min_value=min_value, period=period, id_=0)
        # ret = print_inorder_traversal(tree)
        ids = check_unique_ids(tree)
        assert (rndmInt == len(ids))
        dump_to_file.dump_to_json_file(tree.flatten(), 'Legal_BT_MH/legal_bt_{0}.json'.format(i + 1))