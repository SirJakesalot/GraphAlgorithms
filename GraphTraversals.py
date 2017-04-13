def RDFS(graph, node, path=None, visited=None):
    if not visited and not path:
        path = []
        visited = set()
    path.append(node)
    visited.add(node)
    for neighbor in sorted(graph.neighbors(node)):
        if neighbor not in visited:
            RDFS(graph, neighbor, path, visited)
    return path
            
def IDFS(graph, node):
    visited = set()
    stack = [node]
    path = []
    while stack:
        vert = stack.pop()
        if vert not in visited:
            visited.add(vert)
            path.append(vert)
            stack.extend(sorted(graph.neighbors(vert), reverse=True))
    return path
    
def BFS(graph, node):
    qPtr = 0
    q = [node]
    visited = set()
    path = []
    while qPtr < len(q):
        vert = q[qPtr]
        qPtr += 1
        if vert not in visited:
            path.append(vert)
            visited.add(vert)
            q.extend(sorted(graph.neighbors(vert) - visited))
    return path