import random
import string
from dump_to_file import *

# Generate a random 1 - 50 character alphanumeric string
def generate_random_string():
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))

    return generated_str


# Generate a good element of the map
# Good elements are a (key, value) pair where key does not already exist in the map
def good_element(keys):
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


# Generate an element with a duplicate key and legal value
def duplicate_key_legal_value(keys):
    keys_len = len(keys)    
    random_idx = random.randint(0, keys_len - 1)

    random_element = keys[random_idx]
    new_random_value = generate_random_string()

    if len(random_element) == 2:
        random_element = keys[random_idx][0]

    return (random_element, new_random_value)


# Generate an element with a duplicate key and null value
def duplicate_key_null_value(keys):
    keys_len = len(keys)
    random_idx = random.randint(0, keys_len - 1)

    random_element = keys[random_idx]

    if len(random_element) == 2:
        random_element = keys[random_idx][0]

    return (random_element, None)


# Generate an element with a unique key and null value (the element is just a key, not a (key, value) pair)
def unique_key_null_value(keys):
    generated_key = None
    key_already_exists = True

    while key_already_exists:
        generated_key = generate_random_string()

        key_in_map = False
        for key in keys:
            if generated_key == key:
                key_in_map = True

        key_already_exists = key_in_map

    return (generated_key, None)


# Generate an element with a null key and legal value
def null_key_legal_value():
    value = generate_random_string()

    return (None, value)


# Generate an element with null key and null value
def null_key_null_value():
    return (None, None)


# Generate a map
def generate_illegal_map(error_type):
    # Generate a random map size from 0 - 500. 
    # Allowing empty maps captures the nullary list property from TADT
    map_size = random.randint(0, 500)
    keys = []
    map = []
    pair_to_append = None

    # Half the map will be legal (key, value) pairs
    for i in range(0, int(map_size * 0.5)):
        pair_to_append = good_element()
        map.append(pair_to_append)
        keys.append[pair_to_append[0]]

    
    # The rest of the map will be erroneous (key, value) pairs
    # Iteratively generate each (key, value) pair
    for i in range(int(map_size * 0.5) + 1, map_size):
        # Generate an element with a duplicate key and legal value
        if error_type == 2:
            pair_to_append = duplicate_key_legal_value(keys)

        # Generate an element whose key is duplicate and value is null
        elif error_type == 3:
            pair_to_append = duplicate_key_null_value(keys)

        # Generate an element with a unique key and null value
        elif error_type == 4:
            pair_to_append = unique_key_null_value(keys)

        # Generate an element with a null key and legal value
        elif error_type == 5:
            pair_to_append = null_key_legal_value()

        # Generate an element with null key and null value
        elif error_type == 6:
            pair_to_append = null_key_null_value()

        map.append(pair_to_append)
        keys.append(pair_to_append[0])



    return map
