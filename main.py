import matplotlib.pyplot as plt
import networkx as nx
from  graph import Graph

graph = Graph()

# Inisialisasi Jalur Huruf (Menggunakan array)
my_vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
for vertex in my_vertices:
    graph.add_vertex(vertex)

# Operator yang digunakan (Mendeklarasikan jarak antara huruf pada variable my_vertices menggunakan array)
graph.add_edge('A', 'B') # jarak 1
graph.add_edge('A', 'C') # jarak 1
graph.add_edge('A', 'D') # jarak 1
graph.add_edge('C', 'D') # jarak 1
graph.add_edge('C', 'G') # jarak 1
graph.add_edge('D', 'G') # jarak 1
graph.add_edge('D', 'H') # jarak 1
graph.add_edge('B', 'E') # jarak 1
graph.add_edge('B', 'F') # jarak 1
graph.add_edge('E', 'I') # jarak 1

# Fungsi untuk membuat visualisasi grafik
def draw_graph(graph):
    G = nx.Graph()
    for vertex, neighbours in graph.adjacency_list.items():
        for neighbour in neighbours:
            G.add_edge(vertex, neighbour)
    pos = nx.spring_layout(G)  # Layout graph
    nx.draw(G, pos, with_labels=True)  # Draw graph
    plt.show()

# Memanggil fungsi BFS (Initial state)
graph.bfs("A")

# Menampilkan jalur tujuan (goal state) 
print(graph.return_path("I"))

# Memanggil fungsi untuk membuat visualisasi grafik
draw_graph(graph)
