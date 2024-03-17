import latex_generator
import subprocess

if __name__ == "__main__":
    image_path = "../img/img.png"
    image_latex = latex_generator.generate_latex_image(image_path)

    table_data = [
        ["Name", "Age", "Gender"],
        ["John", 25, "Male"],
        ["Alice", 30, "Female"],
        ["Bob", 28, "Male"]
    ]
    table_latex = latex_generator.generate_latex_table(table_data)

    latex_content = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\usepackage[export]{{adjustbox}}
    
\\begin{{document}}
    
{table_latex}
{image_latex}
    
\\end{{document}}
"""
    with open("../artifacts/full/output.tex", "w") as file:
        file.write(latex_content)

    subprocess.run(["pdflatex", "output.tex"], cwd="artifacts/full")
