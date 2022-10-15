position_of = {1:(0,0), 2:(0,1), 3:(0,2),
               4:(1,0), 5:(1,1), 6:(1,2),
               7:(2,0), 8:(2,1)}

goal  = [[1,2,3],
         [4,5,6],
         [7,8,0]]

class Node:
    def __init__(self, data, level, f):
        self.data = data
        self.f = f
        self.level = 0
        self.N = len(data)
        self.prev = None

    def neighbors(self):
        neighbors = []
        N = self.N

        moves, (x,y) = self.find_moves()

        for i,j in moves:
            state = self.copy(self.data)
            state[x][y], state[i][j] = state[i][j], state[x][y]
            neighbors.append(Node(state, self.level+1, 0))

        return neighbors

    def copy(self, data):
        temp = []

        for i in data:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
        
    
    def find_blank(self, data):
        N = self.N

        for i in range(N):
            for j in range(N):
                if data[i][j] == 0:
                    return (i,j)

    def find_moves(self):
        x,y = self.find_blank(self.data)
        moves = []

        if (x != 0):
            moves.append((x-1,y))
        if (y != 0):
            moves.append((x,y-1))
        if (y != 2):
            moves.append((x,y+1))
        if (x != 2):
            moves.append((x+1,y))

        return moves, (x,y)

def heuristic(board, goal, heuristic_func):
    count = 0

    # Hamming Priority
    if heuristic_func=='hamming':
        for i in range(3):
            for j in range(3):
                if board[i][j] and board[i][j] != goal[i][j]:
                    count += 1

    # Manhattan Distance
    elif heuristic_func=='manhattan':
        for i in range(3):
            for j in range(3):
                if board[i][j]:
                    x,y = position_of[board[i][j]]
                    manhattan = abs(x-i) + abs(y-j)
                    count += manhattan

    return count

def getPath():
    path = []
    temp = curr

    while temp.prev:
        path.insert(0, temp.data)
        temp = temp.prev

    path.insert(0, temp.data)

    return path

curr = None
def solve(start, heuristic_func):
    global curr

    openSet = []
    closedSet = []

    start = Node(start, 0, 0)
    start.f = heuristic(start.data, goal, heuristic_func) + start.level
    openSet.append(start)

    while len(openSet) > 0:
        low = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[low].f:
                low = i
                
        curr = openSet[low]

        if heuristic(curr.data, goal, heuristic_func) == 0:
            break

        closedSet.append(curr.data)
        openSet.remove(curr)

        for neighbor in curr.neighbors():
            if neighbor.data not in closedSet:
                # f(x) = g(x) + h(x)
                h_x = heuristic(neighbor.data, goal, heuristic_func)
                g_x = neighbor.level
                neighbor.f = g_x + h_x
                openSet.append(neighbor)
                neighbor.prev = curr


    return getPath()

def print_solution(board):
    for step in solution:
        for row in step:
            print(row)
        print()
    
    print("Total Steps:",len(solution))

    
board = [[2,0,3],
         [5,8,1],
         [6,7,4]]
solution = solve(board, heuristic_func='manhattan')
print_solution(solution)
