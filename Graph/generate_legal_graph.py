import random
import string

DENSITY: float = 0.5


def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


def generate_legal_graph() -> dict:
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

    return graph


if __name__ == '__main__':
    graph = generate_legal_graph()
    print(graph)
