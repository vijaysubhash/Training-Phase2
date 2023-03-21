def BFS(graph, start):
    q = [start]
    visited = [start]
    while len(q) != 0:
        ele = q.pop(0)
        print(ele, end=" ")
        for i in graph[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited


graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
BFS(graph_elements, "a")

