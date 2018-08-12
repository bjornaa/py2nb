import re

import nbformat as nbf
from nbformat.v4.nbbase import (
    new_code_cell, new_markdown_cell, new_notebook)

# Partly based on answers in:
# https://stackoverflow.com/questions/23292242

# Matches '#%%', '# %%', '#  %%', etc at start of line
SEPARATOR = re.compile(r'^# *%%')


def py2nb(py_file, ipynb_file):
    fp = open(py_file, mode='rt')

    raw_cells = list(extract_cells(fp))

    cells = []

    for rcell in raw_cells:
        # Strip out initial blank lines
        i = 0   #  Counting initial blank lines
        for line in rcell:
            if line.strip():
                break
            else:
                i += 1
        scell = rcell[i:] # Stripped cell

        if scell and scell[0].startswith('"""'):
            end = 0
            for i, line in enumerate(rcell[1:]):
                if line.startswith('"""'):
                    end = i+1
                    break
            if end > 0:   # Has a final line starting with """
                cells.append(new_markdown_cell(source="\n".join(scell[1:end])))
                continue

        # Everything else is a code cell
        cells.append(new_code_cell(source="\n".join(scell)))


    nb0 = new_notebook(cells=cells, metadata={'language': 'python'})

    with open(ipynb_file, encoding='utf-8', mode='wt') as f1:
        nbf.write(nb0, f1, 4)


def extract_cells(fp):
    """Extract the raw cells from a python script

    A raw cell is a list of consecutive lines from a python script

    parse_python breaks up the script at cell markers,
    '#%%', '# In[]', or similar and returns the raw cells

    """
    lines = []
    for line in fp:
        if SEPARATOR.match(line):
            if lines:
                yield(lines)
                lines = []
        else:
            lines.append(line.rstrip())
    # Any remaining lines at end of file
    if lines:
        yield(lines)
