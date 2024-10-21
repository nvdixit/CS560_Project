from dump_to_file import *
from generate_legal_graph import *


# Generate 5 legal graphs
for i in range(5):
    graph: dict = generate_legal_graph()
    filepath: str = str("./Legal_Graphs/legal_graph_" + str(i + 1) + ".json")
    dump_to_json_file(graph, filepath)