import copy

input_file = open("input.txt", "r")

floor_plan = []
row_num = 0

for line in input_file:
    line_list = []
    for char in line.strip():
        line_list.append(char)
    floor_plan.append(line_list)


def p1_iterate(fp):
    fp_cp = copy.deepcopy(fp)
    for r in range(len(fp)):
        for c in range(len(fp[0])):
            if fp[r][c] == '.':
                continue
            num_occ = 0
            num_emp = 0
            for d_r in range(-1, 2):
                for d_c in range(-1, 2):
                    if (d_r != 0 or d_c != 0) and r + d_r >= 0 and c + d_c >= 0 and \
                            r + d_r < len(fp) and c + d_c < len(fp[0]):
                        if fp[r + d_r][c + d_c] == 'L' or fp[r + d_r][c + d_c] == '.':
                            num_emp += 1
                        elif fp[r + d_r][c + d_c] == '#':
                            num_occ += 1
            if num_occ >= 4:
                fp_cp[r][c] = 'L'
            elif num_occ == 0:
                fp_cp[r][c] = '#'
    return fp_cp


def fp_same(fp1, fp2):
    for r in range(len(fp1)):
        for c in range(len(fp1[0])):
            if fp1[r][c] != fp2[r][c]:
                return False
    return True


def fp_count_occ(fp):
    num_occ = 0
    for r in range(len(fp)):
        for c in range(len(fp[0])):
            if fp[r][c] == '#':
                num_occ += 1
    return num_occ


def p1(fp):
    fp_it = copy.deepcopy(fp)
    while True:
        fp_it_2 = p1_iterate(fp_it)
        if fp_same(fp_it, fp_it_2):
            print(fp_count_occ(fp_it))
            break
        fp_it = fp_it_2


p1(floor_plan)

dir_r = [-1, -1, -1, 0, 1, 1, 1, 0]
dir_c = [-1, 0, 1, 1, 1, 0, -1, -1]


def p2_iterate(fp):
    fp_cp = copy.deepcopy(fp)
    for r in range(len(fp)):
        for c in range(len(fp[0])):
            if fp[r][c] == '.':
                continue
            num_occ = 0
            num_emp = 0

            for d in range(8):
                new_r = r + dir_r[d]
                new_c = c + dir_c[d]
                while 0 <= new_r < len(fp) and 0 <= new_c < len(fp[0]):
                    if fp[new_r][new_c] == '#':
                        num_occ += 1
                        break
                    elif fp[new_r][new_c] == 'L':
                        break
                    new_r += dir_r[d]
                    new_c += dir_c[d]

            if num_occ >= 5:
                fp_cp[r][c] = 'L'
            elif num_occ == 0:
                fp_cp[r][c] = '#'
    return fp_cp


def p2(fp):
    fp_it = copy.deepcopy(fp)
    while True:
        fp_it_2 = p2_iterate(fp_it)
        if fp_same(fp_it, fp_it_2):
            print(fp_count_occ(fp_it))
            break
        fp_it = fp_it_2


p2(floor_plan)
