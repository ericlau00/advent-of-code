def main():
    masses = open("input.txt").read().split('\n')
    fuels = [int(mass) // 3 - 2 for  mass in masses]
    total = 0
    for fuel in fuels:
        total += fuel
    print(total)

if __name__ == "__main__":
    main()
