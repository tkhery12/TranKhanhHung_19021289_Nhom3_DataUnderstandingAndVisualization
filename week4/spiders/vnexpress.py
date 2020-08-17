import json
import scrapy
from datetime import datetime

OUTPUT_FILENAME = 'output/vnexpress3_{}.json'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))


class VnexpressSpider(scrapy.Spider):
    name = 'vnexpress3'
    allowed_domains = ['vnexpress.net']
    start_urls = ['https://vnexpress.net']
    CRAWLED_COUNT = 0

    def parse(self, response):
        if response.status == 200 and response.css('meta[name="tt_page_type"]::attr("content")').get() == 'article':
            print('Crawling from:', response.url)
            data = {
                'link': response.url,
                'title': response.css('h1.title-detail::text').get(),
                'description': response.css('p.description::text').get(),

                'content': '\n'.join([
                    ''.join(c.css('*::text').getall())
                    for c in response.css('article.fck_detail p.Normal')
                ]),

                'category': response.css('meta[itemprop="articleSection"]::attr("content")').get(),
                'pub_date': float(response.css('meta[name="its_publication"]::attr("content")').get()),
                'keywords': [
                    k.strip() for k in response.css('meta[name="keywords"]::attr("content")').get().split(',')
                ],
                'tags': [
                    k.strip() for k in response.css('meta[name="its_tag"]::attr("content")').get().split(',')
                ],
            }
            with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write('\n')
                self.CRAWLED_COUNT += 1
                self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
                print('SUCCESS:', response.url)

        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, callback=self.parse)
