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

            if not key_in_map:
                key_already_exists = False

        generated_value = generate_random_string()
        map.append((generated_key, generated_value))
        keys.append(generated_key)

    return map
