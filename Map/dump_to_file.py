# Write the map to a .json string and dump to file
def dump_to_json_file(map, filepath):
    json_str = "{\n"

    idx = 0
    # Loop through the map and manually create the json string for each line
    for pair in map:
        key = pair[0]
        value = pair[1]

        s = ""

        if key is None:
            s = s + "\t\"" + "null" + "\": "
        else:
            s = s + "\t\"" + str(key) + "\": "

        if idx == len(map) - 1:
            if value is None:
                s = s + "\"" + "null" + "\"\n"
            else:
                s = s + "\"" + str(value) + "\"\n"
        else:
            if value is None:
                s = s + "\"" + "null" + ",\"\n"
            else:
                s = s + "\"" + str(value) + ",\"\n"
    
        json_str = json_str + s

        idx = idx + 1

    json_str = json_str + "}"

    # Dump the created map to a json file
    f = open(filepath, "w")
    f.write(str(json_str))
    f.close()