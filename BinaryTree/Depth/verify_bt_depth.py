import json
from BinaryTree import BinaryTree
# prints "INVALID BINARY TREE" IF ILLEGAL, NOTHING IF LEGAL
#returns True if legal, False if illegal


# Checks if the depth of each tree is less than the depth passed in as a param
# no illegal trees for this because it just checks depth

def verify_tree(filepath, depth=50):
        with open(filepath, 'r') as f:
            try:
                nodes = json.load(f)
            except json.decoder.JSONDecodeError:
                # Json format incorrect
                return False

            tree = BinaryTree.from_json(nodes)
            if not tree:
                return False

            max_depth = check_depth(tree)

            return True if max_depth < depth else False



def check_depth(tree):
    if not tree:
        return 0

    if len(tree.children) == 0:
        return 1

    left_depth = check_depth(tree.children[0])
    right_depth = check_depth(tree.children[1])

    return max(left_depth, right_depth) + 1



def test_trees(depth=50):
    print("Legal:")
    for i in range(10):
        filepath = str("./BT_Depth/bt_" + str(i + 1) + ".json")
        legal = verify_tree(filepath, depth=depth)
        if not legal:
            print("INVALID BINARY TREE")




if __name__ == '__main__':
    test_trees(depth=10)
