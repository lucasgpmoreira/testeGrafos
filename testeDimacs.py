from scipy.io import mmread
import networkx as nx
import matplotlib.pyplot as plt

# Load the sparse matrix from Matrix Market format
a = mmread('inf-USAir97.mtx')

# Convert the sparse matrix to a NetworkX graph
graph = nx.Graph(a)

# Plot the graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=False, node_size=10, node_color='blue', edge_color='gray', alpha=0.5)
plt.title('Graph Visualization')
plt.show()
