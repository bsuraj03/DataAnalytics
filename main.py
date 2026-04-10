import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic (estimated cost to goal)
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    """Calculate Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(position, grid):
    """Returns valid neighbors (not obstacles or out of bounds)."""
    rows, cols = len(grid), len(grid[0])
    x, y = position
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0]

def reconstruct_path(current):
    """Backtracks from goal to start to retrieve the path."""
    path = []
    while current:
        path.append(current.position)
        current = current.parent
    return path[::-1]

def a_star(grid, start, goal):
    """Performs the A* search algorithm."""
    open_set = []
    heapq.heappush(open_set, Node(start, None, 0, heuristic(start, goal)))
    visited = set()

    while open_set:
        current = heapq.heappop(open_set)

        if current.position in visited:
            continue
        visited.add(current.position)

        if current.position == goal:
            return reconstruct_path(current)

        for neighbor in get_neighbors(current.position, grid):
            if neighbor in visited:
                continue
            g_cost = current.g + 1
            h_cost = heuristic(neighbor, goal)
            heapq.heappush(open_set, Node(neighbor, current, g_cost, h_cost))

    return None  # No path found

def print_grid(grid, path=None, start=None, goal=None):
    """Prints the grid with obstacles, path, start, and goal."""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif path and (i, j) in path:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# User Interaction
def main():
    rows = int(input("Enter grid rows: "))
    cols = int(input("Enter grid columns: "))
    grid = [[0] * cols for _ in range(rows)]

    print("Enter obstacle positions as 'row col' (enter 'done' to finish):")
    while True:
        data = input("> ")
        if data.lower() == "done":
            break
        try:
            x, y = map(int, data.split())
            grid[x][y] = 1
        except:
            print("Invalid input. Enter row and column as numbers.")

    start = tuple(map(int, input("Enter start position (row col): ").split()))
    goal = tuple(map(int, input("Enter goal position (row col): ").split()))

    path = a_star(grid, start, goal)

    print("\nFinal Grid:")
    print_grid(grid, path, start, goal)

    if path:
        print("Shortest Path:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
