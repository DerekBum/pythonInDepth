from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent

setup(
    long_description=(this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',
    name='latex_generator_DerekBum_AP2024',
    version='0.3',
    py_modules=['latex_generator'],
    install_requires=[],
)
