# -*- coding: UTF-8 -*-
import scrapy
class DmozItem(scrapy.Item):
    title = scrapy.Field()

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://localhost/",
    ]

    def parse(self, response):
        print '------------------------------------------------------------------'
        # print response.body
        # print response.css('p')
        # 获取p内容 返回列表

        # print response.css('p')
        # pprint response.xpath('//p')
        # google浏览器可以直接copy xpath
        # 取class为bb的div
        div = response.xpath('//div[contains(@class, "aa")]')
        # 取div下所有的p
        # for p in div.xpath('.//p/text()'):
            # print p
            # print p.extract()
        # 取div下所有class包含【字符串'cc'+数字】的p的class属性内容
        for p in div.xpath('.//p[re:test(@class, "cc\d$")]/@class'):
            print p
            print p.extract()

        # 取div下直属的p的内容
        for p in div.xpath('p/text()'):
            print p
            print p.extract()

        print '=================================================================='
        # 取所有p
        for p in response.css('p::text'):
            print p
            print p.extract()
        # 取class为aa下的  class为cc下的 class为cc2的p的 class属性的内容 ；空格可代替为 >
        for p in response.css('.aa .cc p.cc2::attr(class)'):
            print p
            print p.extract()

        print '=================================================================='
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     print response.url
        #     print ----------------------
        #     print filename
        #     f.write(response.body)