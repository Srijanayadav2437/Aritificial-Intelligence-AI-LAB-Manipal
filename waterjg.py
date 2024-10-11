def solve(jug_sizes, target, start=(0, 0)):
    stack = [(start, [start])]  # Store state and the path taken
    explored = set()
    
    while stack:
        current, path = stack.pop()  # Get the current state and path
        if target in current:
            return path  # Return the full path to the target
        
        explored.add(current)
        jug1, jug2 = current
        jug1_cap, jug2_cap = jug_sizes
        
        successors = [
            (jug1_cap, jug2),  # Fill jug 1
            (jug1, jug2_cap),  # Fill jug 2
            (0, jug2),         # Empty jug 1
            (jug1, 0),         # Empty jug 2
            (jug1 - min(jug1, jug2_cap - jug2), jug2 + min(jug1, jug2_cap - jug2)),  # Pour jug 1 into jug 2
            (jug1 + min(jug2, jug1_cap - jug1), jug2 - min(jug2, jug1_cap - jug1))   # Pour jug 2 into jug 1
        ]
        
        # Extend the stack with successors and their respective paths
        for s in successors:
            if s not in explored:
                stack.append((s, path + [s]))  # Append new state and updated path
    
    return None  # No solution found

if __name__ == "__main__":
    jugs = (int(input("Jug 1 capacity: ")), int(input("Jug 2 capacity: ")))
    target = int(input("Target volume: "))
    path = solve(jugs, target)
    print("Path to target volume:" if path else "No solution found.")
    print(path)
