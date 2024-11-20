import json


def is_cyc_util(adj, u, visited, rec_stack):
    if not visited[u]:

        # Mark the current node as visited
        # and part of recursion stack
        visited[u] = True
        rec_stack[u] = True

        # Recur for all the vertices
        # adjacent to this vertex
        for x in adj[u]:
            if not visited[x] and is_cyc_util(adj, x, visited, rec_stack):
                return True
            elif rec_stack[x]:
                return True

    # Remove the vertex from recursion stack
    rec_stack[u] = False
    return False


def is_cyclic(adj, V):
    visited = {k: False for k, v in adj.items()}
    rec_stack = {k: False for k, v in adj.items()}

    # Call the recursive helper function to
    # detect cycle in different DFS trees
    for u in adj.keys():
        if not visited[u] and is_cyc_util(adj, u, visited, rec_stack):
            return True

    return False


def correct_parse_graph_cyclic(filepath) -> bool:
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

        return is_cyclic(graph, len(graph.keys()))