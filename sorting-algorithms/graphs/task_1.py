from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def fill_order(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.fill_order(i, visited, stack)
        stack.append(v)

    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def dfs(self, v, visited, scc):
        visited[v] = True
        scc.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, scc)

    def find_scc(self):
        stack = []
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.fill_order(i, visited, stack)

        reversed_graph = self.transpose()

        visited = [False] * self.V
        scc_list = []

        while stack:
            i = stack.pop()
            if not visited[i]:
                scc = []
                reversed_graph.dfs(i, visited, scc)
                scc_list.append(scc)

        return scc_list

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    scc = g.find_scc()
    print("Strongly Connected Components:")
    for component in scc:
        print(component)
