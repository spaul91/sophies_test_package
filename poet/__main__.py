import argparse
import random
from .poem import get_poems
from .filters import *

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--poems")
    parser.add_argument("-t", "--filter-type", choices=["author", "sentiment", "category"], required=False)
    parser.add_argument("-e", "--filter-expression")

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = parse_arguments()

    poems = get_poems(args.poems)

    if args.filter_type:
        if args.filter_type == "author":
            filter = AuthorFilter()
            poems = filter.filter(author=args.filter_expression, poems=poems)
        
        elif args.filter_type == "sentiment":
            filter = SentimentFilter()
            poems = filter.filter(sentiment=args.filter_expression, poems=poems)
        
        if args.filter_type == "category":
            filter = CategoryFilter()
            poems = filter.filter(category=args.filter_expression, poems=poems)
    

    index = random.randint(a=0, b=len(poems)-1)
    poem = poems[index]
    poem.display()