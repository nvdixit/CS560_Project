from dump_to_file import *
from generate_legal_graph_bipartite import *
from generate_illegal_graph_bipartite import *
from correct_parse_graph_bipartite import *


# Generate 5 legal graphs
for i in range(5):
    graph: list = generate_legal_graph_bipartite()
    filepath: str = str("./Legal_Graphs/legal_bipartite_graph_" + str(i + 1) + ".json")
    dump_to_json_file(graph, filepath)

# Generate 5 illegal graphs
for i in range(5):
    graph = generate_illegal_graph_bipartite()
    filepath: str = str("./Illegal_Graphs/illegal_bipartite_graph_" + str(i + 1) + ".json")
    dump_to_json_file(graph, filepath)

# Test the correct parsing function
for i in range(5):
    filepath: str = str("./Legal_Graphs/legal_bipartite_graph_" + str(i + 1) + ".json")
    legal = correct_parse_graph_bipartite(filepath)

    if legal:
        print("Correct parsing function worked on legal_bipartite_graph_" + str(i + 1))
    else:
        print("Correct parsing function failed on legal_bipartite_graph_" + str(i + 1))

for i in range(5):
    filepath: str = str("./Illegal_Graphs/illegal_bipartite_graph_" + str(i + 1) + ".json")
    legal = correct_parse_graph_bipartite(filepath)

    if not legal:
        print("Correct parsing function worked on illegal_bipartite_graph_" + str(i + 1))
    else:
        print("Correct parsing function failed on illegal_bipartite_graph_" + str(i + 1))