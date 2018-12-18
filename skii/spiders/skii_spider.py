import re
import scrapy
from scrapy.http import Request
from skii.items import SkiiItem
from bs4 import BeautifulSoup

class Myspider(scrapy.Spider):
    name = "skii"
    start_urls = [
        'https://www.sephora.com/product/facial-treatment-essence-P375849?skuId=1850346&icid2=products%20grid:p375849',
    ]

    def parse(self, response):
        filename = 'skii.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        data = BeautifulSoup(response.body, 'lxml')
        print(data.find_all("div",class_="css-18suhml")[0].string)