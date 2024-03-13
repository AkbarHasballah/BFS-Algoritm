import matplotlib.pyplot as plt
import networkx as nx
from  graph import Graph

graph = Graph()

# Inisialisasi Jalur Huruf (Menggunakan array)
my_vertices = ['sarijadi', 'surya sumantri', 'cibogo', 'pasteur', 'gerlong', 'dr.setiabudi', 'lemah neundeut', 'Sukajadi', 'sukagalih']
for vertex in my_vertices:
    graph.add_vertex(vertex)

# Operator yang digunakan (Mendeklarasikan jarak antara huruf pada variable my_vertices menggunakan array)
graph.add_edge('sarijadi', 'surya sumantri') # jarak 1
graph.add_edge('sarijadi', 'cibogo') # jarak 1
graph.add_edge('sarijadi', 'pasteur') # jarak 1
graph.add_edge('cibogo', 'pasteur') # jarak 1
graph.add_edge('cibogo', 'lemah neundeut') # jarak 1
graph.add_edge('pasteur', 'lemah neundeut') # jarak 1
graph.add_edge('pasteur', 'Sukajadi') # jarak 1
graph.add_edge('surya sumantri', 'gerlong') # jarak 1
graph.add_edge('surya sumantri', 'dr.setiabudi') # jarak 1
graph.add_edge('gerlong', 'sukagalih') # jarak 1

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
graph.bfs("pasteur")

# Menampilkan jalur tujuan (goal state) 
print(graph.return_path("gerlong"))

# Memanggil fungsi untuk membuat visualisasi grafik
draw_graph(graph)
