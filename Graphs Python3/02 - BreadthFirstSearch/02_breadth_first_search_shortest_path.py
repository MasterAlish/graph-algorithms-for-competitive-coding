class Graph:
    def __init__(self, v):
        """
        In python we will use dict(hashmap) for adjacency list.
        """
        self.v = v
        self.adjacency_list = {i: [] for i in range(v)}

    def add_edge(self, from_node: int, to_node: int, is_undirected: bool = True):
        """
        is_undirected: if True from_node also will be added as adjacent for to_node
        """
        self.adjacency_list[from_node].append(to_node)

        if is_undirected:
            self.adjacency_list[to_node].append(from_node)

    def bfs(self, source: int, dest: int = None):
        queue = []  # in Python we will use list as queue
        visited = set()  # set of visited nodes
        parents = {}
        distance = {}

        queue.append(source)
        visited.add(source)
        parents[source] = source
        distance[source] = 0

        while queue:
            node = queue.pop(0)  # Get first item from queue and remove it from queue
            print(f"Visiting node {node}")

            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    distance[neighbor] = distance[node] + 1
                    parents[neighbor] = node

        # Print the shortest distance for each node from the source node
        for node in range(self.v):
            print(f"Shortest distance from node {source} to node {node} is {distance[node]}")

        if dest:
            # Print the shortest path from source to dest
            current = dest
            while current != source:
                print(current, "<--", end=" ")
                current = parents[current]

            print(source)


if __name__ == "__main__":
    graph = Graph(7)

    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 5)
    graph.add_edge(5, 6)
    graph.add_edge(4, 5)
    graph.add_edge(0, 4)
    graph.add_edge(3, 4)

    graph.bfs(1, 6)
