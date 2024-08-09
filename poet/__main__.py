import argparse
import random
import sys
from .poem import get_poems
from .filters import *

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--poems")
    parser.add_argument("-t", "--filter-type", choices=["author", "sentiment", "category"], required=False)
    parser.add_argument("-e", "--filter-expression")
    parser.add_argument("-s", "--show-search-terms", required=False, action="store_true")

    args = parser.parse_args()

    return args

def comma_sep_info(what, poems_list):
    """
    docstring because vim is complaining
    """
    return(",".join({getattr(poem, what) for poem in poems_list}))

if __name__ == "__main__":
    args = parse_arguments()

    poems = get_poems(args.poems)

    if args.show_search_terms:
        print("EXPRESSIONS:")
        print("Sentiments:", comma_sep_info("sentiment", poems))
        print("Authors:", comma_sep_info("author", poems))
        print("Categories:", comma_sep_info("category", poems))
        sys.exit(0)

    if args.filter_type:
        if args.filter_type == "author":
            poem_filter = AuthorFilter()
            poems = poem_filter.filter(author=args.filter_expression, poems=poems)
        
        elif args.filter_type == "sentiment":
            poem_filter = SentimentFilter()
            poems = poem_filter.filter(sentiment=args.filter_expression, poems=poems)
        
        elif args.filter_type == "category":
            poem_filter = CategoryFilter()
            poems = poem_filter.filter(category=args.filter_expression, poems=poems)
    

    index = random.randint(a=0, b=len(poems)-1)
    poem = poems[index]
    poem.display()
