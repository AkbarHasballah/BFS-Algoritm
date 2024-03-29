from queue import Queue

class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacency_list: dict = {}
        self.prev: dict = {}
        self.distance: dict = {}
        self.colors: dict = {}

    def add_vertex(self, label: str):
        self.vertices.append(label)
        self.adjacency_list[label]: list = []
        self.prev[label] = None
        self.distance[label] = 0
        self.colors[label] = "white"

    def add_edge(self, label1: str, label2: str):
        if label1 not in self.adjacency_list:
            self.add_vertex(label1)
        if label2 not in self.adjacency_list:
            self.add_vertex(label2)
        self.adjacency_list[label1].append(label2)
        self.adjacency_list[label2].append(label1)

    def bfs(self, label: str):
        q = Queue()
        q.enqueue(label)
        self.colors[label] = "gray"
        while not q.is_empty():
            tmp = q.dequeue()
            for neighbour in self.adjacency_list[tmp]:
                if self.colors[neighbour] == "white":
                    self.prev[neighbour] = tmp
                    self.distance[neighbour] = self.distance[tmp] + 1
                    self.colors[neighbour] = "gray"
                    q.enqueue(neighbour)
            self.colors[tmp] = "black"

    def return_path(self, label: str) -> str:
        if self.prev[label] is None:
            return label
        else:
            return self.return_path(self.prev[label]) + " -> " + label