import json
from pathlib import Path

class Poem():
    """
    Stores poem data, and allows printing in a pretty format for reading poetry
    """
    def __init__(self, author: str, title: str, text: str, sentiment: str, category: str):
        self.author = author
        self.title = title
        self.text = text
        self.sentiment = sentiment
        self.category = category
    
    def display(self):
        """
        Prints the stored poem, alongside its title and author
        """
        print(f"\n{self.title}\n\n{self.text}\n\n\n-- {self.author}\n")

def _read_poems_file(poems_path):
    path = Path(poems_path)
    with open(path) as f:
        poems = json.load(f)
    return poems

def _construct_poem(poem_blob):
    poem = Poem(
        author = poem_blob["author"],
        title = poem_blob["title"],
        text = poem_blob["text"],
        sentiment = poem_blob["sentiment"],
        category = poem_blob["category"]
    )
    return poem

def get_poems(path):
    poem_json = _read_poems_file(path)
    poems = [_construct_poem(blob) for blob in poem_json]
    return poems
