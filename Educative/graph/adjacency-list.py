class Graph:
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, v, e):
        self.adj_list[v].append(e)
        self.adj_list[e].append(v)

    def print_adj(self):
        for node in self.nodes:
            print(node, ":", self.adj_list[node])


edges = [
    ("a", "b"),
    ("a", "c"),
    ("b", "c"),
    ("b", "d"),
]
nodes = ["a", "b", "c", "d"]
graph = Graph(nodes)
for v, e in edges:
    graph.add_edge(v, e)

graph.print_adj()
