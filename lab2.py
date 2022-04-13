import collections


def read_matrix(my_dict, filename):
    with open(filename) as f:
        flines = f.readlines()
        n = int(flines.pop(0))
        for i in range(n):
            tmp_str = flines[i].replace(' ', '')
            for j in range(n):
                if tmp_str[j] == '1':
                    my_dict[i+1].append(j+1)
    print(my_dict)


def restore_cycle(route, node):
    pass


def dfs(graph, visited, node):
    queue = list()
    queue.append(node)
    while queue:
        curr_node = queue.pop(0)
        for neighbour in graph[curr_node]:
            if neighbour not in queue and neighbour not in visited:
                queue.append(neighbour)
        visited.append(curr_node)


my_dict = collections.defaultdict(list)
read_matrix(my_dict, 'testLab2.txt')
visited = list()
dfs(my_dict, visited, 1)
print(visited)