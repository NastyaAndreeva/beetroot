def floyd_warshall(graph):
    V = len(graph)
    
    dist = [[float('inf')] * V for _ in range(V)]
    
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif (i, j) in graph:
                dist[i][j] = graph[(i, j)]
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

if __name__ == "__main__":
    graph = {
        (0, 1): 3,
        (0, 2): 6,
        (1, 0): 2,
        (1, 2): 7,
        (2, 0): 5,
        (2, 1): 4
    }

    shortest_paths = floyd_warshall(graph)
    for i in range(len(shortest_paths)):
        for j in range(len(shortest_paths[i])):
            print(f"Shortest distance from vertex {i} to {j}: {shortest_paths[i][j]}")
