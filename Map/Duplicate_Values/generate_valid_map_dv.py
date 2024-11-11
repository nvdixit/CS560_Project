import random
import string

# Generate a random 1 - 50 character alphanumeric string
def generate_random_string():
    str_len = random.randint(1, 50)
    generated_str = ''.join(random.choices(string.ascii_letters, k=str_len))

    return generated_str


# Generate a legal map
def generate_valid_map_dv():
    # Generate a random map size from 0 - 500. 
    # Allowing empty maps captures the nullary list property from TADT
    map_size = random.randint(0, 500)

    map = []

    # Iteratively generate each (key, value) pair
    for i in range(0, map_size):
        generated_key = None
        generated_value = None
        already_exists = True

        while already_exists:
            generated_key = generate_random_string()
            generated_value = generate_random_string()

            key_or_val_in_map = False
            for pair in map:
                if generated_key == pair[0]:
                    key_or_val_in_map = True
                
                if generated_value == pair[1]:
                    key_or_val_in_map = True

            if not key_or_val_in_map:
                already_exists = False
        
        map.append((generated_key, generated_value))

    return map
