from dump_to_file import *
from generate_legal_map import *
from generate_illegal_map import *
from correct_parse_map import *
from incorrect_parse_map import *


# Generate 5 legal maps
for i in range(0, 5):
    map = generate_legal_map()
    filepath = str("./Legal_Maps/legal_map_" + str(i + 1) + ".json")
    dump_to_json_file(map, filepath)

# Generate 5 illegal maps - 1 map for each possible fault
map_faults = ["duplicate_key_legal_value", "duplicate_key_null_value", "unique_key_null_value", "null_key_legal_value", "null_key_null_value"]
error_indicator = 2
for map_fault in map_faults:
    map = generate_illegal_map(error_indicator)
    filepath = str("./Illegal_Maps/" + map_fault + ".json")
    dump_to_json_file(map, filepath)

    error_indicator = error_indicator + 1


# Test the correct parsing function
for i in range(0, 5):
    filepath = str("./Legal_Maps/legal_map_" + str(i + 1) + ".json")
    map_is_legal = correct_parse_map(filepath)

    if map_is_legal:
        print("Correct parsing function worked on legal_map_" + str(i + 1))
    else:
        print("Correct parsing function failed on legal_map_" + str(i + 1))

for map_fault in map_faults:
    filepath = str("./Illegal_Maps/" + map_fault + ".json")
    map_is_legal = correct_parse_map(filepath)

    if not map_is_legal:
        print("Correct parsing function worked on illegal map " + map_fault)
    else:
        print("Correct parsing function failed on illegal map " + map_fault)

print()


# Test the incorrect parsing functions
for i in range(0, 3):
    if i == 0:
        for j in range(0, 5):
            filepath = str("./Legal_Maps/legal_map_" + str(j + 1) + ".json")
            map_is_legal = unchecked_null_keys(filepath)

            if map_is_legal:
                print("Incorrect parsing function (unchecked null keys) worked on legal_map_" + str(j + 1))
            else:
                print("Incorrect parsing function (unchecked null keys) failed on legal_map_" + str(j + 1))

        for map_fault in map_faults:
            filepath = str("./Illegal_Maps/" + map_fault + ".json")
            map_is_legal = unchecked_null_keys(filepath)

            if not map_is_legal:
                print("Incorrect parsing function (unchecked null keys) worked on illegal map " + map_fault)
            else:
                print("Incorrect parsing function (unchecked null keys) failed on illegal map " + map_fault)
        print()

    if i == 1:
        for j in range(0, 5):
            filepath = str("./Legal_Maps/legal_map_" + str(j + 1) + ".json")
            map_is_legal = unchecked_null_values(filepath)

            if map_is_legal:
                print("Incorrect parsing function (unchecked null values) worked on legal_map_" + str(j + 1))
            else:
                print("Incorrect parsing function (unchecked null values) failed on legal_map_" + str(j + 1))

        for map_fault in map_faults:
            filepath = str("./Illegal_Maps/" + map_fault + ".json")
            map_is_legal = unchecked_null_values(filepath)

            if not map_is_legal:
                print("Incorrect parsing function (unchecked null values) worked on illegal map " + map_fault)
            else:
                print("Incorrect parsing function (unchecked null values) failed on illegal map " + map_fault)
        print()

    if i == 2:
        for j in range(0, 5):
            filepath = str("./Legal_Maps/legal_map_" + str(j + 1) + ".json")
            map_is_legal = unchecked_duplicate_keys(filepath)

            if map_is_legal:
                print("Incorrect parsing function (unchecked duplicate keys) worked on legal_map_" + str(j + 1))
            else:
                print("Incorrect parsing function (unchecked duplicate keys) failed on legal_map_" + str(j + 1))

        for map_fault in map_faults:
            filepath = str("./Illegal_Maps/" + map_fault + ".json")
            map_is_legal = unchecked_duplicate_keys(filepath)

            if not map_is_legal:
                print("Incorrect parsing function (unchecked duplicate keys) worked on illegal map " + map_fault)
            else:
                print("Incorrect parsing function (unchecked duplicate keys) failed on illegal map " + map_fault)
        print()