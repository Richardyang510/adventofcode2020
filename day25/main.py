DIV_VALUE = 20201227
SUBJECT_NUM = 7
card_pkey = 10604480
door_pkey = 4126658


def transform(loop_size, sn=SUBJECT_NUM):
    val = 1
    for _ in range(loop_size):
        val = (val * sn) % DIV_VALUE

    return val


def get_loop_sizes(val1, val2):
    i = 1
    val = 1
    ls1, ls2 = None, None
    while ls1 is None or ls2 is None:
        val = (val * SUBJECT_NUM) % DIV_VALUE
        if val == val1:
            ls1 = i
        if val == val2:
            ls2 = i
        i += 1
    return ls1, ls2


r1, r2 = get_loop_sizes(card_pkey, door_pkey)
print(transform(r1, door_pkey))
