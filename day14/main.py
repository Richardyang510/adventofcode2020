def mask_val(v, m, write_x=False):
    v = v.zfill(len(m))
    v_l = list(v)

    for i in range(len(m)):
        if not write_x and m[i] == '0':
            v_l[i] = '0'
        elif m[i] == '1':
            v_l[i] = '1'

        if write_x and m[i] == 'X':
            v_l[i] = 'X'

    return ''.join(v_l)


def p1():
    input_file = open("input.txt", "r")
    mask = ""
    mem = {}
    for line in input_file:
        if line[:4] == "mask":
            mask = line[7:].strip()
        else:
            addr = int(line[line.find('[') + 1: line.find(']')])
            val = int(line[line.find('=') + 2:])

            bin_val = format(val, 'b')
            bin_masked = mask_val(str(bin_val), mask)
            int_masked = int(bin_masked, 2)

            mem[addr] = int_masked

    total = 0
    for key in mem:
        total += mem[key]

    print(total)


def p2():
    input_file = open("input.txt", "r")
    mask = ""
    mem = {}
    for line in input_file:
        if line[:4] == "mask":
            mask = line[7:].strip()
        else:
            addr = int(line[line.find('[') + 1: line.find(']')])
            val = int(line[line.find('=') + 2:])

            bin_addr = format(addr, 'b')
            bin_masked = mask_val(str(bin_addr), mask, True)

            # print(bin_addr.zfill(36))
            # print(mask)
            # print(bin_masked)

            num_x = bin_masked.count('X')
            for i in range(2**num_x):
                x_replaces = list(str(format(i, 'b')).zfill(num_x))
                bin_masked_cpy = bin_masked.replace('X', '{}')
                bin_masked_cpy = bin_masked_cpy.format(*x_replaces)
                int_masked = int(bin_masked_cpy, 2)
                mem[int_masked] = val
                # print(int_masked, val)

    total = 0
    for key in mem:
        total += mem[key]

    print(total)


p1()
p2()
