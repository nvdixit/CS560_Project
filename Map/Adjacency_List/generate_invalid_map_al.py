import random
import math


def generate_invalid_map_al():
    # In order for a map to be an invalid adjacency list, it must have more than 0 elements
    # as empty maps are legal
    map_size = random.randint(5, 500)
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

        for j in range(0, edge_list_len):
            # Decide if the vertex to add to the edge list is legitimate or not
            legitimate_vertex = random.randrange(0, 2)

            # If it is legit, add a random vertex that is not already in the edge list
            if legitimate_vertex == 1:
                candidate_vertex = random.choice(vertices)
                edge_list.append(candidate_vertex)
            
            # If it is not legit, add a random vertex whose ID is greater than any possible in the graph (map_size to 600)
            else:
                illegal_vertex = random.randrange(map_size, 600)
                edge_list.append(illegal_vertex)
    
        map.append((vertex, edge_list))
        
    return map
