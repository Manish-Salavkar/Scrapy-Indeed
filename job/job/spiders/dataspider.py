# job\job\spiders\dataspider.py
import scrapy
import json
from urllib.parse import urlencode, unquote
from datetime import datetime
from job.items import DataItem
from job.settings import SCRAPEOPS_API_KEY
import psycopg2
from job.database_manager import database_manager

KEY = SCRAPEOPS_API_KEY

def get_scrapeops_url(url):
    payload = {'api_key': KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class DataspiderSpider(scrapy.Spider):
    name = "dataspider"

    def start_requests(self):

        connection, cursor = database_manager.get_connection()

        try:
            cursor.execute("SELECT final_link, date FROM link_data")
            urls_and_dates = cursor.fetchall()
            
            for url, date in urls_and_dates:
                if url:
                    proxy_url = get_scrapeops_url(url)
                    self.logger.info(f"Processing URL: {url}")
                    yield scrapy.Request(url, callback=self.parse, meta={'proxy_url': proxy_url, 'date': date})
        finally:
            database_manager.close_connection()

    def parse(self, response):
        item = DataItem()
        item['date'] = response.meta.get('date')
        item['job_title'] = response.css('div.jobsearch-JobInfoHeader-title-container h1 span::text').get()
        item['company_name'] = response.css('a.css-1f8zkg3::text').get()
        item['company_location'] = response.css('div.css-6z8o9s div::text').get()
        item['salary'] = response.css('span.css-2iqe2o::text').get()
        all_text = response.css('div#jobDescriptionText *::text').getall()
        item['job_description'] = ' '.join(all_text).strip()
        item['url'] = response.url

        yield item
