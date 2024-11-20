import json


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


def transpose_graph(graph):
    transposed = {}
    for node in graph:
        transposed.setdefault(node, [])  # Ensure every node appears in the transposed graph
    for source in graph:
        for target in graph[source]:
            transposed.setdefault(target, [])
            transposed[target].append(source)
    return transposed


def correct_parse_graph_strongly_connected(filepath) -> bool:
    with open(filepath, 'r') as f:
        try:
            nodes: list = json.load(f)
        except json.decoder.JSONDecodeError:
            # Json format incorrect
            return False

        graph: dict = {}

        for node, edges in nodes:
            # If node is null or edges is null
            if node is None or edges is None:
                return False

            # If node already in the graph
            if node in graph.keys():
                return False

            graph[node] = edges

        if not graph:
            return True

        # Pick any node as the starting point
        start_node = next(iter(graph))

        # Perform DFS on the original graph
        visited = dfs(graph, start_node)

        if len(visited) != len(graph):
            # Not all nodes are reachable from start_node
            return False

        # Transpose the graph
        transposed_graph = transpose_graph(graph)

        # Perform DFS on the transposed graph
        visited_transposed = dfs(transposed_graph, start_node)

        if len(visited_transposed) != len(graph):
            # Not all nodes can reach start_node
            return False

        # The graph is strongly connected
        return True
