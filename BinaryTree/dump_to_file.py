import json

def dump_to_json_file(tree, filepath) -> None:
    with open(filepath, "w") as outfile:
        json.dump(tree, outfile, indent=4)



