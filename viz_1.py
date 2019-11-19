import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import networkx as nx
from os import listdir
from os.path import isfile, join
import pandas as pd

DATADIR = "P:\Python\Project\Data_Viz\data"

Z = []
G = nx.Graph()

def readFile(file):
    keys = []
    values = []
    with open(file) as f:
        list_of_edges = [line.split() for line in f]
    for edge in list_of_edges:
        if([int(edge[1]), int(edge[0])] not in Z and ([int(edge[0]), int(edge[1])] not in Z)):
            Z.append([int(edge[0]), int(edge[1])])
            G.add_edge(int(edge[0]), int(edge[1]))
            keys.append(int(edge[0]))
            values.append(int(edge[1]))
    return keys, values
            
    

keys, values = readFile("common_columns.txt")
fig, ax = plt.subplots()
ax.scatter(keys, values, alpha=0.5)
x_labels = [_file for _file in listdir(DATADIR) if isfile(join(DATADIR, _file))]
print(x_labels)
ax.set_yticklabels(x_labels)
ax.set_xticklabels(x_labels)
plt.xticks(rotation=90)


ax.grid(True, markevery = 1)
fig.tight_layout()
plt.show()


pos=nx.spring_layout(G)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G, nlist=[range(50, 100), range(50)], with_labels=True, font_weight='bold', node_color=range(50), node_size=800, cmap=plt.cm.Blues)
plt.show()
# print(Z)

