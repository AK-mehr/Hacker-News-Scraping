import requests
from bs4 import BeautifulSoup
import pprint

for page in range(1, 10):
    res = requests.get('https://news.ycombinator.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')


def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key= lambda k: k['points'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for inx, item in enumerate(links):
        title = item.getText()
        href = item.get('href')
        vote = subtext[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'points': points})
    return sort_stories_by_vote(hn)


pprint.pprint(create_custom_hn(links, subtext))

