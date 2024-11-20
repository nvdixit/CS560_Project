import json
from collections import deque


# Function to check if the graph is Bipartite using BFS
def is_bipartite(adj):
    # Initialize all as -1 (uncolored)
    color = {k: -1 for k, v in adj.items()}

    for u in adj.keys():

        # If the vertex is uncolored, start BFS from it
        if color[u] == -1:

            # Assign first color (0)
            color[u] = 0
            q = deque([u])

            while q:
                u = q.popleft()

                # Traverse all adjacent vertices
                for v in adj[u]:

                    # If the adjacent vertex is uncolored,
                    # assign alternate color
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)

                    # If the adjacent vertex has the same color,
                    # graph is not bipartite
                    elif color[v] == color[u]:
                        return False

    # If no conflicts in coloring, graph is bipartite
    return True


def correct_parse_graph_bipartite(filepath) -> bool:
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

        return is_bipartite(graph)
