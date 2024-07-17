import os
import warnings

from .config.config import PAPER_DATABASE_PATH
from .data_models.paper_database import PaperDatabase
from .html_rendering.html_renderer import HTMLGenerator


def load_paper_database(path: str = None):
    path = path or PAPER_DATABASE_PATH
    if os.path.exists(path):
        with open(path, 'r') as file:
            paper_database = PaperDatabase.model_validate_json(file.read())
    else:
        if path != PAPER_DATABASE_PATH:
            warnings.warn(f'Could not load a paper database from {path}. Returning empty database.')
        paper_database = PaperDatabase(db_path=path)
    return paper_database


def build_html_files(db_path: str = None):
    db = load_paper_database(db_path or PAPER_DATABASE_PATH)
    html_generator = HTMLGenerator(db)
    html_generator.build_html_files()


if __name__ == '__main__':
    # import sys
    # pkg_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # sys.path.append(pkg_dir)

    from .config.config import DOTENV_PATH
    from dotenv import load_dotenv
    load_dotenv(DOTENV_PATH)

    arxiv_papers = [
        # '2406.17837',
        '2006.04710',
        # '2406.01506',
    ]

    db = load_paper_database()
    db.add_arxiv_papers(arxiv_papers)
    # db.extend(overwrite=False)
    db.save()

    # db = load_paper_database()
    # db.extend_urls()
    # db.extend_label2statementids()
    # db.extend_html_refs()
    # db.extend_motivation_htmls()
    # db.extend_proof_explaination_htmls()
    # db.save()
    
    # build_html_files()

    # db = load_paper_database(PAPER_DATABASE_PATH)
    # print(db.papers[0].model_dump_json(indent=4))



    # from .builders.paper_builder import build_arxiv_paper
    
    # db.add_arxiv_papers(['2406.17837'])

    # arxiv_url = '2406.17837'
    # paper = 