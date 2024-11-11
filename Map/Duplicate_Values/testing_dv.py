from dump_to_file import *
from generate_valid_map_dv import *
from generate_invalid_map_dv import *
from correct_parse_map_dv import *
from incorrect_parse_map_dv import *


# Generate 5 valid DV maps
for i in range(0, 5):
    map = generate_valid_map_dv()
    filepath = str("./Valid_Maps_DV/valid_map_dv_" + str(i + 1) + ".json")
    dump_to_json_file(map, filepath)

# Generate 5 invalid DV maps, which all have duplicate values
for i in range(0, 5):
    map = generate_invalid_map_dv()
    filepath = str("./Invalid_Maps_DV/invalid_map_dv_" + str(i + 1) + ".json")
    dump_to_json_file(map, filepath)


# Test the correct parsing function on all 10 maps
for i in range(0, 5):
    filepath = str("./Valid_Maps_DV/valid_map_dv_" + str(i + 1) + ".json")
    valid_map_dv = correct_parse_map_dv(filepath)

    if valid_map_dv:
        print("Correct parsing function worked on valid_map_dv_" + str(i + 1) + ".json")
    else:
        print("Correct parsing function failed on valid_map_dv_" + str(i + 1) + ".json")

    filepath = str("./Invalid_Maps_DV/invalid_map_dv_" + str(i + 1) + ".json")
    valid_map_dv = correct_parse_map_dv(filepath)

    if not valid_map_dv:
        print("Correct parsing function worked on invalid_map_dv_" + str(i + 1) + ".json")
    else:
        print("Correct parsing function failed on invalid_map_dv_" + str(i + 1) + ".json")

print()

# Test the incorrect parsing function on all 10 maps
for i in range(0, 5):
    filepath = str("./Valid_Maps_DV/valid_map_dv_" + str(i + 1) + ".json")
    invalid_map_dv = incorrect_parse_map_dv(filepath)

    if invalid_map_dv:
        print("Incorrect parsing function worked on valid_map_dv_" + str(i + 1) + ".json")
    else:
        print("Incorrect parsing function failed on valid_map_dv_" + str(i + 1) + ".json")

    filepath = str("./Invalid_Maps_DV/invalid_map_dv_" + str(i + 1) + ".json")
    invalid_map_dv = incorrect_parse_map_dv(filepath)

    if not invalid_map_dv:
        print("Incorrect parsing function worked on invalid_map_dv_" + str(i + 1) + ".json")
    else:
        print("Incorrect parsing function failed on invalid_map_dv_" + str(i + 1) + ".json")

print()
