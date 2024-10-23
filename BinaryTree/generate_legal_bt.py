import random
import string
from BinaryTree import BinaryTree
import dump_to_file



def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str



def generate_legal_bt(id_, node_count=100):
    if node_count <= 0:
        return None

    left_count = random.randint(0, node_count - 1)
    right_count = node_count - left_count - 1

    left_subtree = generate_legal_bt(node_count=left_count, id_=id_ + 1)
    right_subtree = generate_legal_bt(node_count=right_count, id_=id_ + left_count + 1)

    root = BinaryTree(val=generate_random_string(), id_=id_)

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
    random.seed(26) # temporarily have this for debug/testing purposes
    for i in range(5):
        rndmInt = random.randint(0,150)
        tree = generate_legal_bt(node_count=rndmInt, id_=0)
        #ret = print_inorder_traversal(tree)
        ids = check_unique_ids(tree)
        assert(rndmInt == len(ids))
        dump_to_file.dump_to_json_file(tree.flatten(), 'Legal_BT/legal_bt_{0}.json'.format(i + 1))