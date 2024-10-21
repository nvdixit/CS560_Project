import json


def dump_to_json_file(graph: list, filepath: str) -> None:
    with open(filepath, "w") as outfile:
        json.dump(graph, outfile, indent=4)
