from .page import Page

class Dictionary:

    def __init__(self, words: list[str]) -> None:
        self.pages = []
        for i in range(len(words), Page.MAX_WORDS):
            page_words = words[i: min(i + Page.MAX_WORDS, len(words))]
            page = Page(page_words)
            self.pages.append(page)
