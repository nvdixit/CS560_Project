from dump_to_file import *
from generate_legal_graph_strongly_connected import *
from generate_illegal_graph_strongly_connected import *
from correct_parse_graph_strongly_connected import *


# Generate 5 legal graphs
for i in range(5):
    graph: list = generate_legal_graph_strongly_connected()
    filepath: str = str("./Legal_Graphs/legal_strongly_connected_graph_" + str(i + 1) + ".json")
    dump_to_json_file(graph, filepath)

# Generate 5 illegal graphs
for i in range(5):
    graph = generate_illegal_graph_strongly_connected()
    filepath: str = str("./Illegal_Graphs/illegal_strongly_connected_graph_" + str(i + 1) + ".json")
    dump_to_json_file(graph, filepath)

# Test the correct parsing function
for i in range(5):
    filepath: str = str("./Legal_Graphs/legal_strongly_connected_graph_" + str(i + 1) + ".json")
    legal = correct_parse_graph_strongly_connected(filepath)

    if legal:
        print("Correct parsing function worked on legal_strongly_connected_graph_" + str(i + 1))
    else:
        print("Correct parsing function failed on legal_strongly_connected_graph_" + str(i + 1))

for i in range(5):
    filepath: str = str("./Illegal_Graphs/illegal_strongly_connected_graph_" + str(i + 1) + ".json")
    legal = correct_parse_graph_strongly_connected(filepath)

    if not legal:
        print("Correct parsing function worked on illegal_strongly_connected_graph_" + str(i + 1))
    else:
        print("Correct parsing function failed on illegal_strongly_connected_graph_" + str(i + 1))