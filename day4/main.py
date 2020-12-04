def is_int(int_str):
    try:
        int(int_str)
    except ValueError:
        return False
    return True


def is_hex(hex_str):
    try:
        int(hex_str, 16)
    except ValueError:
        return False
    return True


def p1(port):
    return "byr" in port and "iyr" in port and "eyr" in port and "hgt" in port and "hcl" in port and "ecl" in port and \
           "pid" in port


def p2(port):
    if not("byr" in port and is_int(port["byr"]) and 1920 <= int(port["byr"]) <= 2002):
        return False

    if not("iyr" in port and is_int(port["iyr"]) and 2010 <= int(port["iyr"]) <= 2020):
        return False

    if not("eyr" in port and is_int(port["eyr"]) and 2020 <= int(port["eyr"]) <= 2030):
        return False

    if "hgt" in port:
        val = port["hgt"][:-2]
        typ = port["hgt"][-2:]
        if typ == "cm" and is_int(val):
            if int(val) < 150 or int(val) > 193:
                return False
        elif typ == "in" and is_int(val):
            if int(val) < 59 or int(val) > 76:
                return False
        else:
            return False
    else:
        return False

    if not("hcl" in port and port["hcl"][0] == "#" and len(port["hcl"]) == 7 and is_hex(port["hcl"][1:])):
        return False

    if not("ecl" in port and port["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False

    if not("pid" in port and len(port["pid"]) == 9 and is_int(port["pid"])):
        return False

    return True


valid_p1 = 0
valid_p2 = 0

input_file = open("input.txt", "r")
passport = {}
for line in input_file:
    if line == "\n":
        valid_p1 += 1 if p1(passport) else 0
        valid_p2 += 1 if p2(passport) else 0
        passport = {}
    tokens = line.split()
    for token_pair in tokens:
        kvp = token_pair.split(":")
        k = kvp[0]
        v = kvp[1]
        if len(v) > 0:
            passport[k] = v

# check last entry
valid_p1 += 1 if p1(passport) else 0
valid_p2 += 1 if p2(passport) else 0

print(valid_p1)
print(valid_p2)
