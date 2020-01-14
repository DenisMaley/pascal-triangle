def sierpinski_latex(triangle):
    triangle_tabular_rows = ['\\begin{tabular}{r%s}' % ('c' * (2 * triangle.n + 1))]
    for i, row in enumerate(triangle.triangle):
        row_i = '$m=%d$:&' % i
        row_i += '&' * (triangle.n - i)
        row_i += '& &'.join(triangle.repr_element(x) for x in row)
        row_i += '\\\\\\noalign{\\smallskip\\smallskip}'
        triangle_tabular_rows.append(row_i)
    triangle_tabular_rows.append('\\end{tabular}')
    result = '\n'.join(triangle_tabular_rows)
    return result
