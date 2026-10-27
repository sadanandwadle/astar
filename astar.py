import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            target = goal.index(state[i])
            distance += abs(i // 3 - target // 3)
            distance += abs(i % 3 - target % 3)

    return distance

queue = [(0, start)]
cost = {start: 0}
parent = {start: None}

while queue:
    f, current = heapq.heappop(queue)

    if current == goal:
        break

    for i in range(9):
        if current[i] == 0:
            break

    for move in [-3, 3, -1, 1]:
        j = i + move

        if j < 0 or j >= 9:
            continue

        if abs(i % 3 - j % 3) > 1:
            continue

        new = list(current)
        new[i], new[j] = new[j], new[i]
        new = tuple(new)

        new_cost = cost[current] + 1

        if new not in cost or new_cost < cost[new]:
            cost[new] = new_cost
            parent[new] = current
            heapq.heappush(
                queue,
                (new_cost + heuristic(new), new)
            )

path = []
state = goal

while state is not None:
    path.append(state)
    state = parent.get(state)

path.reverse()

for state in path:
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()