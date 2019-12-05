def intcode(mem, noun, verb):
    mem[1] = noun
    mem[2] = verb
    pointer = 0
    while(mem[pointer + 3] < len(mem) and mem[pointer] != 99):
        param1 = mem[pointer + 1]
        param2 = mem[pointer + 2]
        param3 = mem[pointer + 3]
        mem[param3] = \
            mem[param1] + mem[param2] if mem[pointer] == 1 \
            else mem[param1] * mem[param2]
        pointer += 4
    return mem


def part2():
    for noun in range(100):
        for verb in range(100):
            seq = [int(integer) for integer in open('input.txt').read().split(',')]
            output = intcode(seq, noun, verb)[0]
            if output == 19690720:
                return 100 * noun + verb


if __name__ == "__main__":
    seq = [int(integer) for integer in open('input.txt').read().split(',')]
    print("Answer to part 1:", intcode(seq, 12, 2)[0])
    print("Answer to part 2:", part2())
