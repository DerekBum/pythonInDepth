import sys


def nl(input_stream):
    try:
        line_number = 1
        for line in input_stream:
            print(f"{line_number:>6}\t{line}", end="")
            line_number += 1
        print()
    except KeyboardInterrupt:
        print()
        sys.exit()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        nl(sys.stdin)
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                nl(file)
        except FileNotFoundError:
            print(f"nl: {sys.argv[1]}: No such file or directory")
