import networkx as nx
import pylab
import matplotlib.pyplot as plt
import numpy as np

#グラフオブジェクトの作成
G = nx.Graph()

N, M, P, Q = tuple(map(int, input().split()))

pos = {}
for k in range(1,N+1):
    G.add_node(str(k))
    pos[str(k)] = tuple(map(int, input().split()))

for k in range(1, M+1):
    edge1, edge2 = input().split()
    G.add_edge(edge1, edge2)



plt.axis('on')
nx.draw(G,pos,with_labels=True)
plt.axis('on')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(color='lightgray', linestyle=':')
plt.tick_params(labelbottom=True,
                labelleft=True)
# plt.xticks()
plt.savefig("test_fig.png")
plt.show()
