from lark import Lark

input_file = open("input.txt", "r")

rules = ""
messages = []

reading_rules = True
for line in input_file:
    if len(line.strip()) == 0:
        reading_rules = False
        continue

    if reading_rules:
        # remove block for p1
        if line.startswith('8:'):
            line = "8: 42 | 42 8\n"
        elif line.startswith('11:'):
            line = "11: 42 31 | 42 11 31\n"
        # end block
        rules += line
    else:
        messages.append(line.strip())

remove_digits = str.maketrans('0123456789', 'cdefghijkl')
grammar = rules.translate(remove_digits)

parser = Lark(grammar, start='c')

num_match = 0
for msg in messages:
    try:
        parser.parse(msg)
        num_match += 1
    except:
        continue

print(num_match)
