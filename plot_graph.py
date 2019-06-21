import networkx as nx
import pylab
import matplotlib.pyplot as plt
import numpy as np

Graph = nx.DiGraph()

for i in range(1,7):
    Graph.add_node(str(i))

Graph.add_edge('1','2')
Graph.add_edge('1','3')
Graph.add_edge('1','4')

Graph.add_edge('2','1')
Graph.add_edge('2','3')

Graph.add_edge('3','5')

Graph.add_edge('4','2')
Graph.add_edge('4','3')
Graph.add_edge('4','5')

Graph.add_edge('5','2')

Graph.add_edge('6','4')
Graph.add_edge('6','5')


nx.draw(Graph, with_labels=True)
plt.show()