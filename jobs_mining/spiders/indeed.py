import re

import scrapy
from scrapy import Selector, Spider

from jobs_mining.items import JobItem


class IndeedJobsSpider(Spider):
    name = 'indeed'
    base_url = 'https://www.indeed.com.br'
    details_url = base_url + '/viewjob?'
    query = ''
    state = ''
    country = 'Brasil'
    next_page_counter = 0
    source = "Indeed.com.br"

    def start_requests(self):
        self.query = getattr(self, 'q', None)
        self.state = getattr(self, 'l', None)
        if self.query and self.state:
            url = self.base_url + '/empregos?q=' + self.query + '&l=' + self.state
            self.logger.info(url)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        def extract_string(obj, query, multiline=False):
            values = obj.css(query).extract()
            if len(values) > 0:
                output = ''.join(values) if multiline else values[0]
                return output.strip()
            else:
                return ''

        jobs = Selector(response).css('div[data-tn-component=organicJob]')

        for job in jobs:
            item = JobItem()
            item['title'] = extract_string(job, 'h2.jobtitle a::attr(title)')
            company = extract_string(job, 'span.company::text')
            item['company'] = company if company else extract_string(job, 'span.company a::text')
            item['location'] = extract_string(job, 'span.location::text')
            item['state_short'] = self.state
            item['state_long'] = ''
            item['country'] = self.country
            item['short_summary'] = extract_string(job, 'span.summary::text', True)
            item['long_summary'] = ''
            item['tag'] = self.query
            item['source'] = self.source

            href = job.css('h2.jobtitle a::attr(href)').extract_first()
            long_summary_url = self.generate_long_summary_url(href)

            yield scrapy.Request(long_summary_url, self.parse_long_summary, meta={'item': item})

        self.next_page_counter = self.next_page_counter + 10
        selector = 'a[href*="start=' + str(self.next_page_counter) + '"]'
        page_links = response.css(selector)
        next_page = page_links.css('a::attr(href)').extract_first()
        self.logger.info(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_long_summary(self, response):
        lines = response.xpath('//span[@id="job_summary"]//text()').extract()
        long_summary = ''.join(lines).strip()
        item = response.meta['item']
        item['long_summary'] = long_summary
        return item

    def generate_long_summary_url(self, href):
        if '/rc' in href:
            href = re.search('(jk=.+)', href).group(1)
            url = self.details_url + href
        else:
            url = self.base_url + href
        return url
