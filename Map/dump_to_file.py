

# Write the map to a .json string and dump to file
def dump_to_json_file(map, filepath):
    json_str = "{\n"

    idx = 0
    # Loop through the map and manually create the json string for each line
    for pair in map:
        key = pair
        value = None

        s = ""

        if len(pair) == 2:
            key = pair[0]
            value = pair[1]

            s = s + "\t\"" + str(key) + "\": "
            if idx == len(map) - 1:
                s = s + "\"" + str(value) + "\"\n"
            else:
                s = s + "\"" + str(value) + "\",\n"

        else:
            s = s + "\t\"" + str(key) + "\": null"
            if idx == len(map) - 1:
                s = s + "\n"
            else:
                s = s + ",\n"
    
        json_str = json_str + s

        idx = idx + 1
    json_str = json_str + "\n}"

    # Dump the created map to a json file
    f = open(filepath, "w")
    f.write(str(json_str))
    f.close()