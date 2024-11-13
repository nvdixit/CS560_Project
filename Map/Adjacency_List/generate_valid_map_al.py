import random
import math


def generate_valid_map_al():
    map_size = random.randint(0, 500)
    map = []

    vertices = []

    # Add all vertices to the graph
    for i in range(0, map_size):
        vertices.append(i)

    # Create edge lists for each vertex
    for vertex in vertices:
        # The list of each vertices' edges can be no more than map_size / 2
        edge_list_len = random.randrange(0, int(math.ceil(map_size / 2)))
        edge_list = []

        # Get a random element from the vertex set and add it to the current vertex's edge list
        # We allow multiple edges between the same two vertices as this is allowed by our FOL formulae 
        # for the semantics of adjacency lists
        for j in range(0, edge_list_len):
            candidate_vertex = random.choice(vertices)
            edge_list.append(candidate_vertex)
        
        map.append((vertex, edge_list))
        
    return map
