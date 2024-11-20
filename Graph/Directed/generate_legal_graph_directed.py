import random
import string

DENSITY: float = 0.1


def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


def generate_legal_graph_directed() -> list:
    node_count = random.randint(0, 500)
    graph = {}

    for i in range(node_count):
        graph[generate_random_string()] = []

    nodes = list(graph.keys())
    for s in nodes:
        for t in nodes:
            if s == t:
                continue

            if random.random() < DENSITY:
                graph[s].append(t)

    return list(graph.items())


if __name__ == '__main__':
    graph = generate_legal_graph_directed()
    print(graph)
