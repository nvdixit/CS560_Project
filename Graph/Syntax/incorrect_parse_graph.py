import json


# Parser that doesn't check for null nodes
def unchecked_null_nodes(filepath: str) -> bool:
    with open(filepath, 'r') as f:
        try:
            nodes: list = json.load(f)
        except json.decoder.JSONDecodeError:
            # Json format incorrect
            return False

        graph: dict = {}

        for node, edges in nodes:
            # If node is null or edges is null
            if edges is None:
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


# Parse that doesn't check for null edges
def unchecked_null_edges(filepath: str) -> bool:
    with open(filepath, 'r') as f:
        try:
            nodes: list = json.load(f)
        except json.decoder.JSONDecodeError:
            # Json format incorrect
            return False

        graph: dict = {}

        for node, edges in nodes:
            # If node is null or edges is null
            if node is None:
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


# Parser that doesn't check for duplicate nodes
def unchecked_duplicate_nodes(filepath) -> bool:
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


# Parser that doesn't check that there are no edges to null nodes
def unchecked_edge_to_null(filepath) -> bool:
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
                # If node contains an edge to itself
                if target == node:
                    return False
                # If target node not in the graph
                if target not in graph.keys():
                    return False
    return True


# Parser that doesn't check that nodes have no edges to itself
def unchecked_edge_to_self(filepath) -> bool:
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
                # If target node not in the graph
                if target not in graph.keys():
                    return False
    return True


# Parser that doesn't check that all edges lead to nodes in the graph
def unchecked_edge_to_nonexistent_node(filepath) -> bool:
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
    return True