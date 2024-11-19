import json
from BinaryTree import BinaryTree
# prints "INVALID BINARY TREE" IF ILLEGAL, NOTHING IF LEGAL
#returns True if legal, False if illegal

def verify_tree(filepath):
        with open(filepath, 'r') as f:
            try:
                nodes = json.load(f)
            except json.decoder.JSONDecodeError:
                # Json format incorrect
                return False

            tree = BinaryTree.from_json(nodes)
            if not tree:
                return False

            ret = check_mh(tree)

            return ret


def check_mh(tree):
    if not tree:
        return True

    if len(tree.children) != 2:
        return False

    if tree.children[0] and tree.val > tree.children[0].val:
        return False

    if tree.children[1] and tree.val > tree.children[1].val:
        return False

    left = check_mh(tree=tree.children[0])
    right = check_mh(tree=tree.children[1])

    return left and right



def test_legals():
    print("Legal:")
    for i in range(5):
        filepath = str("./Legal_BT_MH/legal_bt_" + str(i + 1) + ".json")
        legal = verify_tree(filepath)
        if not legal:
            print("INVALID BINARY TREE")


# NOTE: ILLEGAL BT 3 doesn't return False because the size is so small that it was made validly
def test_illegals():
    print("Illegal:")
    for i in range(6):
        print(i)
        filepath = str("./Illegal_BT_MH/illegal_bt_" + str(i + 1) + ".json")
        legal = verify_tree(filepath)
        if not legal:
            print("INVALID BINARY TREE")



if __name__ == '__main__':
    test_legals()
    test_illegals()