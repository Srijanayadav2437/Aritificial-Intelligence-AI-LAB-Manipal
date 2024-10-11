def dfs_hill_climbing(f, neighbor_fn, current, visited, max_depth=1000, depth=0):

    if depth > max_depth:
        return current, f(current)  # Return if maximum depth is reached
    
    visited.add(current)  # Mark the current state as visited
    neighbors = neighbor_fn(current)  # Generate neighbors

    # Filter unvisited neighbors
    neighbors = [n for n in neighbors if n not in visited]
    
    # If no neighbors are left, return the current state
    if not neighbors:
        return current, f(current)

    # Sort neighbors by the value of the objective function in descending order
    neighbors.sort(key=lambda x: f(x), reverse=True)

    # Explore the best neighbor that improves the objective function
    for next_state in neighbors:
        if f(next_state) > f(current):  # Only recurse if it improves the solution
            best_solution, best_value = dfs_hill_climbing(f, neighbor_fn, next_state, visited, max_depth, depth + 1)
            return best_solution, best_value
    
    # If no better neighbor was found, return the current solution
    return current, f(current)

# Example usage:

def f(x):
    return -x**2  # Example objective function to maximize (maximize -x^2, peak at x=0)

def neighbor_fn(x):
    return [x + dx for dx in [-0.1, 0, 0.1] if (x + dx) in x_range]  # Generate neighbors

if __name__ == "__main__":
    x_start = float(input("Enter the starting point for x (between 0 and 10): "))
    x_end = float(input("Enter the ending point for x (between 0 and 10): "))
    
    x_range = [round(x, 1) for x in [i * 0.1 for i in range(int(x_start * 10), int(x_end * 10) + 1)]]

    start_state = random.choice(x_range)
    visited = set()  # Keep track of visited states

    best_solution, best_value = dfs_hill_climbing(f, neighbor_fn, start_state, visited)
    
    print("Best solution: x =", best_solution, "Best value: f(x) =", -best_value)
