filename = 'alice.txt'

try:
    with open(filename) as fo:
        contents = fo.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} was not found")
