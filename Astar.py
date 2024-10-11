import heapq

def astar(graph, start, goal, heuristic):
    frontier = [(heuristic[start], start)]
    explored = set()
    cost = {start: 0}
    path = {start: None}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            return reconstruct_path(path, current)

        explored.add(current)
        
        for neighbor in graph[current]:
            new_cost = cost[current] + graph[current][neighbor]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (priority, neighbor))
                path[neighbor] = current
                
    return None

def reconstruct_path(path, current):
    result = []
    while current is not None:
        result.append(current)
        current = path[current]
    return result[::-1]

def get_graph_and_heuristic():
    graph = {}
    heuristic = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for _ in range(num_nodes):
        node = int(input("Enter node (as a number): "))
        heuristic[node] = int(input(f"Heuristic for {node}: "))
        neighbors = input(f"Neighbors for {node} (format: 2:5,3:10): ").split(',')
        graph[node] = {int(n.split(':')[0].strip()): int(n.split(':')[1]) for n in neighbors}
    return graph, heuristic

if __name__ == "__main__":
    graph, heuristic = get_graph_and_heuristic()
    start = int(input("Start node: "))
    goal = int(input("Goal node: "))
    path = astar(graph, start, goal, heuristic)
    print("Shortest path:", " -> ".join(map(str, path)) if path else "No path found.")
