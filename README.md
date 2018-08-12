# py2nb – Conversion between jupyter notebooks and python scripts

This python package provides two scipts

* `py2nb` – Convert a python script to a jupyter notebook
* `nb2py` – Convert a jupyter notebook to a python script

### `py2nb`

Cells in the python script are separated by '#%%' as in the
jupyter extension for visual studio code. (Also spyder?)

Markdown cells are marked by following the separator with a triple quoted
string, starting and ending with """ at the start of their lines. Any code in
the cell after the triple quoted string is ignored.

All other cells are converted to jupyter code cells.

### `nb2py`

Code cells and markdown cells are converted to a python file with cells
separated as described above. Raw NBConvert cells are presently ignored.

It differs from `jupyter nbconvert --to script` by a clear markup of the markdown cells.

### Motivation

I like the jupyter extension for the visual studio code editor. However for
documentation and sharing with others a jupyter notebook is needed. With the
py2nb script this is possible and gives the added bonus of being able to edit
the notebook with markdown cells in a real editor.

The nb2py script goes the opposite way, converting a notebook to a format
suitable for working in vs code with the jupyter extension.

py2nb followed with nb2py should return the same script. The only exception
should be the removal of code in a markdown cell after the triple quoted
string.

nb2py followed by nb2py should return an equivalent notebook with output and
Raw NBConvert removed and execution counts blanked out. This combined operation
may be useful for storing notebooks in a version control system.

These scripts work for me, but do not provide an ideal solution. I would have
preferred that opening an ipynb-file in vs code should do the nb2py (or
something similar) automatically and saving should perform something like the
py2nb script. Preferably with nice preview of the markdown cells or the whole
notebook. Unfortunately, I do not have the competence in Javascript to follow
this up.

### Other work

Conversion from notebook to python is part of the official `jupyter nbconvert` package.
It may be possible to make a template that provides a clearer markup of the
markdown cells.

Conversion from python to notebook is discussed at stackoverflow,
https://stackoverflow.com/questions/23292242. I learned a lot from that
discussion.

There is also a github repository, https://github.com/sklam/py2nb, with the
same name. It is presently not maintained. A newer repository is
https://github.com/chicham/py2nb.

There is a vs code extension, Jupyter Notebook Converter, by Yigit Ozgumus.
This is supposed to do a py2nb-like conversion within the vs code editor.
Unfortunately, it is not working for me. Presently, the `py2nb` script does not
accept the Jupyter Notebook Converter markup format for the markdown info. This
may be implemented later.