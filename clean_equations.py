import glob

# get all relevant tex files
files = glob.glob("./**/*.tex", recursive=True)

for filename in files:
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            # look for last lines of equations
            if i != len(lines) - 1 and '\end' in line and '*' in line:

                j = 2
                while '\\begin' not in lines[i - j]:
                    j += 1
                lastchar_text = lines[i - j - 1][-2]
                lastchar_equation = lines[i - 1][-2]
                firstchar_text = lines[i + 1].replace('\t', '')[0]

                while lastchar_equation in [' ', '\t', '\\']:
                    lines[i - 1] = lines[i - 1][:-2] + '\n'
                    print(f"Removed trailing whitespace or unnecessary break at {filename}:{i}")
                    lastchar_equation = lines[i - 1][-2]

                if lastchar_equation != '.' and (firstchar_text.isupper() or (firstchar_text == '\n' and lastchar_text == ',')):
                    lines[i - 1] = lines[i - 1][:-1] + '.\n'
                    print(f"Added period at {filename}:{i}")
                elif lastchar_equation == '.' and firstchar_text.islower():
                    lines[i] = line[:-2] + '\n'
                    print(f"Removed extra period at {filename}:{i}")

    with open(filename, 'w', encoding="utf-8", newline='\r\n') as f:
        f.writelines(lines)
