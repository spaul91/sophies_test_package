from abc import ABC, abstractmethod

class PoemFilter(ABC):
    @abstractmethod
    def filter(self):
        pass

class AuthorFilter(PoemFilter):
    def filter(self, author: str, poems: list):
        return [poem for poem in poems if poem.author == author]

class SentimentFilter(PoemFilter):
    def filter(self, sentiment: str, poems: list) -> list:
        return [poem for poem in poems if poem.sentiment == sentiment]
    
class CategoryFilter(PoemFilter):
    def filter(self, category: str, poems: list) -> list:
        return [poem for poem in poems if poem.category == category]