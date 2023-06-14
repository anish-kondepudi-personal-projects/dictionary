from .page import Page

class Dictionary:

    def __init__(self, words: list[str]) -> None:
        self.pages: list[Page] = []
        for i in range(0, len(words), Page.MAX_WORDS):
            page_words = words[i: min(i + Page.MAX_WORDS, len(words))]
            page = Page(page_words)
            self.pages.append(page)

    def get_page(self, page_number: int) -> list[str]:
        assert 0 <= page_number < len(self.pages)
        return self.pages[page_number - 1].words
