import random
import string
from dump_to_file import *

# Generate a random 1 - 50 character alphanumeric string
def generate_random_string():
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))

    return generated_str


# Generate a legal map
def generate_legal_map():
    # Generate a random map size from 0 - 500. 
    # Allowing empty maps captures the nullary list property from TADT
    map_size = random.randint(0, 500)
    keys = []

    map = []

    # Iteratively generate each (key, value) pair
    for i in range(0, map_size):
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
        map.append((generated_key, generated_value))

    return map


for i in range(0, 5):
    map = generate_legal_map()
    dump_to_json_file(map, "./Legal_maps/legal_json_" + str(i + 1) + ".json")
