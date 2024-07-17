from ..extracting.tex_extraction.arxiv_extraction import ArxivExtraction
from ..extracting.tex_extraction.arxiv_extraction import ArxivExtraction
from ..extracting.tex_extraction.base_extraction import BaseExtraction
from ..data_models.paper import Paper


def extraction2paper(extraction: BaseExtraction):
    paper = Paper(
        title=extraction.get_title(),
        authors=extraction.get_authors(),
        source_url=extraction.get_paper_url(),
        bibtex=extraction.get_bibtex(),
        original_tex=extraction.get_tex(),
    )
    return paper


def build_arxiv_paper(arxiv_id: str):
    arxiv_extraction = ArxivExtraction(arxiv_id)
    return extraction2paper(arxiv_extraction)


if __name__ == '__main__':
    # Example
    arxiv_id = '2006.04710'
    arxiv_paper = build_arxiv_paper(arxiv_id)
    print(arxiv_paper.statements.model_dump_json(indent=4))