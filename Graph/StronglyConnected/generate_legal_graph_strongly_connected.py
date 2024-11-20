import random
import string

DENSITY = 0.1

def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


def generate_legal_graph_strongly_connected() -> list:
    node_count = random.randint(0, 500)
    graph = {}

    for _ in range(node_count):
        graph[generate_random_string()] = []

    nodes = list(graph.keys())

    # Form a cycle to ensure strong connectivity
    for i in range(len(nodes)):
        source = nodes[i]
        target = nodes[(i + 1) % len(nodes)]  # Wrap around to form a cycle
        graph[source].append(target)

    # Add additional random edges based on DENSITY
    for s in nodes:
        for t in nodes:
            if s == t:
                continue

            if random.random() < DENSITY:
                graph[s].append(t)

    return list(graph.items())


if __name__ == '__main__':
    graph = generate_legal_graph_strongly_connected()
    # print(graph)
