# each line has format x-y z: password
# a password is valid if char 'z' appears between x to y times (inclusive) in password
def p1(lower, h, ch, pwd):
    return 1 if lower <= pwd.count(ch) <= h else 0


# a password is valid if char 'z' appears exactly once at index x or y (1-indexed)
def p2(lower, h, ch, pwd):
    return 1 if (pwd[lower - 1] == ch) != (pwd[h - 1] == ch) else 0


input_file = open("input.txt", "r")
num_valid_1 = 0
num_valid_2 = 0
for line in input_file:
    tokens = line.split()
    range_tokens = tokens[0].split("-")
    lo = int(range_tokens[0])
    hi = int(range_tokens[1])
    c = tokens[1][0]
    password = tokens[2]
    num_valid_1 += p1(lo, hi, c, password)
    num_valid_2 += p2(lo, hi, c, password)

print(num_valid_1)
print(num_valid_2)
