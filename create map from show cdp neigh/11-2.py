from pathlib import Path
import parse_cdp_neighbors
infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def create_network_map(filenames):
    path_body='/Users/andrey/Desktop/NEWVENEV_PY/py_exercises_from_natenka_book/'
    file_paths=[Path(path_body)/ file_name for file_name in filenames]
    dict_total={}
    for each in file_paths:
         with open(each, 'r') as f:
            f=f.read()
            output=parse_cdp_neighbors.parse_cdp_neighbors(f)
            dict_total.update(output)
    return dict_total

if __name__ == "__main__":
    print(create_network_map(infiles))

"""
if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
"""