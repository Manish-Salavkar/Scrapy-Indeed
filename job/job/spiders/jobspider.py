# job\job\spiders\jobspider.py
import scrapy
from urllib.parse import urlencode, unquote, urljoin
from datetime import datetime
import re
from job.settings import SCRAPEOPS_API_KEY
from job.items import JobItem

KEY = SCRAPEOPS_API_KEY
JOBS = ['it', 'manager', 'programming', 'backend', 'frontend', 'UI/UX']
LOCATIONS = ['Mumbai', 'Pune', 'Banglore', 'Chennai', 'Noida']


def get_scrapeops_url(url):
    payload = {'api_key': KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class JobspiderSpider(scrapy.Spider):
    name = "jobspider"

    def start_requests(self):
         for job in JOBS:
              for location in LOCATIONS:
                   search_url = f"https://in.indeed.com/jobs?q={job}&l={location}&fromage=1"
                   yield scrapy.Request(search_url ,callback= self.parse)
    

    def parse(self, response):
        extracted_date = datetime.now().date()
        extracted_date_str = extracted_date.isoformat()

        widget_links = response.css('div.job_seen_beacon a.jcs-JobTitle::attr(href)').extract()

        for widget_link in widget_links:
            widget_url = response.urljoin(widget_link)
            proxy_widget_url = get_scrapeops_url(widget_url)
            original_widget_url = unquote(proxy_widget_url)

            x = '&url='

            if x in original_widget_url:
                final_link = original_widget_url.split(x)[1]

                job_item = JobItem()
                job_item['date'] = extracted_date_str
                job_item['final_link'] = final_link

                yield job_item
