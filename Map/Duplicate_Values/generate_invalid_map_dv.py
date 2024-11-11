import random
import string

# Generate a random 1 - 50 character alphanumeric string
def generate_random_string():
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))

    return generated_str


# Generate a legal map with no duplicate values
# The map returned by this method will be half of the whole invalid map
def generate_valid_submap(map_size):
    map = []

    # Iteratively generate each (key, value) pair
    for i in range(0, map_size):
        generated_key = None
        generated_value = None
        already_exists = True

        while already_exists:
            generated_key = generate_random_string()
            generated_value = generate_random_string()

            one_in_map = False
            for pair in map:
                if generated_key == pair[0] or generated_value == pair[1]:
                    one_in_map = True

            if not one_in_map:
                already_exists = False

        map.append((generated_key, generated_value))

    return map



# Generate a semantically invalid map that has duplicate values
def generate_invalid_map_dv():
    # Generate a random map size from 0 - 500. 
    # Allowing empty maps captures the nullary list property from TADT
    map_size = random.randint(0, 500)

    # Half the map will be legal (key, value) pairs
    map = generate_valid_submap(int(map_size * 0.5))
    
    # The rest of the map will be erroneous (key, value) pairs
    # Iteratively generate each (key, value) pair
    for i in range(int(map_size * 0.5) + 1, map_size):
        existing_value = random.choice(map)[1]

        # Correctly get a new unique key
        generated_key = None
        key_already_exists = True
        while key_already_exists:
            generated_key = generate_random_string()

            key_in_map = False
            for pair in map:
                if generated_key == pair[0]:
                    key_in_map = True

            if not key_in_map:
                key_already_exists = False

        # Add the correct key and the duplicate value to the map
        map.append((generated_key, existing_value))

    random.shuffle(map) # Shuffle the map in place

    return map
