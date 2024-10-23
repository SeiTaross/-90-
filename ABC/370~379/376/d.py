import sys
import io

_INPUT = """\
6 9
6 1
1 5
2 6
2 1
3 6
4 2
6 4
3 5
5 4

"""

sys.stdin = io.StringIO(_INPUT)

from collections import defaultdict

def find_min_cycle(n, m, edges):
    
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)

    min_cycle_length = float('inf')

    def dfs(current, start, visited, depth):
        nonlocal min_cycle_length
        if depth > 0 and current == start:
            min_cycle_length = min(min_cycle_length, depth)
            return
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor, start, visited, depth + 1)
                visited.remove(neighbor)
            elif neighbor == start and depth > 0:
                min_cycle_length = min(min_cycle_length, depth + 1)

    visited = set([1])
    dfs(1, 1, visited, 0)

    return min_cycle_length if min_cycle_length != float('inf') else -1

n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

result = find_min_cycle(n, m, edges)
print(result)
