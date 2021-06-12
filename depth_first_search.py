#!urs/bin/env python
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set()
def depth_first_search(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for i in graph[node]:
            depth_first_search(visited, graph, i)
depth_first_search(visited, graph, "A")

