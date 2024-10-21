import json


def correct_parse_graph(filepath) -> bool:
    legal_graph: bool = True
    with open(filepath, 'r') as f:
        try:
            graph: dict = json.load(f)
        except json.decoder.JSONDecodeError:
            return False

        for node, edges in graph.items():
            # If node is null or edges is null
            if node == "null" or edges is None:
                return False

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
