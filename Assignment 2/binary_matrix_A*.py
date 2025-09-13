def a_star_search(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    start, goal = (0,0), (n-1,n-1)
    open_set = [(heuristic(start, goal), 0, start, [start])]  # (f, g, node, path)
    visited = {}

    while open_set:
        f, g, (x,y), path = heapq.heappop(open_set)

        if (x,y) in visited and visited[(x,y)] <= g:
            continue
        visited[(x,y)] = g

        if (x,y) == goal:
            return len(path), path

        for dx,dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                new_g = g + 1
                new_f = new_g + heuristic((nx,ny), goal)
                new_path = path + [(nx,ny)]
                heapq.heappush(open_set, (new_f, new_g, (nx,ny), new_path))

    return -1, []
