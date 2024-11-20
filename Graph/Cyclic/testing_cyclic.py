from dump_to_file import *
from generate_legal_graph_cyclic import *
from generate_illegal_graph_cyclic import *
from correct_parse_graph_cyclic import *


cycle_lengths = [3, 5, 10, 20, 50]

# Generate 5 legal cyclic graphs
for cycle_length in cycle_lengths:
    graph: list = generate_legal_graph_cyclic(cycle_length)
    filepath: str = str(f"./Legal_Graphs/legal_cyclic_graph_length_{cycle_length}.json")
    dump_to_json_file(graph, filepath)

# Generate 5 illegal graphs
for cycle_length in cycle_lengths:
    graph = generate_illegal_graph_cyclic(cycle_length)
    filepath: str = str(f"./Illegal_Graphs/illegal_cyclic_graph_length_{cycle_length}.json")
    dump_to_json_file(graph, filepath)

# Test the correct parsing function
for cycle_length in cycle_lengths:
    filepath: str = str(f"./Legal_Graphs/legal_cyclic_graph_length_{cycle_length}.json")
    legal = correct_parse_graph_cyclic(filepath)

    if legal:
        print("Correct parsing function worked on legal_graph_length_" + str(cycle_length))
    else:
        print("Correct parsing function failed on legal_graph_length_" + str(cycle_length))

for cycle_length in cycle_lengths:
    filepath: str = str(f"./Illegal_Graphs/illegal_cyclic_graph_length_{cycle_length}.json")
    legal = correct_parse_graph_cyclic(filepath)

    if not legal:
        print("Correct parsing function worked on illegal_graph_length_" + str(cycle_length))
    else:
        print("Correct parsing function failed on illegal_graph_length_" + str(cycle_length))
