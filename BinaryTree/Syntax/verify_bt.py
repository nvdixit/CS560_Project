import json
from BinaryTree.Syntax.BinaryTree import BinaryTree
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

            _, ret = check_unique_ids(tree)
            if not ret:
                return ret

            ret = check_children(tree)

            return ret


def check_children(tree):
    if not tree:
        return True

    if len(tree.children) != 2:
        return False

    left = check_children(tree=tree.children[0])
    right = check_children(tree=tree.children[1])

    return left and right

def check_unique_ids(tree) -> (list, bool):
    ret = True
    if not tree:
        return ([], ret)

    left, left_ret = check_unique_ids(tree=tree.children[0])
    right, right_ret = check_unique_ids(tree=tree.children[1])
    combined = left + right
    combined.append(tree.id)

    if not (left_ret and right_ret) or len(combined) != len(set(combined)):
        ret = False

    return (combined, ret)


def test_legals():
    print("Legal:")
    for i in range(5):
        filepath = str("./Legal_BT/legal_bt_" + str(i + 1) + ".json")
        legal = verify_tree(filepath)
        if not legal:
            print("INVALID BINARY TREE")



def test_illegals():
    print("Illegal:")
    for i in range(6):
        filepath = str("./Illegal_BT/illegal_bt_" + str(i + 1) + ".json")
        legal = verify_tree(filepath)
        if not legal:
            print("INVALID BINARY TREE")



if __name__ == '__main__':
    test_legals()
    test_illegals()