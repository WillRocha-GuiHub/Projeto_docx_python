from typing import List
from dataclasses import dataclass, field
from docx import Document
from docx.opc.exceptions import PackageNotFoundError

@dataclass
class FormatFilter:
    bold: List or str = field(default_factory = lambda: ["None", "True"])

class ReadDocFile:
    def __init__(self, filename):
        self.fname = filename
        self.loaded_document = None
        self.content = None

    def load_document(self):
        try:
            self.loaded_document = Document(self.fname)
            self.content = self.get_content_as_list()
        except PackageNotFoundError as e:
            print(f"File not found: {self.fname}")
            quit()

    def get_content_as_list(self):
        return [paragraph.text for paragraph in self.loaded_document.paragraphs]

    # Devolve todos os runs do paragrafo em negrito
    def _get_bold(self, paragraph, filter):
        bold_runs = []
        for run in paragraph.runs:
            if run.bold == filter or filter is None:
                bold_runs.append(run.text) # se quiser somente o primeiro match pode dar um return run.text aqui
        return bold_runs
        
    def get_formatted_text(self, format_filter: FormatFilter):
        match_list = []
        for paragraph in self.loaded_document.paragraphs:
            bold = self._get_bold(paragraph, format_filter.bold)

            if bold:
                match_list.append(bold) # Em vez de add o paragrafo, adicionamos o return de bold
        return match_list    

if __name__ == "__main__" :
    doc = ReadDocFile("cv.docx")
    doc.load_document()

    # Find bold:
    filter1 = FormatFilter(bold="True")
    print(doc.get_formatted_text(format_filter=filter1))