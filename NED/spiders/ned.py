import scrapy
from bs4 import BeautifulSoup
from scrapy import Request
from NED.items import NedItem


def parse_article(response):
    soup = BeautifulSoup(response.text, 'lxml')
    text = ""
    title = soup.find('h1', {'class', 'entry-title'}).text
    for p in soup.find_all('p'):
        text += p.text
    result = NedItem()
    result['text'] = text
    result['title'] = title
    yield result


class NedSpider(scrapy.Spider):
    name = 'ned'
    allowed_domains = ['ned.org']
    start_urls = [f'https://www.ned.org/category/news/page/{page}/' for page in range(1, 100)]

    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.text, 'lxml')
        url_list = soup.select("p.view_more > a")
        for url in url_list:
            url = url.attrs.get('href')
            yield Request(url, dont_filter=True, callback=parse_article)