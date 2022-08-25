#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    total = 0
    for n in range(args):
        total = total + int(sys.argv[n + 1])
    print(total)
