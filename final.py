from __future__ import print_function

import numpy as np
import pgmpy
from pgmpy.models import FactorGraph
from pgmpy.factors.discrete import DiscreteFactor
#Example User-Item Matrix

G = FactorGraph()


# Data Statistics
num_users = 700
num_targets = 9000

# Create nodes
user_nodes = []
for i in range(1,11):
    user_nodes.append('u' + str(i))

item_nodes = []
for i in range(1,11):
    item_nodes.append('i' + str(i))


#node_list = ['u1', 'u2', 'u3', 't1', 't2', 't3']
G.add_nodes_from(user_nodes)
G.add_nodes_from(item_nodes)

#Create Factors
g = []
h = []
f = []

for node in user_nodes:
    g.append(DiscreteFactor([node], [2], np.ones(2)))

for node in item_nodes:
    h.append(DiscreteFactor([node], [2], np.ones(2)))

for user in user_nodes:
    for item in item_nodes:
        f.append(DiscreteFactor([user,item], [2,2], np.ones([2,2])))

#Add factors to graph
for factor in g:
    G.add_factors(factor)
for factor in h:
    G.add_factors(factor)
for factor in f:
    G.add_factors(factor)

#Add edges
for idx in range(len(user_nodes)):
    G.add_edge(user_nodes[idx], g[idx])

for idx in range(len(item_nodes)):
    G.add_edge(item_nodes[idx], h[idx])
    G.add_edge(item_nodes[idx], f[idx])

for i in range(len(f)):
    for j in range(len(user_nodes)):
        G.add_edge(f[i], user_nodes[j])



# Rating matrix
R = [[3, 4, 5],
     [4, 3, 5],
     [2, 5, 4]]

#todo: 1) Change discrete factors to continuous factors! 2) Code rating bias, f, g, h