import scrapy
from urllib.parse import urlencode, urljoin, unquote
from job.items import DataItem
from job.settings import SCRAPEOPS_API_KEY
from datetime import datetime
from time import sleep



KEY = SCRAPEOPS_API_KEY
JOBS = ['fresher+engineering']
LOCATIONS = ['Panvel']

def get_scrapeops_url(url):
    payload = {'api_key': KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url



class ListingsspiderSpider(scrapy.Spider):
    name = "listingsspider"

    def start_requests(self):
        for job in JOBS:
            for location in LOCATIONS:
                search_url = f"https://in.indeed.com/jobs?q={job}&l={location}&fromage=1"
                yield scrapy.Request(search_url, callback=self.parse)

    def parse_final_link(self, response):

        extracted_date = datetime.now().date().isoformat()



        item = DataItem()
        item['date'] = extracted_date
        item['job_title'] = response.css('div.jobsearch-JobInfoHeader-title-container h1 span::text').get()
        item['company_name'] = response.css('a.css-1f8zkg3::text').get()
        item['company_location'] = response.css('div.css-6z8o9s div::text').get()
        item['salary'] = response.css('span.css-2iqe2o::text').get()
        all_text = response.css('div#jobDescriptionText *::text').getall()
        item['job_description'] = ' '.join(all_text).strip()
        item['url'] = response.url

        yield item

    def parse(self, response):

        widget_links = response.css('div.job_seen_beacon a.jcs-JobTitle::attr(href)').extract()

        for widget_link in widget_links:
            widget_url = response.urljoin(widget_link)
            proxy_widget_url = get_scrapeops_url(widget_url)
            original_widget_url = unquote(proxy_widget_url)

            x = '&url='
            if x in original_widget_url:
                final_link = original_widget_url.split(x)[1]

                yield scrapy.Request(final_link, callback=self.parse_final_link, meta={'delay': 10})
                

        pagination_links = response.css('nav[aria-label=pagination] a::attr(href)').extract()
        for next_page in pagination_links:
            if next_page:
                yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
            else:
                self.logger.info("Reached last page. No pagination links further")