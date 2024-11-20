import random
import string

DENSITY: float = 0.5


def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


def generate_illegal_graph_directed() -> list:
    node_count = random.randint(0, 500)
    graph = {}

    for i in range(node_count):
        graph[generate_random_string()] = []

    nodes = list(graph.keys())
    for s in nodes:
        for t in nodes:
            if s == t:
                continue

            # Generate a directed graph by adding both directions in adj list
            if random.random() < DENSITY:
                graph[s].append(t)
                graph[t].append(s)

    return list(graph.items())


if __name__ == '__main__':
    graph = generate_illegal_graph_directed()
    print(graph)
