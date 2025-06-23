# DFS 구현 (재귀 방식)
def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")  # 방문한 노드 출력
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# DFS 구현 (스택 방식)
def dfs_stack(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")  # 방문한 노드 출력
            stack.extend(reversed(graph[node]))  # 인접 노드 스택에 추가

import heapq

def dijkstra(graph, start):
    # 최단 거리 테이블 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (거리, 노드) 우선순위 큐

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 현재 노드까지의 거리가 기존 거리보다 크다면 무시
        if current_distance > distances[current_node]:
            continue

        # 인접 노드 확인
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 더 짧은 경로 발견 시 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 예제 그래프 (인접 리스트 표현)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 8},
    'D': {'B': 10, 'C': 3, 'E': 6},
    'E': {'C': 8, 'D': 6}
}

# 실행 예제
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print("최단 경로:", shortest_paths)