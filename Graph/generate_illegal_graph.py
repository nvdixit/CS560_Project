import random
import string

DENSITY: float = 0.5


def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


# Generate a good node
def good_node(graph: dict) -> tuple[str, list]:
    node = generate_random_string()
    edges = []
    for t in graph.keys():
        if random.random() < DENSITY:
            edges.append(t)
    return node, edges


# Generate a node with an edge to a null node
def node_with_null_edge() -> tuple[str, list]:
    node = generate_random_string()
    edges = [None]
    return node, edges


# Generate a node with an edge to a node not in the graph
def node_not_in_graph() -> tuple[str, list]:
    node = generate_random_string()
    edges = [generate_random_string()]
    return node, edges


# Generate a node with an edge to itself
def node_with_self_edge() -> tuple[str, list]:
    node = generate_random_string()
    edges = [node]
    return node, edges


# Generate a duplicate node
def duplicate_node(graph: dict) -> tuple[str, list]:
    return random.choice(list(graph.items()))


# Generate a node with null label
def null_node() -> tuple[str, list]:
    return None, []


# Generate a node with null edges
def null_edges() -> tuple[str, list]:
    return generate_random_string(), None


# Generate a graph
def generate_illegal_graph(error_type):
    map_size = random.randint(0, 500)
    graph = {}

    return graph
