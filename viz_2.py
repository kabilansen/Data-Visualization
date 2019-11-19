import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()



def readFile(file):
    with open(file) as f:
        list_of_edges = [line.split() for line in f]
    for edge in list_of_edges:
        G.add_edge(int(edge[0]), int(edge[1]))


readFile("common_columns.txt")




pos=nx.spring_layout(G)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G, nlist=[range(50, 100), range(50)], with_labels=True, font_weight='bold', node_color=range(50), node_size=800, cmap=plt.cm.Blues)
plt.show()