import glob
import re

# get all relevant tex files
files = glob.glob("./**/*.tex", recursive=True)

for file in files:
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            split_line = re.split("\"", line)

            if len(split_line) % 2 == 0:
                print(f"WARNING: Possible unmatched quote at {file}:{i}")
                continue

            # each token at an odd index is in quotes
            for j in range(1, len(split_line), 2):
                split_line[j] = "``" + split_line[j] + "''"
                print(f"Fixed backward quote at {file}:{i}")

            lines[i] = ''.join(split_line)

    with open(file, 'w', encoding="utf-8", newline='\r\n') as f:
        f.writelines(lines)
