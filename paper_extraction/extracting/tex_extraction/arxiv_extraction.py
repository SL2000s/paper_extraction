import os

from ..tex_extraction.base_extraction import BaseExtraction
from ...config.config import ARXIV_EXTRACT_DIR
from ...utils.utils import extract_online_zip, dir_extension_files


class ArxivExtraction(BaseExtraction):
    ARXIV_SRC_URL_TEMPLATE = 'https://arxiv.org/src/{arxiv_id}'
    ARXIV_ABS_URL_TEMPLATE = 'https://arxiv.org/abs/{arxiv_id}'
    TEX_ACCUMULATION_ENTRY_TEMPLATE = """==== BEGINNING OF {file_name} ====
{content}
==== END OF {file_name} ===="""

    def __init__(self, arxiv_id: str, extract_dir: str = ARXIV_EXTRACT_DIR):
        self.arxiv_id = arxiv_id
        self.extract_dir = extract_dir
        self.src_url = self.ARXIV_SRC_URL_TEMPLATE.format(arxiv_id=self.arxiv_id)
        self.abs_url = self.ARXIV_ABS_URL_TEMPLATE.format(arxiv_id=self.arxiv_id)
        self.zip_extract_dir = extract_online_zip(
            url=self.src_url,
            extract_dir=os.path.join(self.extract_dir, self.arxiv_id)
        )
        self.tex_files = self._tex_files()
        self.tex_accumulation = self._accumulate_tex_files()

    def _tex_files(self):
        if self.zip_extract_dir:
            return dir_extension_files(self.zip_extract_dir)
        return []

    def _accumulate_tex_files(self):
        content_sb = []
        for tex_file in self.tex_files:
            with open(tex_file, 'r') as f:
                content = f.read()
            file_name = tex_file.replace(self.extract_dir, '')
            tex_file_content = self.TEX_ACCUMULATION_ENTRY_TEMPLATE.format(
                file_name=file_name,
                content=content
            )
            content_sb.append(tex_file_content)
        return '\n'.join(content_sb)

    def get_tex(self):
        return self.tex_accumulation
    
    def get_paper_url(self):
        return self.abs_url


if __name__ == '__main__':  # TODO: remove this
    arxiv_id = '2406.17837'
    extraction = ArxivExtraction(arxiv_id)
    print(extraction.get_tex())