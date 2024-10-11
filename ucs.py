from queue import PriorityQueue

def uniform_cost_search(start_node, goal_node, graph):
    frontier = PriorityQueue()
    frontier.put((0, start_node))  # (cost, node)
    
    explored = set()
    
    while not frontier.empty():
        current_cost, current_node = frontier.get()
        
        if current_node == goal_node:
            return current_cost
        
        explored.add(current_node)
        
        for neighbor, cost in graph[current_node].items():
            if neighbor not in explored:
                new_cost = current_cost + cost
                frontier.put((new_cost, neighbor))
    
    return -1  

def get_graph_input():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))  # Number of nodes
    
    for i in range(n):
        node = i  # Using numeric nodes (0, 1, 2, ...)
        graph[node] = {}
        
        num_edges = int(input(f"Enter the number of edges from node {node}: "))  # Number of edges
        
        for _ in range(num_edges):
            neighbor, cost = map(int, input("Enter neighbor and cost (format: neighbor cost): ").split())
            graph[node][neighbor] = cost
    
    return graph

if __name__ == "__main__":
    graph = get_graph_input()
    
    start_node = int(input("Enter the start node (as a number): "))  # Start node
    goal_node = int(input("Enter the goal node (as a number): "))  # Goal node
    
    result = uniform_cost_search(start_node, goal_node, graph)
    
    if result != -1:
        print(f"The cost from {start_node} to {goal_node} is: {result}")
    else:
        print(f"Failed to find a path from {start_node} to {goal_node}.")
