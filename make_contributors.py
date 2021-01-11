"""
Queries GitHub API to list contributors and their names.
Uses this info to generate the contributors page.

author: William Boyles (wmboyles)
"""

import requests

# Get contributor info, specifically username (login) and name
res = requests.get("https://api.github.com/repos/wmboyles/Math-Summaries/contributors")

if not res.ok:
    raise Exception(f"ERROR - {res.status_code}: {res.text}")

contributors = res.json()
for contributor in contributors:
    res = requests.get(contributor['url'])

    # Default to username if request fails or no full name
    if not res.ok:
        contributor['name'] = contributor['login']
        continue

    contributor_info = res.json()
    if 'name' not in contributor_info or contributor_info['name'] is None:
        contributor['name'] = contributor['login']
        continue

    contributor['name'] = contributor_info['name']


# Create the contributors.tex page
with open("common/contributors.tex", 'w') as f:
    f.write("""\section{Contributors}
Special thanks to everyone who made contributions to this project on \href{https://github.com/wmboyles/Math-Summaries}{Github}.
They are listed in order of number of commits as \\texttt{name (GitHub username)}.

\\begin{center}
    \\begin{tabular}{ c c c }
    """)

    i = 0
    for contributor in contributors:
        if i % 3 != 0:
            f.write(" & ")
        else:
            f.write("\t")
        
        f.write(f"{contributor['name']} (\\href{{{contributor['url']}}}{{{contributor['login']}}})")

        if i % 3 == 2:
            f.write(" \\\\\n\t")
        
        i += 1

    f.write("""\\end{tabular}
\\end{center}\n""")
