from paper_extraction.builders.paper_database_builder import create_paper_database, load_paper_database
from paper_extraction.builders.html_pages_builder import build_html_files


test_db_path = '/remote/idiap.svm/temp.rea01/sljungbeck/lm_theory_library/test/test_db.json'     # TODO: change to universal paths
pages_root = '/remote/idiap.svm/temp.rea01/sljungbeck/lm_theory_library/test/generated_pages'
root = '/remote/idiap.svm/temp.rea01/sljungbeck/lm_theory_library/test/'


from dotenv import load_dotenv
from paper_extraction.config.config import DOTENV_PATH
load_dotenv(DOTENV_PATH)


arxiv_papers = [
    # '2406.17837',
    '2006.04710',
    # '2406.01506',
]

db = create_paper_database(
    path=test_db_path,
    extraction_dir='/remote/idiap.svm/temp.rea01/sljungbeck/lm_theory_library/test/tmp'
)
# db = load_paper_database(test_db_path)


db.add_arxiv_papers(arxiv_papers)
db.extend(overwrite=False)
db.save()

build_html_files(pages_root, root, test_db_path)