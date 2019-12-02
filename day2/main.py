def intcode(seq):
    seq[1] = 12
    seq[2] = 2
    opcode_pos = 0
    while(seq[opcode_pos] != 99):
        index1 = seq[opcode_pos + 1]
        index2 = seq[opcode_pos + 2]
        index3 = seq[opcode_pos + 3]
        seq[index3] = \
            seq[index1] + seq[index2] if seq[opcode_pos] == 1 \
            else seq[index1] * seq[index2]
        opcode_pos += 4
    return seq


if __name__ == "__main__":
    seq = [int(integer) for integer in open('input.txt').read().split(',')]
    print("Answer to part 1:", intcode(seq)[0])
