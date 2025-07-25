class State:
    def __init__(self, amogh, ameya, grandmother, grandfather, umbrella='L', time=0):
        self.amogh = amogh
        self.ameya = ameya
        self.grandmother = grandmother
        self.grandfather = grandfather
        self.umbrella = umbrella
        self.time = time

    def goalTest(self):
        return (self.amogh == self.ameya == self.grandmother == self.grandfather == 'R' and self.time <= 60)

    def moveGen(self):
        children = []
        new_side = 'R' if self.umbrella == 'L' else 'L'
        items = {
            "amogh": 5,
            "ameya": 10,
            "grandmother": 20,
            "grandfather": 25
        }

        current_side_people = []
        for item in items:
            if getattr(self, item) == self.umbrella:
                current_side_people.append(item)

        if self.umbrella == 'L':
            moves = [(current_side_people[i], current_side_people[j])
                     for i in range(len(current_side_people))
                     for j in range(i + 1, len(current_side_people))]
        else:
            
            moves = [(p,) for p in current_side_people]

        for move in moves:
            new_amogh = self.amogh
            new_ameya = self.ameya
            new_grandmother = self.grandmother
            new_grandfather = self.grandfather

            for person in move:
                if person == "amogh":
                    new_amogh = new_side
                elif person == "ameya":
                    new_ameya = new_side
                elif person == "grandmother":
                    new_grandmother = new_side
                elif person == "grandfather":
                    new_grandfather = new_side

            new_time = self.time + max(items[p] for p in move)

    
            if new_time <= 60:
                child = State(
                    new_amogh,
                    new_ameya,
                    new_grandmother,
                    new_grandfather,
                    umbrella=new_side,
                    time=new_time
                )
                children.append(child)

        return children

    def __eq__(self, other):
        return (self.amogh == other.amogh and
                self.ameya == other.ameya and
                self.grandmother == other.grandmother and
                self.grandfather == other.grandfather and
                self.umbrella == other.umbrella and
                self.time == other.time)

    def __hash__(self):
        return hash((self.amogh, self.ameya, self.grandmother, self.grandfather, self.umbrella, self.time))


def removeSeen(children, OPEN, CLOSED):
    open_nodes = [node for node, parent in OPEN]
    closed_nodes = [node for node, parent in CLOSED]
    new_nodes = [node for node in children if node not in open_nodes and node not in closed_nodes]
    return new_nodes


def reconstructPath(node_pair, CLOSED):
    parent_map = {}
    for node, parent in CLOSED:
        parent_map[node] = parent
    N, parent = node_pair
    path = [N]

    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]

    path.reverse()
    for e in path:
        print("amogh =", e.amogh, "ameya =", e.ameya, "grandmother =", e.grandmother,  "grandfather =", e.grandfather, "umbrella =", e.umbrella, "time =", e.time)

    return path


def bfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair
        if N.goalTest():
            print("Goal is found (BFS):")
            path = reconstructPath(node_pair, CLOSED)
            return path
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN = OPEN + new_pairs
    print("No solution found using BFS.")
    return []


def dfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair
        if N.goalTest():
            print("Goal is found (DFS):")
            path = reconstructPath(node_pair, CLOSED)
            return path
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN = new_pairs + OPEN
    print("No solution found using DFS.")
    return []

start_state = State(amogh='L', ameya='L', grandmother='L', grandfather='L')

print("BFS Solution:")
bfs(start_state)
print("\nDFS Solution:")
dfs(start_state)