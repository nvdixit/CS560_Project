def correct_parse_map(filepath):
    f = open(filepath)

    legal_map = True

    map = []

    # Run through every line in the map json file
    for line in f:
        if line == "{\n" or line == "}":
            continue
            
        # Get the line from the file and split on the colon seperating the key from the value
        key = line.split(":")[0]
        value = line.split(":")[1]

        # Strip whitespace 
        key = key.strip()
        value = value.strip()

        # If the value ends with a comma (is not the last value in the file), remove the comma
        value_final_char = value[len(value) - 1]
        if value_final_char == ",":
            value = value[: len(value) - 1]

        # If the key or value are missing, this is not a legal map
        if key == "null" or value == "null":
            legal_map = False
        else:
            # Remove the quotes around the key and value
            key = str(key)[1:]
            key = key[:len(key) - 1]

            value = str(value)[1:]
            value = str(value)[:len(value) - 1]

            # Check if this key already exists in the map
            # If it does, this is not a legal map
            for existing_key in map:
                if key == existing_key[0]:
                    legal_map = False

            map.append((key, value)) # Add the pair to the map        

    f.close()

    return legal_map
