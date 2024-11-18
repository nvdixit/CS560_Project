import random
import string
from BinaryTree import BinaryTree
import dump_to_file

# Generate Binary Trees that are balanced within a certain variable a

def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str



def generate_legal_bt(id_, node_count=100, a=1):
    if node_count <= 0:
        return None

    if node_count == 1:
        return BinaryTree(val=generate_random_string(), id_=id_)

    variance = random.randint(-a, a)
    left_count = node_count // 2 + variance
    right_count = node_count - left_count - 1

    #print(id_, node_count, variance,  left_count, right_count)

    left_subtree = generate_legal_bt(node_count=left_count, id_=id_ + 1)
    right_subtree = generate_legal_bt(node_count=right_count, id_=id_ + left_count + 1)

    root = BinaryTree(val=generate_random_string(), id_=id_)

    root.children.append(left_subtree) # will be none if there is no left subtree, making the right subtree in the valid spot
    root.children.append(right_subtree)

    return root


def print_inorder_traversal(tree):
    if not tree:
        return 0

    left = print_inorder_traversal(tree=tree.children[0])
    print(tree.id, tree.val, tree.children, len(tree.children))
    right = print_inorder_traversal(tree=tree.children[1])

    return left + right + 1




if __name__ == '__main__':
    random.seed(26) # temporarily have this for debug/testing purposes
    for i in range(5):
        rndmInt = random.randint(0,150)
        tree = generate_legal_bt(node_count=rndmInt, id_=0, a=1)
        dump_to_file.dump_to_json_file(tree.flatten(), 'Legal_BT_Balance/legal_bt_{0}.json'.format(i + 1))