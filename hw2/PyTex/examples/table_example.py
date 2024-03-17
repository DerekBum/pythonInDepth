from latex_generator import generate_latex_table

if __name__ == "__main__":
    data = [
        ["Name", "Age", "Gender"],
        ["John", 25, "Male"],
        ["Alice", 30, "Female"],
        ["Bob", 28, "Male"]
    ]

    latex_table = generate_latex_table(data)

    latex_begin = ('\\documentclass{article}\n'
                   '\\usepackage[english]{babel}\n'
                   '\\begin{document}\n')
    latex_end = '\\end{document}'

    with open("../artifacts/output_table.tex", "w") as file:
        file.write(latex_begin)
        file.write(latex_table)
        file.write(latex_end)
