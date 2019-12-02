def main():
    masses = open("input.txt").read().split('\n')
    fuels = [int(mass) // 3 - 2 for mass in masses]
    total = 0
    for fuel in fuels:
        total += sub(fuel)
    return total


def sub(fuel):
    if(fuel < 0):
        return 0
    else:
        return sub(fuel // 3 - 2) + fuel


if __name__ == "__main__":
    print(main())
