#!/usr/bin/python3
"""query Reddit API and print tittles of first ten listed
"""
import requests


def  getMovieTitles(substr):
    num = 1
    movie_titles = []
    url_base = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + substr + '&page=' + str(num)
    head = {"user-agent": 'N'}
    r = requests.get(url_base, headers=head, allow_redirects=False)
    if r.status_code != 200:
        print(None)
    else:
        page = r.json().get('page')
        total_pages = r.json().get('total_pages')
        while int(page) <= int(total_pages):
            data = r.json().get('data')
            num = num + 1
            url_base = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + substr + '&page=' + str(num)
            r = requests.get(url_base, headers=head, allow_redirects=False)
            page = r.json().get('page')
            total_pages = r.json().get('total_pages')
            for movie in data:
                movie_titles.append(movie.get('Title'))

        return(sorted(movie_titles))

p = getMovieTitles('spiderman')
print(p)