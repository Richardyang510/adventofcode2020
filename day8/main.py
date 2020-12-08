input_file = open("input.txt", "r")
instructions = []
for line in input_file:
    instructions.append(line)


def exec_instr(instr):
    acc = 0
    i = 0
    visited = set()
    while i not in visited and i < len(instr):
        visited.add(i)
        ins = instr[i].split(" ")[0]
        val = instr[i].split(" ")[1].strip()
        if ins == "acc":
            acc += int(val)
            i += 1
        elif ins == "jmp":
            i += int(val)
        else:
            i += 1

    return i, acc


print(exec_instr(instructions))

for i in range(len(instructions)):
    instructions_cpy = instructions.copy()
    ins = instructions_cpy[i].split(" ")[0]
    if ins == "jmp":
        instructions_cpy[i] = instructions_cpy[i].replace("jmp", "nop")
    elif ins == "nop":
        instructions_cpy[i] = instructions_cpy[i].replace("nop", "jmp")
    else:
        continue
    end_line, acc = exec_instr(instructions_cpy)
    if end_line == len(instructions_cpy):
        print("found", i, acc)
        break
