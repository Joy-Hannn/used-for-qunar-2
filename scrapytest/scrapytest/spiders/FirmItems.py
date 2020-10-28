#引入文件
import scrapy

class FirmItem(scrapy.Item):
    #公司名称
    name = scrapy.Field()
    #公司url
    url = scrapy.Field()

    # 定义一个item


