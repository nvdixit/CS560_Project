from dump_to_file import *
from generate_legal_graph import *
from generate_illegal_graph import *
from correct_parse_graph import *


# Generate 5 legal graphs
for i in range(5):
    graph: list = generate_legal_graph()
    filepath: str = str("./Legal_Graphs/legal_graph_" + str(i + 1) + ".json")
    dump_to_json_file(graph, filepath)

# Generate 6 illegal graphs - 1 map for each possible fault
graph_faults = ["node_with_null_edge", "edge_to_nonexistent_node", "edge_to_itself", "duplicate_node", "null_node", "null_edge"]
error_indicator = 1
for fault in graph_faults:
    graph = generate_illegal_graph(error_indicator)
    filepath = str("./Illegal_Graphs/" + fault + ".json")
    dump_to_json_file(graph, filepath)
    error_indicator = error_indicator + 1

# Test the correct parsing function
for i in range(0, 5):
    filepath = str("./Legal_Graphs/legal_graph_" + str(i + 1) + ".json")
    legal = correct_parse_graph(filepath)

    if legal:
        print("Correct parsing function worked on legal_map_" + str(i + 1))
    else:
        print("Correct parsing function failed on legal_map_" + str(i + 1))

for fault in graph_faults:
    filepath = str("./Illegal_Graphs/" + fault + ".json")
    map_is_legal = correct_parse_graph(filepath)

    if not map_is_legal:
        print("Correct parsing function worked on illegal map " + fault)
    else:
        print("Correct parsing function failed on illegal map " + fault)