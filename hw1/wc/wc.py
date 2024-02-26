import sys


def count_lines_words_chars(file):
    lines = 0
    words = 0
    chars = 0
    for line in file:
        # In the real wc number of lines equal to the number of newline characters.
        # https://stackoverflow.com/questions/28038633/wc-l-is-not-counting-last-of-the-file-if-it-does-not-have-end-of-line-character
        if line[-1] == '\n':
            lines += 1
        words += len(line.split())
        chars += len(line)
    return lines, words, chars


def print_stats(lines, words, chars, filename=None):
    if filename:
        print(f"{lines:>4} {words:>4} {chars:>4} {filename:>4}")
    else:
        print(f"{lines:>4} {words:>4} {chars:>4}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        lines, words, chars = count_lines_words_chars(sys.stdin)
        print_stats(lines, words, chars)
    else:
        total_lines = 0
        total_words = 0
        total_chars = 0
        for filename in sys.argv[1:]:
            try:
                with open(filename, 'r') as file:
                    lines, words, chars = count_lines_words_chars(file)
                    print_stats(lines, words, chars, filename)
                    total_lines += lines
                    total_words += words
                    total_chars += chars
            except FileNotFoundError:
                print(f"wc: {filename}: No such file or directory", file=sys.stderr)
        if len(sys.argv) > 2:
            print_stats(total_lines, total_words, total_chars, "total")
