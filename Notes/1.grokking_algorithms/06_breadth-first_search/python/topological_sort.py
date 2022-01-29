from collections import deque

GRAY, BLACK = 0, 1


def topological(graph):
    """
    Topological sort with Colors
    https://gist.github.com/kachayev/5910538
    http://py-algorithm.blogspot.com/2011/09/blog-post.html
    :param graph:
    :return:
    """
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order


graph = {
    '1': ['4'],
    '4': ['2', '3'],
    '3': [],
    '2': []
}
print(topological(graph))
# 1, 2, 3, 4
# deque(['1', '4', '3', '2'])
