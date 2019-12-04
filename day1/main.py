def main(part):
    masses = open("input.txt").read().split('\n')
    fuels = [int(mass) // 3 - 2 for mass in masses]
    total = 0
    for fuel in fuels:
        total += fuel if part == 1 else sub(fuel)
    return total


def sub(fuel):
    return 0 if fuel < 0 else sub(fuel // 3 - 2) + fuel


if __name__ == "__main__":
    print("Answer to part 1:", main(1))
    print("Answer to part 2:", main(2))
