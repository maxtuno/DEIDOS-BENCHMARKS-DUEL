if __name__ == '__main__':

    import sys
    import random

    bits = int(sys.argv[1])
    size = int(sys.argv[2])

    universe = [complex(random.randint(1, 2 ** bits - 1), random.randint(1, 2 ** bits - 1)) for i in range(size)]

    with open('data.txt', 'w') as data:
        target = random.randint(2 ** bits - 1, 2 ** (bits + 1) - 1)
        print(int(target), file=data)
        for uv in universe:
            print(int(uv.real), int(uv.imag), file=data)
