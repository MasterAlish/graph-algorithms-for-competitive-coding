class Graph:
    def __init__(self, v):
        """
        In python we will use dict(hashmap) for adjacency list.
        """
        self.v = v
        self.adjacency_list = {i: [] for i in range(v)}

    def add_edge(self, from_node: int, to_node: int, is_undirected: bool = False):
        """
        is_undirected: if True from_node also will be added as adjacent for to_node
        """
        self.adjacency_list[from_node].append(to_node)

        if is_undirected:
            self.adjacency_list[to_node].append(from_node)

    def print_adjacency_list(self):
        for node, adjacent_nodes in self.adjacency_list.items():
            adjacent_nodes_as_str = [str(n) for n in adjacent_nodes]
            print(node, "-->", ",".join(adjacent_nodes_as_str))


if __name__ == "__main__":
    graph = Graph(6)

    graph.add_edge(0, 1, True)
    graph.add_edge(0, 4, True)
    graph.add_edge(2, 1, True)
    graph.add_edge(3, 4, True)
    graph.add_edge(4, 5, True)
    graph.add_edge(2, 3, True)
    graph.add_edge(3, 5, True)

    graph.print_adjacency_list()
