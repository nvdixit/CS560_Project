import random
import string
from dump_to_file import *

# Generate a random 1 - 50 character alphanumeric string
def generate_random_string():
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))

    return generated_str


# Generate a good element of the map
# Good elements are a (key, value) pair where key doesn not already exist in the map
def generate_good_element(keys):
    generated_key = None
    key_already_exists = True

    while key_already_exists:
        generated_key = generate_random_string()

        key_in_map = False
        for key in keys:
            if generated_key == key:
                key_in_map = True

        key_already_exists = key_in_map

    generated_value = generate_random_string()

    return (generated_key, generated_value)


# Generate an element with a duplicate key
def generate_bad_element_duplicate_key(keys):
    keys_len = len(keys)
    random_idx = 0 
    
    if keys_len > 1:
        random_idx = random.randint(0, keys_len - 1)

    random_element = keys[random_idx]
    new_random_value = generate_random_string()

    if len(random_element) == 2:
        random_element = keys[random_idx][0]

    return (random_element, new_random_value)


# Generate an element with a duplicate key and no value
def generate_bad_element_duplicate_single_key(keys):
    keys_len = len(keys)
    random_idx = 0 
    
    if keys_len > 1:
        random_idx = random.randint(0, keys_len - 1)

    random_element = keys[random_idx]

    if len(random_element) == 2:
        random_element = keys[random_idx][0]

    return random_element


# Generate an element with no value (the element is just a key, not a (key, value) pair)
def generate_bad_element_single_key(keys):
    generated_key = None
    key_already_exists = True

    while key_already_exists:
        generated_key = generate_random_string()

        key_in_map = False
        for key in keys:
            if generated_key == key:
                key_in_map = True

        key_already_exists = key_in_map

    return generated_key


# Generate a map
def generate_illegal_map():
    # Generate a random map size from 0 - 500. 
    # Allowing empty maps captures the nullary list property from TADT
    map_size = random.randint(0, 500)
    keys = []
    map = []

    # Whether each of the 4 errors have occurred
    good_element = False
    single_key = False
    duplicate_key = False
    duplicate_single_key = False

    # Iteratively generate each (key, value) pair
    for i in range(0, map_size):
        select_element = random.randint(1, 4) # Randomly pick a good/bad element to generate
        
        # Generate a good element
        if select_element == 1:
            pair = generate_good_element(keys)
            map.append(pair)
            keys.append(pair[0])
            good_element = True

        # Generate an element with just a key and no value
        elif select_element == 2:
            key = generate_bad_element_single_key(keys)
            map.append(key)
            keys.append(key)
            single_key = True

        # Generate an element whose key is duplicate
        elif select_element == 3 and len(keys) > 0:
            pair = generate_bad_element_duplicate_key(keys)
            map.append(pair)
            keys.append(pair[0])
            duplicate_key = True

        # Generate an element with no value whose key is duplicate
        elif select_element == 4 and len(keys) > 0:
            key = generate_bad_element_duplicate_single_key(keys)
            map.append(key)
            keys.append(key)
            duplicate_single_key = True

    # If any of the element generations were not randomly selected
    # Do them now
    if not good_element:
        pair = generate_good_element(keys)
        map.append(pair)

    if not single_key:
        key = generate_bad_element_single_key(keys)
        map.append(key)   

    if not duplicate_key:
        pair = generate_bad_element_duplicate_key(keys)
        map.append(pair)

    if not duplicate_single_key:
        pair = generate_bad_element_duplicate_single_key(keys)
        map.append(pair)

    return map


for i in range(0, 5):
    map = generate_illegal_map()
    dump_to_json_file(map, "./Illegal_maps/illegal_json_" + str(i + 1) + ".json")
