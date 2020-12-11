'''program to scrape hackernews'''

import pprint
import requests
from bs4 import BeautifulSoup

def get_multiple_pages(pages):
    '''get multiple pages from hacker rank ending with {pages} page'''

    for pnumber in range(1, pages+1):
        links1 = []
        subtext1 = []
        res = requests.get(f'https://news.ycombinator.com/news?p={pnumber}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')

        print(pnumber)
        print(len(links))
        print(len(subtext))

        links1.append(links)
        subtext1.append(subtext)
        print(links)
        print(subtext)
        links2 = ''.join([str(elem) for elem in links1])
        subtext2 = ''.join([str(elem) for elem in subtext1])

    print(len(links1))
    print(len(subtext1))
    return create_custom_hn(links2, subtext2)

def sort_stories_by_votes(hnlist):
    '''sorts the stories by votes'''
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links2, subtext2):
    '''create list and append results to list'''
    hn = []
    for idx, item in enumerate(links2):
        title = item.getText()
        href = item.get('href', 'None')
        vote = subtext2[idx].select('.score')
        if len(vote) != 0:
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                #print(points)
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)

pprint.pprint(get_multiple_pages(2))
