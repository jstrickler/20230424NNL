import os

FOLDER = "DATA"
FILE = "mary.txt"

file_path = os.path.join(FOLDER, FILE)

with open(file_path) as file_in:
    # F.seek() F.tell() F.read()
    with open('mary_upper.txt', 'w') as mary_out:
        for raw_line in file_in:
            line = raw_line.rstrip()
            print(line)
            mary_out.write(raw_line.upper())

with open(file_path) as mary_in:
    all_lines = mary_in.read().splitlines()
    print("all_lines: {}".format(all_lines))


    