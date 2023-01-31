from typing import List, Dict


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []


class Graph:
    def __init__(self, cities):
        """
        In python we will use dict(hashmap) for adjacency list.
        """
        self.adjacency_list: Dict[str, Node] = {city: Node(city) for city in cities}

    def add_edge(self, from_city: str, to_city: str, is_undirected: bool = False):
        """
        is_undirected: if True from_city also will be added as adjacent for to_city
        """
        self.adjacency_list[from_city].neighbors.append(to_city)

        if is_undirected:
            self.adjacency_list[to_city].neighbors.append(from_city)

    def print_adjacency_list(self):
        for node in self.adjacency_list.values():
            print(node.name, "-->", ",".join(node.neighbors))


if __name__ == "__main__":
    graph = Graph(["Delhi", "London", "Paris", "New York"])

    graph.add_edge("Delhi", "London")
    graph.add_edge("New York", "London")
    graph.add_edge("Delhi", "Paris")
    graph.add_edge("Paris", "New York")

    graph.print_adjacency_list()
