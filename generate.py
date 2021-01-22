import argparse
import random
import string


def generate(size, line_length):
    for _ in range(size):
        length = random.randint(0, line_length)
        yield "".join(random.choice(string.printable) for _ in range(length))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--file-size", type=int, required=True)
    parser.add_argument("-l", "--line-max-length", type=int, required=True)
    parser.add_argument("-f", "--filename", type=str, required=True)
    args = parser.parse_args()

    with open(args.filename, 'w') as f:
        f.writelines(generate(args.file_size, args.line_max_length))
