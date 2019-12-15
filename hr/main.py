#!/usr/bin/python3
import sys

if __name__ == '__main__':
    top_ten = __import__('req').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
