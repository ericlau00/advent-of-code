def intcode(mem, id, part):
    pointer = 0
    outputs = list()
    while(mem[pointer] != 99):
        opcode = int(str(mem[pointer])[-2:])
        param_modes = [int(mode) for mode in str(mem[pointer])[:-2]]
        while(len(param_modes) < 3):
            param_modes.insert(0, 0)
        param1 = mem[pointer + 1]
        param2 = mem[pointer + 2]
        if not opcode == 3 and not opcode == 4:
            param3 = mem[pointer + 3]

        if opcode == 1 or opcode == 2:
            if not param_modes[-1]:
                param1 = mem[param1]
            if not param_modes[-2]:
                param2 = mem[param2]
            mem[param3] = param1 + param2 if opcode == 1 \
                else param1 * param2
            pointer += 4
            continue
        elif opcode == 3:
            mem[param1] = id
            pointer += 2
            continue
        elif opcode == 4:
            if not param_modes[-1]:
                param1 = mem[param1]
            outputs.append(param1)
            pointer += 2
            continue

        if(part == 2):
            if not param_modes[-1]:
                param1 = mem[param1]
            if not param_modes[-2]:
                param2 = mem[param2]

            if opcode == 5:
                if(param1 != 0):
                    pointer = param2
                else:
                    pointer += 3
            elif opcode == 6:
                if(param1 == 0):
                    pointer = param2
                else:
                    pointer += 3
            elif opcode == 7:
                mem[param3] = 1 if param1 < param2 else 0
                pointer +=4
            elif opcode == 8:
                mem[param3] = 1 if param1 == param2 else 0
                pointer +=4
    return outputs[-1]


if __name__ == "__main__":
    seq = [int(integer) for integer in open('input.txt').read().split(',')]
    print("Answer to part 1:", intcode(seq, 1, 1))
    seq = [int(integer) for integer in open('input.txt').read().split(',')]
    print("Answer to part 2:", intcode(seq, 5, 2))
