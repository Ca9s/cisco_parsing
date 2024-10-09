#!/usr/bin/env python

from pathlib import Path
import parse_cdp_neighbors
import graphviz
from itertools import chain

infiles = [
    "wds-acc-sw-1.txt",
    "wds-acc-sw-2.txt",
#    "sh_cdp_n_r2.txt",
#    "sh_cdp_n_r3.txt",
]

def create_network_map(filenames):
    path_body='/Users/andrey/Desktop/pylabbook/py_exercises_from_natenka_book/'
    file_paths=[Path(path_body)/ file_name for file_name in filenames]
    dict_total={}
    for each in file_paths:
         with open(each, 'r') as f:
            f=f.read()
            output=parse_cdp_neighbors.parse_cdp_neighbors(f)
            dict_total.update(output)
    return dict_total


def create_reversed_map(net_map):
    reversed_clear_map={}
    for left_device, right_device in net_map.items():
        if (right_device in reversed_clear_map.keys() and left_device in reversed_clear_map.values()):
            continue
        else:
            reversed_clear_map[left_device]=right_device  
    return reversed_clear_map

styles = {
    'graph': {
        'label': 'Network Map',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'box',
        'fontcolor': 'white',
        'color': '#006699',
        'style': 'filled',
        'fillcolor': '#006699',
        'margin': '0.4',
    },
    'edges': {
        'style': 'dashed',
        'color': 'green',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '10',
        'fontcolor': 'white',
    }
}
def draw_topology(topology, output_filename='topology'):
    nodes = set([key[0] for key in chain(topology.keys(), topology.values())])

    g = graphviz.Graph(format='png')

    for node in nodes:
        g.node(node)

    for key, value in topology.items():
        head, t_label = key
        tail, h_label = value
        g.edge(head, tail, headlabel=h_label, taillabel=t_label, label=" "*33)

    g.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    g.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    g.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )

    g.render(filename=output_filename)


if __name__ == "__main__":
    result=create_network_map(infiles)
#    print(result)
    print(create_reversed_map(result))
    clear_map=create_reversed_map(result)
    draw_topology(clear_map)
"""
if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
"""