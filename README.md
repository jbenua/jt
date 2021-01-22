# JT

Test task, generate and sort very large text file line-by-line.
Python 3.

## Usage

Generate file:

```
$ python generate.py -s FILE_SIZE -l LINE_MAX_LENGTH -f FILENAME
```

Sort file:

```
$ python sort_file_by_lines.py [-s CHUNK_SIZE] -f FILENAME.EXT
```
The result will appear in `FILENAME.sorted.EXT`
