import json
from BinaryTree import BinaryTree
# prints "INVALID BINARY TREE" IF ILLEGAL, NOTHING IF LEGAL
#returns True if legal, False if illegal


# Note: a will have to be sometimes greater than 1 to allow some leway for trees of random sizes
# unless the tree is not a sum(i^2) for i; 0...n, it will not be perfectly balanced
# where n is the depth of the tree.

def verify_tree(filepath,a=1):
        with open(filepath, 'r') as f:
            try:
                nodes = json.load(f)
            except json.decoder.JSONDecodeError:
                # Json format incorrect
                return False

            tree = BinaryTree.from_json(nodes)
            if not tree:
                return False

            _, ret = check_balance(tree, a=a)
            return ret


def check_balance(tree, a=1):
    if not tree:
        return 0, True

    if len(tree.children) == 0:
        return 1, True
    left_size, left_ret = check_balance(tree.children[0], a=a)
    right_size, right_ret = check_balance(tree.children[1], a=a)



    if not (left_ret and right_ret) or abs(left_size - right_size) > a:
        return left_size + right_size + 1, False

    return left_size + right_size + 1, True



def test_legals(a=1):
    print("Legal:")
    for i in range(5):
        filepath = str("./Legal_BT_Balance/legal_bt_" + str(i + 1) + ".json")
        legal = verify_tree(filepath,a=a)
        if not legal:
            print("INVALID BINARY TREE")



def test_illegals(a=1):
    print("Illegal:")
    for i in range(6):
        filepath = str("./Illegal_BT_Balance/illegal_bt_" + str(i + 1) + ".json")
        legal = verify_tree(filepath,a=a)
        if not legal:
            print("INVALID BINARY TREE")



if __name__ == '__main__':
    test_legals(a=5)
    test_illegals(a=5)