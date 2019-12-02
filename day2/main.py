def intcode(mem, noun, verb):
    mem[1] = noun
    mem[2] = verb
    pointer = 0
    while(mem[pointer] != 99):
        param1 = mem[pointer + 1]
        param2 = mem[pointer + 2]
        param3 = mem[pointer + 3]
        mem[param3] = \
            mem[param1] + mem[param2] if mem[pointer] == 1 \
            else mem[param1] * mem[param2]
        pointer += 4
    return mem


if __name__ == "__main__":
    seq = [int(integer) for integer in open('input.txt').read().split(',')]
    print("Answer to part 1:", intcode(seq, 12, 2)[0])