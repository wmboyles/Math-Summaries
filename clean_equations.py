import glob

# get all relevant tex files
exceptions = ['./common/main_common.tex', './common/contributors.tex']
files = [f for f in glob.glob("./**/*.tex", recursive=True) if f not in exceptions]

for filename in files:
    with open(filename) as f:
        lines = f.readlines()

        for i, line in enumerate(lines):

            # look for last lines of equations
            if i != len(lines) - 1 and '\end' in line and '*' in line:

                # get last character of above line and first character of below line
                lastchar = lines[i - 1][-2]
                firstchar = lines[i + 1].replace('\t', '')[0]

                if lastchar == ' ' or lastchar == '\t':
                    lines[i - 1] = lines[i - 1][:-2] + '\n'
                    print('Removed extra space/tab on line', i, 'in', filename)
                    lastchar = lines[i - 1][-2]

                if lastchar != '.' and firstchar.isupper():
                    lines[i - 1] = lines[i - 1][:-1] + '.\n'
                    print('Added period on line', i, 'in', filename)
                elif lastchar == '.' and firstchar.islower():
                    lines[i - 1] = lines[i - 1][:-2] + '\n'
                    print('Removed extra period on line', i, 'in', filename)

            # replace LF newlines with CRLF
            line = line.replace('\n', '\r\n')

    with open(filename, 'w', newline='\r\n') as f:
        f.writelines(lines)
