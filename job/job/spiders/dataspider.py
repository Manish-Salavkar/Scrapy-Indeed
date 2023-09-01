import scrapy
import json
from urllib.parse import urlencode, unquote
from datetime import datetime
from job.items import DataItem

KEY = 'API_KEY'

def get_scrapeops_url(url):
    payload = {'api_key': KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class DataspiderSpider(scrapy.Spider):
    name = "dataspider"
    # allowed_domains = ["in.indeed.com"]
    # start_urls = ["https://in.indeed.com"]
    max_retries = 2

    def start_requests(self):
        
        with open(r"C:\Users\Tanmay\Documents\tempscrape\job\job\spiders\data.json", 'r') as link_file:
            links = json.load(link_file)

        for link in links:
            url = link.get('link')
            date = link.get('date')
            if url:
                proxy_url = get_scrapeops_url(url)
                self.logger.info(f"Processing URL: {url}")
                yield scrapy.Request(url, callback=self.parse, meta={'proxy_url': proxy_url, 'date':date})

    # def parse(self, response):

    #     job_title = response.css('div.jobsearch-JobInfoHeader-title-container h1 span::text').get()
    #     company_name = response.css('a.css-1f8zkg3::text').get()
    #     company_location = response.css('div.css-6z8o9s div::text').get()
    #     salary = response.css('span.css-2iqe2o::text').get()
    #     all_text = response.css('div#jobDescriptionText *::text').getall()
    #     job_description_text = ' '.join(all_text).strip()

    #     date = response.meta.get('date')
    #     yield {
    #         'date': date,
    #         'title': job_title,
    #         'company': company_name,
    #         'location': company_location,
    #         'salary': salary,
    #         'job_description': job_description_text,
    #         'url': response.url,
    #     }

    def parse(self, response):
        item = DataItem()  # Use the DataItem class
        item['date'] = response.meta.get('date')
        item['job_title'] = response.css('div.jobsearch-JobInfoHeader-title-container h1 span::text').get()
        item['company_name'] = response.css('a.css-1f8zkg3::text').get()
        item['company_location'] = response.css('div.css-6z8o9s div::text').get()
        item['salary'] = response.css('span.css-2iqe2o::text').get()
        all_text = response.css('div#jobDescriptionText *::text').getall()
        item['job_description'] = ' '.join(all_text).strip()
        item['url'] = response.url

        yield item
