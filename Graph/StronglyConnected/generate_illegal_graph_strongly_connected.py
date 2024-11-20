import random
import string

DENSITY = 0.1


def generate_random_string() -> str:
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))
    return generated_str


def generate_illegal_graph_strongly_connected() -> list:
    node_count = random.randint(2, 500)  # Ensure at least two nodes to make the graph not strongly connected
    graph = {}

    # Create nodes
    for _ in range(node_count):
        graph[generate_random_string()] = []

    nodes = list(graph.keys())

    # Divide nodes into two groups
    split_index = node_count // 2
    group1 = nodes[:split_index]
    group2 = nodes[split_index:]

    # Add edges within group1
    for source in group1:
        for target in group1:
            if source == target:
                continue  # Skip self-loops
            if random.random() < DENSITY:
                graph[source].append(target)

    # Add edges within group2
    for source in group2:
        for target in group2:
            if source == target:
                continue  # Skip self-loops
            if random.random() < DENSITY:
                graph[source].append(target)

    # Optional: Add edges from group1 to group2
    for source in group1:
        for target in group2:
            if random.random() < DENSITY:
                graph[source].append(target)

    # Do NOT add edges from group2 to group1 to ensure the graph is not strongly connected

    return list(graph.items())

if __name__ == '__main__':
    graph = generate_illegal_graph_strongly_connected()
    print(graph)