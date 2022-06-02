class Edge:
    a = 0
    b = 0
    e_len = 0

    def __init__(self, a, b, e_len):
        self.a = a
        self.b = b
        self.e_len = e_len


def read_input():
    with open('testLab3.txt') as file:
        edges_list = list()
        flines = file.readlines()
        n = int(flines.pop(0))
        for i in range(n):
            curr_line = flines[i]
            curr_line_ints = list(map(int, curr_line.split()))
            a = i
            while True:
                b = curr_line_ints.pop(0) - 1
                if b != -1:
                    e_len = curr_line_ints.pop(0)
                    edge = Edge(a, b, e_len)
                    edges_list.append(edge)
                else:
                    break
            start_pos = int(flines[n]) - 1
            end_pos = int(flines[n + 1]) - 1
        return [edges_list, n, start_pos, end_pos]


def ford_bellman(edges_list, n, start_pos, end_pos):
    longest_path = [-1] * n
    longest_path[start_pos] = 1
    farest_vertex = [-1] * n
    path = list()
    while True:
        flag = False
        for i in range(len(edges_list)):
            if longest_path[edges_list[i].a] > -1:
                if longest_path[edges_list[i].b] < longest_path[edges_list[i].a] * edges_list[i].e_len:
                    longest_path[edges_list[i].b] = longest_path[edges_list[i].a] * edges_list[i].e_len
                    farest_vertex[edges_list[i].b] = edges_list[i].a
                    flag = True
        if not flag:
            break
    cur = farest_vertex[end_pos]
    if longest_path[end_pos] == -1:
        return [-1, -1]
    path.append(end_pos + 1)
    while cur != -1:
        path.append(cur + 1)
        cur = farest_vertex[cur]
    path.reverse()
    return [longest_path[end_pos], path]


def create_output(path_weight, path):
    with open('testLab3Result.txt', 'w') as file:
        if path_weight == -1:
            file.write('N')
        else:
            file.write('Y\n')
            file.write(str(path)[1:-1].replace(',', '') + '\n')
            file.write(str(path_weight))


input_params = read_input()
f_b_params = ford_bellman(input_params[0], input_params[1], input_params[2], input_params[3])
create_output(f_b_params[0], f_b_params[1])
