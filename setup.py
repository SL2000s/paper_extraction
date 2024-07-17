import os

from setuptools import setup, find_packages


PKG_ROOT = os.path.abspath(os.path.dirname(__file__))


def load_requirements() -> list:
    """Load requirements from file, parse them as a Python list!"""

    with open(os.path.join(PKG_ROOT, "requirements.txt"), encoding="utf-8") as f:
        all_reqs = f.read().split("\n")
    install_requires = [str(x).strip() for x in all_reqs]

    return install_requires


setup(
    name='paper_extraction',
    version='0.1',
    packages=find_packages(),
    install_requires=load_requirements(),
    author='Simon Ljungbeck',
    author_email='simon.ljungbeck@idiap.ch',
    description='A package for extracting data from scientific papers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SL2000s/paper_extraction',
    python_requires='>=3.6',
)
