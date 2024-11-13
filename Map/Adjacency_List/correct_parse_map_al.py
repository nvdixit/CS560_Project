from generate_valid_map_al import *
from generate_invalid_map_al import *
from dump_to_file import *


def correct_parse_map_al(filepath):
    f = open(filepath)

    legal_map = True

    map = []

    # Run through every line in the map json file
    for line in f:
        if line == "{\n" or line == "}":
            continue
            
        # Get the line from the file and split on the colon seperating the key from the value
        key = line.split(":")[0]
        value = line.split(":")[1]

        # Strip whitespace 
        key = key.strip()
        value = value.strip()

        # If the value ends with a comma (is not the last value in the file), remove the comma
        value_final_char = value[len(value) - 1]
        if value_final_char == ",":
            value = value[: len(value) - 1]

        # If the key or value are missing, this is not a legal map
        if key == "null" or value == "null":
            legal_map = False
        else:
            # Remove the quotes around the key and value
            key = str(key)[1:]
            key = key[:len(key) - 1]
            key = int(key) # Cast to integer

            # Remove the brackets around the value
            value = str(value)[1:]
            value = str(value)[1 :len(value) - 2]
            value = value.split(',') # And split on the comma to make a list of strings
            
            # Cast each string in the value list to an int 
            value_ints = []
            for edge_str in value:
                edge_str_treated = edge_str.strip()

                if edge_str_treated == '':
                    value_ints.append(None)
                else:
                    edge_int = int(edge_str_treated)
                    value_ints.append(edge_int)

            # Check if this key already exists in the map
            for existing_pair in map:
                if key == existing_pair[0]:
                    legal_map = False

            map.append((key, value_ints)) # Add the pair to the map        

    f.close()

    # Run through all vertices in the map
    for vertex_edges in map:
        edges = vertex_edges[1] # Get the current vertex's edge list

        # Run through all those edges
        for edge in edges:
            vertex_found = False

            # Run through the entire map again
            for ve in map:
                v = ve[0] # Get the vertex on this runthrough

                # If the edge is not None (the current vertex is a sink)
                # and the vertex in the current vertex's edge list matches this vertex
                # We know that this edge exists in the graph
                if edge is not None and v == edge:
                    vertex_found = True
                else:
                    vertex_found = True

            # If we never found a match, the map is not valid (1+ vertices have edges that connect to vertices that don't exist)
            if not vertex_found:
                legal_map = False

    return legal_map
