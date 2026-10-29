import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    h = 0

    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            h += abs(i // 3 - j // 3)
            h += abs(i % 3 - j % 3)

    return h


def astar(start):
    queue = [(heuristic(start), 0, start)]
    visited = set()
    parent = {start: None}

    while queue:
        f, g, state = heapq.heappop(queue)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]

            for state in reversed(path):
                print(state[:3])
                print(state[3:6])
                print(state[6:9])
                print()
            return

        zero = state.index(0)

        for move in [-3, 3, -1, 1]:
            new_pos = zero + move

            if not 0 <= new_pos < 9:
                continue

            if move == -1 and zero % 3 == 0:
                continue

            if move == 1 and zero % 3 == 2:
                continue

            new_state = list(state)
            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                parent[new_state] = state
                heapq.heappush(
                    queue,
                    (g + 1 + heuristic(new_state), g + 1, new_state)
                )


astar(start)