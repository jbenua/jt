import argparse
import contextlib
import os


def comp_strings(a, b):
    """Compare two Noneable-strings"""
    try:
        return a < b
    except TypeError:
        return bool(a)


def merge(chunk_names):
    """Order the lines from many chunks"""
    n_o_chunks = len(chunk_names)

    with contextlib.ExitStack() as stack:
        files = [stack.enter_context(open(name)) for name in chunk_names]
        strings = [file.readline() for file in files]

        while any(strings):
            min_index = 0
            for i in range(1, n_o_chunks):
                if comp_strings(strings[i], strings[min_index]):
                    min_index = i
            if strings[min_index]:
                yield strings[min_index]
                line = files[min_index].readline()
                if line:
                    strings[min_index] = line
                else:
                    strings[min_index] = None



def read_chunk(file, chunk_size):
    """Read specifiс number of lines from file"""
    chunk = []
    for _ in range(chunk_size):
        line = file.readline()
        if line:
            chunk.append(line)
        else:
            return chunk
    return chunk


def sort(chunk_size, filename, output):
    """Sort filename by `chunk_size` chunks, write result to output"""
    chunk_id = 0
    chunk_names = []

    with open(filename) as f:
        chunk = read_chunk(f, chunk_size)
        while chunk:
            chunk.sort()
            chunk_name = "{}.chunk.{}".format(filename, chunk_id)
            with open(chunk_name, "w") as out_chunk:
                out_chunk.writelines(chunk)
            chunk_id += 1
            chunk_names.append(chunk_name)
            chunk = read_chunk(f, chunk_size)

    with open(output, "w") as out:
        out.writelines(merge(chunk_names))

    for chunk in chunk_names:
        os.unlink(chunk)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--chunk-size",
        help="Chunk size", type=int, default=1000
    )
    parser.add_argument("-f", "--filename", help="File to sort")
    args = parser.parse_args()
    name, ext = args.filename.rsplit('.', maxsplit=1)
    sort(
        args.chunk_size,
        args.filename,
        "{}.sorted.{}".format(name, ext)
    )
