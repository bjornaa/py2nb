import nbformat


def nb2py(nbfile, pyfile):

    nb = nbformat.read(nbfile, as_version=4)

    with open(pyfile, mode='wt', encoding='utf-8') as pyf:
        for cell in nb.cells:
            type = cell.cell_type

            if type == 'code':
                pyf.write('#%%\n')
                pyf.write(cell.source)
                pyf.write('\n\n')

            elif type == 'markdown':
                pyf.write('#%%\n')
                pyf.write('"""\n')
                pyf.write(cell.source)
                pyf.write('\n"""\n\n')
