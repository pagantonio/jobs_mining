import scrapy


class JobLinksSpider(scrapy.Spider):
    name = 'joblinks';
    base_url = 'https://www.indeed.com.br'
    next_page_counter = 0

    def start_requests(self):
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = self.base_url + '/empregos?q=' + tag
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        jobs = response.css('div[data-tn-component=organicJob]')
        for job in jobs:
            yield {
                'link': job.css('h2 a::attr(href)').extract_first()
            }
        self.next_page_counter = self.next_page_counter + 10;
        selector = 'a[href*="start=' + str(self.next_page_counter) + '"]'
        page_links = response.css(selector)
        next_page = page_links.css('a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
