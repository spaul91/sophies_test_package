import unittest
from poet.poem import Poem

class TestPoem(unittest.TestCase):
    def test_this_test_always_passes_cba(self):
        self.assertEqual(1, 1)
    
    def test_this_test_also_always_passes_really_cba(self):
        self.assertEqual(2, 2)
    
    def test_this_poem(self):
        poem = Poem(title="A Poem", author="A Poet", text="There once was a man from the Gower", sentiment="goofy", category="limerick") 
        self.assertEqual(poem.title, "A Poem")

if __name__ == "__main__":
    unittest.main()