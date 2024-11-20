import random
import string

DENSITY: float = 0.1


def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


def generate_legal_graph_bipartite() -> list:
    graph = {}


    set1 = set()
    set2 = set()

    node_count = random.randint(0, 250)
    for i in range(node_count):
        set1.add(generate_random_string())

    node_count = random.randint(0, 250)
    for i in range(node_count):
        set2.add(generate_random_string())

    nodes = []
    for n in set1:
        nodes.append(n)
    for n in set2:
        nodes.append(n)
    random.shuffle(nodes)

    for n in nodes:
        graph[n] = []

    for s in set1:
        for t in set2:
            if random.random() < DENSITY:
                graph[s].append(t)
                graph[t].append(s)

    return list(graph.items())


if __name__ == '__main__':
    graph = generate_legal_graph_bipartite()
    print(graph)
