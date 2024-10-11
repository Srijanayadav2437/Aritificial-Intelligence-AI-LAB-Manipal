def valid(state):
    m_left, c_left = state[0]
    m_right, c_right = state[1]
    return (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right)

def successors(state):
    children = []
    for i in range(3):  # Move 1 or 2 missionaries
        for j in range(3):  # Move 1 or 2 cannibals
            if 1 <= i + j <= 2:
                new_state = (
                    (state[0][0] - i, state[0][1] - j) if state[2] else (state[0][0] + i, state[0][1] + j),
                    (state[1][0] + i, state[1][1] + j) if state[2] else (state[1][0] - i, state[1][1] - j),
                    1 - state[2]
                )
                if valid(new_state):
                    children.append(new_state)
    return children

def bfs(start, goal):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for child in successors(node):
            if child not in visited:
                visited.add(child)
                queue.append(path + [child])
    return []

def main():
    initial_m = int(input("Missionaries on initial side: "))
    initial_c = int(input("Cannibals on initial side: "))
    goal_m = int(input("Missionaries on goal side: "))
    goal_c = int(input("Cannibals on goal side: "))
    initial = ((initial_m, initial_c), (0, 0), 1)
    goal = ((goal_m, goal_c), (initial_m - goal_m, initial_c - goal_c), 0)
    
    path = bfs(initial, goal)
    if path:
        print("Solution path:")
        for state in path:
            print(state)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
