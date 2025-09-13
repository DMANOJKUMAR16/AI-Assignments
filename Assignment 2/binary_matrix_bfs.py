import heapq
import math

 
directions = [(-1,-1), (-1,0), (-1,1),
              (0,-1),          (0,1),
              (1,-1),  (1,0),  (1,1)]

def heuristic(a, b):
 
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def best_first_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    start, goal = (0,0), (n-1,n-1)
    visited = set()
    pq = [(heuristic(start, goal), start, [start])]  # (priority, node, path)

    while pq:
        _, (x, y), path = heapq.heappop(pq)
        if (x,y) in visited:
            continue
        visited.add((x,y))

        if (x,y) == goal:
            return len(path), path

        for dx,dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0 and (nx,ny) not in visited:
                new_path = path + [(nx,ny)]
                heapq.heappush(pq, (heuristic((nx,ny), goal), (nx,ny), new_path))

    return -1, []
