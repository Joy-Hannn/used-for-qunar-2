import scrapy
#引入容器
from bs4 import BeautifulSoup

from scrapytest.spiders.FirmItems import FirmItem


class MySpider(scrapy.Spider):
    #设置name
    name = "MySpider"
    #设定域名
    allowed_domains = ["https://www.nowcoder.com/intern/center"]
    #填写爬取地址
    start_urls = ["https://www.nowcoder.com/intern/center"]
    #编写爬取方法
    def parse(self, response):
        #实例一个容器保存爬取的信息
        item = FirmItem()
        html = response.text
        soup = BeautifulSoup (html, "lxml")
        print(soup.prettify())