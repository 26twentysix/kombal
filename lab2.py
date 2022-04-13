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


queue = collections.deque()


def dfs(graph, visited, node, parent):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor != parent:
            queue.append(neighbor)
        if neighbor in visited and not neighbor == parent:
            cycle_end = neighbor
            queue.pop()
            cycle = list()
            while True:
                cycle_elem = queue.pop()
                cycle.append(cycle_elem)
                if cycle_elem == cycle_end:
                    break
            cycle.sort()
            with open('testLab2Result.txt', 'w') as f:
                f.write('N\n')
                for node in cycle:
                    f.write(str(node) + ' ')
            exit(0)
        elif neighbor not in visited:
            dfs(graph, visited, neighbor, node)


my_dict = collections.defaultdict(list)
read_matrix(my_dict, 'testLab2.txt')
visited = list()
queue.append(1)
with open('testLab2Result.txt', 'w') as f:
    f.write('A')
dfs(my_dict, visited, 1, None)

