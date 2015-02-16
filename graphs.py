# graph from tom's example as a dict
the_graph = {1: [2, 4],
             2: [3, 5],
             3: [2],
             4: [1, 7],
             5: [2, 6, 8],
             6: [5, 9, 10],
             7: [4],
             8: [5],
             9: [6, 12],
             10: [6, 11],
             11: [10],
             12: [9],
             13: []}


# stacks and queues as classes
class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


class Queue(object):

    def __init__(self):
        self.items = []

    def dequeue(self):  # pops from end of list
        return self.items.pop()

    def enqueue(self, item):  # adds to beginning of list
        self.items.insert(0, item)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# iterative breadth-first search w/ queue class
def bfs(graph, start):
    visited = set()
    q = Queue()
    q.enqueue(start)
    path = []
    while not q.is_empty():
        vertex = q.dequeue()
        if vertex not in visited:
            visited.add(vertex)
            path = path + [vertex]
            for v in graph[vertex]:
                if v not in visited:
                    q.enqueue(v)
    return path


# write a function that, given a graph and two nodes, tells if the second
# node is accessible from the first
def is_accessible(graph, start, target):
    if start == target:
        return True
    visited = set()
    q = Queue()
    q.enqueue(start)
    while not q.is_empty():
        v = q.dequeue()
        if v == target:
            return True
        if v not in visited:
            visited.add(v)
            for n in graph[v]:
                q.enqueue(n)
    return False


# iterative depth-first search w/stack class
def dfs(graph, start):
    visited = set()
    stack = Stack()
    stack.push(start)
    path = []
    while not stack.is_empty():
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path = path + [vertex]
            for v in graph[vertex]:
                if v not in visited:
                    stack.push(v)
    return path


# find all paths between two nodes in a graph, recursive
def find_paths(graph, start, end, path=[]):
    path = [start]
    if start == end:
        return path
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_path(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


# find the shortest path between two nodes
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest
