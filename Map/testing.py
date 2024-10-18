from dump_to_file import *
from generate_legal_map import *
from generate_illegal_map import *


for i in range(0, 5):
    map = generate_legal_map()
    filepath = "./Legal_Maps/" + str(i + 1)
    dump_to_json_file(map, filepath)


    map = generate_illegal_map(i + 2)
    filepath = "./Ilegal_Maps/" + str(i + 1)
    dump_to_json_file(map, filepath)
