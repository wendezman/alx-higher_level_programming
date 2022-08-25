#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = (len(sys.argv) - 1)

    if args == 1:
        print("1 argument:")
    elif args == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(args))

    for count in range(1, len(sys.argv)):
        print("{:d}:".format(count), str(sys.argv[count]))
