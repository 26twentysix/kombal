class Edge:
    a = 0
    b = 0
    e_len = 0

    def __init__(self, a, b, e_len):
        self.a = a
        self.b = b
        self.e_len = e_len


edges_list = list()


def read_input():
    with open('testLab3.txt') as file:
        flines = file.readlines()
        n = int(flines.pop(0))
        for i in range(n):
            curr_line = flines[i]
            curr_line_ints = list(map(int, curr_line.split()))
            a = i + 1
            while True:
                b = curr_line_ints.pop(0)
                if b != 0:
                    e_len = curr_line_ints.pop(0)
                    edge = Edge(a, b, e_len)
                    edges_list.append(edge)
                else:
                    break

read_input()
for edge in edges_list:
    print(str(edge.a) + ' ' + str(edge.b) + ' ' + str(edge.e_len))