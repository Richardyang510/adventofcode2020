
def find_rparen(e, i):
    s = 0
    while i < len(e):
        if e[i] == '(':
            s += 1
        elif e[i] == ')':
            s -= 1
        i += 1
        if s == 0:
            return i - 1


def find_lparen(e, i):
    s = 0
    while i >= 0:
        if e[i] == '(':
            s += 1
        elif e[i] == ')':
            s -= 1
        i -= 1
        if s == 0:
            return i + 1


def get_first_token(e):
    if e[0] == '(':
        rp = find_rparen(e, 0)
        return p1_eval(e[1:rp]), rp + 1
    else:
        return int(e[0]), 1


def p1_eval(e):
    e = e.replace(' ', '')
    if len(e) == 0:
        return 0

    lhs, i = get_first_token(e)
    e = e[i:]

    while len(e) > 0:
        op = e[0]
        e = e[1:]
        rhs, i = get_first_token(e)
        e = e[i:]

        if op == '+':
            lhs += rhs
        elif op == '*':
            lhs *= rhs

    return lhs


def get_lhs(e, i, d):
    s = i - 1
    while True:
        lp = s
        if e[s] == '+' or e[s] == '*':
            s += 1
            lp += 1
            break
        elif e[s] == ')':
            lp = find_lparen(e, s)
            break
        if s == 0:
            break
        s -= 1
    return p2_eval(e[lp: i], d+1), lp


def get_rhs(e, i, d):
    r = i + 1
    while True:
        rp = r
        if e[r] == '+' or e[r] == '*':
            r -= 1
            rp -= 1
            break
        elif e[r] == '(':
            rp = find_rparen(e, r)
            break
        if r == len(e) - 1:
            break
        r += 1
    return p2_eval(e[i + 1: rp + 1], d+1), rp


def replace_val(e, l, r, v):
    e_char = list(e)
    del e_char[l:r + 1]
    e_char[l:l] = list(str(v))
    return ''.join(e_char)


def p2_eval(e, d=0):
    e = e.replace(' ', '')
    if len(e) == 0:
        return 0
    # print(' '*d, e)

    if '(' in e:
        lp = e.find('(')
        rp = lp + find_rparen(e[lp:], 0)
        val = p2_eval(e[lp + 1:rp], d+1)
        e = replace_val(e, lp, rp, val)
    elif '+' in e:
        op = e.find('+')
        lhs, li = get_lhs(e, op, d)
        rhs, ri = get_rhs(e, op, d)
        val = lhs + rhs
        e = replace_val(e, li, ri, val)
    elif '*' in e:
        op = e.find('*')
        lhs, li = get_lhs(e, op, d)
        rhs, ri = get_rhs(e, op, d)
        val = lhs * rhs
        e = replace_val(e, li, ri, val)
    else:
        return int(e)

    return p2_eval(e, d)



tot1 = 0
tot2 = 0
input_file = open("input.txt", "r")
for line in input_file:
    tot1 += p1_eval(line.strip())
    tot2 += p2_eval(line.strip())

print(tot1)
print(tot2)
