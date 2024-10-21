import json


def correct_parse_graph(filepath) -> bool:
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

        for node, edges in graph.items():
            for target in edges:
                # Null node in edge list
                if target is None:
                    return False
                # If node contains an edge to itself
                if target == node:
                    return False
                # If target node not in the graph
                if target not in graph.keys():
                    return False

    return True
