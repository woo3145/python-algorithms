from collections import deque, defaultdict

# 그래프 (Graph)

graph = defaultdict(list) # 없는 key에 접근하면 Error 대신 default 값을 반환/사용
graph['A'].extend(['B', 'C'])
graph['B'].append('A')
graph['B'].append('D')
graph['C'].extend(['A', 'D'])
graph['D'].extend(['B', 'C'])

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("Graph DFS:", end=" ")
dfs(graph, 'A')  # A B D C
print()
print("Graph BFS:", end=" ")
bfs(graph, 'A')  # A B C D
print()