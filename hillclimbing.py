import random

def hill_climbing_search(f, neighbor_fn, max_iter=1000):
    # Step 2: Initialize the current state as a random starting point.
    current = random.choice(x_range)
    
    for i in range(max_iter):
        # Step 4: Generate a set of possible next states.
        neighbors = neighbor_fn(current)
        
        # Step 5: Evaluate the objective function for each of the possible next states.
        next_neighbor = max(neighbors, key=lambda x: f(x))
        
        # Step 6: Select the next state with the highest objective function value.
        if f(next_neighbor) <= f(current):
            break  # Stopping criterion
            
        current = next_neighbor
        
    return current, f(current)  # Step 8: Return the final state and its value.

def f(x):
    return -x**2  # Example objective function to maximize (we are maximizing -x^2)

def neighbor_fn(x):
    return [x + dx for dx in [-0.1, 0, 0.1] if (x + dx) in x_range]  # Generate neighbors

if __name__ == "__main__":
    x_start = float(input("Enter the starting point for x (between 0 and 10): "))
    x_end = float(input("Enter the ending point for x (between 0 and 10): "))
    
    x_range = [round(x, 1) for x in [i * 0.1 for i in range(int(x_start * 10), int(x_end * 10) + 1)]]

    best_solution, best_value = hill_climbing_search(f, neighbor_fn)
    
    print("Best solution: x =", best_solution, "Best value: f(x) =", -best_value)
