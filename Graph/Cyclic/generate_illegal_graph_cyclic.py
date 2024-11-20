import random
import string


def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


def generate_illegal_graph_cyclic(cycle_length: int) -> list:
    graph = {}

    for i in range(cycle_length):
        graph[generate_random_string()] = []

    nodes = list(graph.keys())
    for i, s in enumerate(nodes):
        if random.random() < 0.25:
            if i < cycle_length - 1:
                graph[s].append(nodes[i+1])
            else:
                graph[s].append(nodes[0])

    return list(graph.items())


if __name__ == '__main__':
    graph = generate_illegal_graph_cyclic(5)
    print(graph)
