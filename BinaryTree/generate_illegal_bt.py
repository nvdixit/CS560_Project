import random
import string
from BinaryTree import BinaryTree
import dump_to_file


def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str



def add_illegal_children(id_, node_count, err_nodes, err_type):
    print("Add Illegal Children")
    rndm = random.randint(3, 5)
    subtree_size = node_count // rndm
    root = BinaryTree(val=generate_random_string(), id_=id_)

    for i in range(rndm):
        child = generate_illegal_bt(node_count=subtree_size, id_=id_ + (subtree_size * i + 1),
                                    err_nodes=err_nodes, err_type=err_type)
        root.children.append(child)

    return root

def create_cycle(root, tree):

    while True:
        if not tree.children[0] and not tree.children[1]: # Found a leaf node!
            break
        elif not tree.children[0]: # go down right subtree
            create_cycle(root, tree.children[1])
        elif not tree.children[1]: # go down left subtree
            create_cycle(root, tree.children[0])
        else:
            if random.random() >= 0.5: # For the right child subtree
                create_cycle(root, tree.children[1])
            else: # For the left child subtree
                create_cycle(root, tree.children[0])

    # Gonna create a new node with the same id, val to save memory space
    # could also just append the entire subtree but could get messy
    new_root = BinaryTree(val=root.val, id_=root.id)
    tree.children.append(new_root)

    return root


def generate_legal_tree(id_, err_nodes, err_type, node_count=100):
    left_count = random.randint(0, node_count - 1)
    right_count = node_count - left_count - 1

    left_subtree = generate_illegal_bt(node_count=left_count, id_=id_ + 1, err_nodes=err_nodes, err_type=err_type)
    right_subtree = generate_illegal_bt(node_count=right_count, id_=id_ + left_count + 1,
                                        err_nodes=err_nodes, err_type=err_type)

    root = BinaryTree(val=generate_random_string(), id_=id_)

    root.children.append(left_subtree)
    root.children.append(right_subtree)

    return root

def generate_illegal_bt(id_, err_nodes, err_type, node_count=100):
    if node_count <= 0:
        return None

    root = None
    if id_ == err_nodes:
        if err_type == 1:
            root = add_illegal_children(id_, node_count, err_nodes, err_type)
            return root

        elif err_type == 3:
            root = BinaryTree(val=generate_random_string(), id_=id_)
            child = BinaryTree(val=root.val, id_=root.id)
            root.children.append(child)

            count = node_count - 1
            subtree = generate_illegal_bt(node_count=count, id_=id_ + 1, err_nodes=err_nodes, err_type=err_type)
            if random.random() >= 0.5: # For the right child subtree
                root.children.append(subtree)
            else: # For the left child subtree
                root.children.insert(0, subtree)

            return root
        else:
            root = generate_legal_tree(id_=id_, node_count=node_count, err_nodes= err_nodes, err_type=err_type)


    else:
        root = generate_legal_tree(id_=id_, node_count=node_count, err_nodes= err_nodes, err_type=err_type)

    if id_ == err_nodes:
        # This will occur by randomly choosing a leaf node in the subtree
        # created above and adding the current root as a child
        if err_type == 2:
            root = create_cycle(root, root)


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
        print(i + 1)
        rndmInt = random.randint(0, size)
        err_node = random.randint(0, rndmInt - 1)
        tree = generate_illegal_bt(node_count=rndmInt, id_=0, err_nodes=err_node, err_type=i % total_errs + 1)
        #ret = print_inorder_traversal(tree)
        dump_to_file.dump_to_json_file(tree.flatten(), 'Illegal_BT/illegal_bt_{0}.json'.format(i + 1))
