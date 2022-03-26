from collections import deque


def convert_node_to_index(node):
    ret = 0
    if node[0] == 'a':
        ret += 0
    elif node[0] == 'b':
        ret += 1
    elif node[0] == 'c':
        ret += 2
    elif node[0] == 'd':
        ret += 3
    elif node[0] == 'e':
        ret += 4
    elif node[0] == 'f':
        ret += 5
    elif node[0] == 'g':
        ret += 6
    elif node[0] == 'h':
        ret += 7
    ret += (8 - int(node[1])) * 8
    return ret


def convert_index_to_node(index):
    ret = ''
    if index % 8 == 0:
        ret += 'a'
    elif index % 8 == 1:
        ret += 'b'
    elif index % 8 == 2:
        ret += 'c'
    elif index % 8 == 3:
        ret += 'd'
    elif index % 8 == 4:
        ret += 'e'
    elif index % 8 == 5:
        ret += 'f'
    elif index % 8 == 6:
        ret += 'g'
    elif index % 8 == 7:
        ret += 'h'
    ret += str(8 - int(index / 8))
    return ret


def find_bad_pos(pawn_pos):
    if pawn_pos % 8 == 0:
        return [pawn_pos + 9]
    elif pawn_pos % 8 == 7:
        return [pawn_pos + 7]
    elif pawn_pos > 55:
        return []
    else:
        return [pawn_pos + 7, pawn_pos + 9]


dirs = [-17, -15, -6, 10, 17, 15, 6, -10]


def check_if_move_is_possible(current_node, move):
    if current_node % 8 == 0:
        if move == dirs[0]:
            return False
        elif move == dirs[5]:
            return False
        elif move == dirs[6]:
            return False
        elif move == dirs[7]:
            return False
    elif current_node % 8 == 7:
        if move == dirs[1]:
            return False
        elif move == dirs[2]:
            return False
        elif move == dirs[3]:
            return False
        elif move == dirs[4]:
            return False
    elif int(current_node / 8) == 0:
        if move == dirs[0]:
            return False
        elif move == dirs[1]:
            return False
        elif move == dirs[2]:
            return False
        elif move == dirs[7]:
            return False
    elif int(current_node / 8) == 7:
        if move == dirs[3]:
            return False
        elif move == dirs[4]:
            return False
        elif move == dirs[5]:
            return False
        elif move == dirs[6]:
            return False
    return True


def bfs(graph, start_node, end_node):
    bad_pos = find_bad_pos(end_node)
    my_queue = deque()
    my_queue.append(start_node)
    visited = set()
    while my_queue:
        current_node = my_queue.popleft()
        visited.add(current_node)
        print(convert_index_to_node(current_node))
        if current_node == end_node:
            print('Im done!')
            break
        for i in range(8):
            if check_if_move_is_possible(current_node, dirs[i]):
                if current_node + dirs[i] not in visited and -1 < current_node + dirs[i] < len(graph)\
                        and current_node + dirs[i] not in bad_pos:
                    my_queue.append(current_node+dirs[i])


graph = '#'*64
root_node = convert_node_to_index('b2')
finish_node = convert_node_to_index('e6')
graph = graph[:root_node] + 'К' + graph[root_node + 1:]
graph = graph[:finish_node] + 'П' + graph[finish_node + 1:]
print(graph)
bfs(graph, root_node, finish_node)
