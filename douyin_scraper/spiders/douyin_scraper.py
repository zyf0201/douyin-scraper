class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com']

    def parse(self, response):
        # 处理爬取到的数据
        self.log('Visited: ' + response.url)
        # 示例：提取标题
        title = response.xpath('//title/text()').get()
        yield {'title': title}