import sys


def tail(f):
    lines = f.readlines()
    last_lines = lines[-10:]
    return last_lines


if __name__ == "__main__":
    if len(sys.argv) == 1:
        lines = sys.stdin.readlines()
        last_lines = lines[-17:]
        print(''.join(last_lines))
    else:
        for ind, file in enumerate(sys.argv[1:]):
            try:
                with open(file, 'r') as f:
                    if ind != 0:
                        print()
                    if len(sys.argv) > 2:
                        print(f"==> {file} <==")
                    last_lines = tail(f)
                    print(''.join(last_lines), end='')

            except FileNotFoundError:
                print(f"tail: cannot open '{file}' for reading: No such file or directory")
