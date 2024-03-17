def generate_latex_table(data):
    """
    Generate a LaTeX table from a two-dimensional list.

    Args:
    data (list): Double list containing table data.

    Returns:
    str: LaTeX formatted table string.
    """
    latex_table = "\\begin{table}[h!]\n\\centering\n\\begin{tabular}{|" + "c|" * len(data[0]) + "}\n\\hline\n"

    for row in data:
        latex_table += " & ".join(map(str, row)) + " \\\\\n\\hline\n"

    latex_table += "\\end{tabular}\n\\end{table}\n"

    return latex_table


def generate_latex_image(image_path):
    """
    Generate LaTeX code for inserting an image.

    Args:
    image_path (str): Path to the image file.

    Returns:
    str: LaTeX code for inserting the image.
    """
    latex_code = "\\begin{figure}[h!]\n"
    latex_code += "\\centering\n"
    latex_code += "\\includegraphics[max size={\\textwidth}{\\textheight}]{" + image_path + "}\n"
    latex_code += "\\end{figure}"

    return latex_code
