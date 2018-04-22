import re

from scrapy import Selector, Spider, Request
from jobs_mining.items import JobItem


class IndeedJobsSpider(Spider):
    BASE_URL = 'https://www.indeed.com.br'
    DETAILS_URL = BASE_URL + '/ver-emprego?'
    COUNTRY = 'Brasil'
    SOURCE = 'Indeed.com.br'

    name = 'indeed'
    query = ''
    location = ''
    next_page_counter = 0

    def start_requests(self):
        self.query = getattr(self, 'q', None)
        self.location = getattr(self, 'l', None)

        if self.query and self.location:
            url = self.BASE_URL + '/empregos' + '?q=' + self.query + '&l=' + self.location
            self.logger.info(f'Fetching URL, url={url}')
            yield Request(url, self.parse)

    def parse(self, response):
        def extract(obj, query, multiline=False):
            values = obj.css(query).extract()
            if len(values) > 0:
                output = ''.join(values) if multiline else values[0]
                return output.strip()
            else:
                return ''

        # lista com as ofertas da pagina atual
        jobs = Selector(response).css('div[data-tn-component=organicJob]')

        for job in jobs:
            item = JobItem()
            item.source = self.SOURCE
            item.country = self.COUNTRY
            item.state_short = self.location
            item.tag = self.query

            item.title = extract(job, 'h2.jobtitle a::attr(title)')
            item.location = extract(job, 'span.location::text')
            item.short_summary = extract(job, 'span.summary::text', True)

            # existem casos em que a companhia esta em um <span> ou em um link <a>
            company = extract(job, 'span.company::text')
            if not company:
                company = extract(job, 'span.company a::text')
            item.company = company

            # este campo e atribuido no StatePipeline
            item.state_long = ''

            # este campo e atribuido na requisicao para a pagina com os detalhes
            item.long_summary = ''

            details_href = job.css('h2.jobtitle a::attr(href)').extract_first()
            long_summary_url = self.get_long_summary_url(details_href)

            yield Request(long_summary_url, self.parse_long_summary, meta={'item': item})

        self.next_page_counter = self.next_page_counter + 10

        selector = 'a[href*="start=' + str(self.next_page_counter) + '"]'
        page_links = response.css(selector)
        next_page = page_links.css('a::attr(href)').extract_first()

        self.logger.info(f'Fetching next page, url={next_page}')
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse)

    def parse_long_summary(self, response):
        lines = response.xpath('//span[@id="job_summary"]//text()').extract()
        long_summary = ''.join(lines).strip()
        item = response.meta['item']
        item['long_summary'] = long_summary
        return item

    # o link para os detalhes da vaga podem ter 2 tipos:
    # - um token 'jk' seguido por um identificador, ex: 'https://www.indeed.com.br/rc/clk?jk=7afcb7c70157697c',
    #   neste caso captura-se apenas o token
    # - ou um link que nao contem este token, neste caso captura-se o link inteiro
    def get_long_summary_url(self, href):
        if '/rc' in href:
            href = re.search('(jk=.+)', href).group(1)
            url = self.DETAILS_URL + href
        else:
            url = self.BASE_URL + href
        return url
