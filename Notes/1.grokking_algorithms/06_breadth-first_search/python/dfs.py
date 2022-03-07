def person_is_seller(name):
    return name[-1] == "m"


graph = {"you": ["alice", "bob", "claire"],
         "bob": ["anuj", "peggy"],
         "alice": ["peggy"],
         "claire": ["thom", "jonny"],
         "anuj": [],
         "peggy": [],
         "thom": [],
         "jonny": []}

visited = []


def search(visited, graph, node):
    """
    This is actually dfs
    dfs and bsf have same time complexity but dfs slower
    because it can search on ways that in the end can be
    false and return and search again.
    Dfs used just for search somethibg abd
    Bfs used for finding shortest way
    :param visited:
    :param graph:
    :param node:
    :return:
    """
    print(visited)
    if not node in visited:
        # выполняем проверку на продавца она должна вернуть true false
        if person_is_seller(node):
            print(node + " is a mango seller!")
            return True
        else:
            visited.append(node)
            for neighbour in graph[node]:
                search(visited, graph, neighbour)
    return False


search(visited, graph, "you")
