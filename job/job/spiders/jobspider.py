# import scrapy
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
# from urllib.parse import urlencode



# def get_scrapeops_url(url):
#     payload = {'api_key': KEY, 'url': url}
#     proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
#     return proxy_url


# class JobspiderSpider(CrawlSpider):
#     name = "jobspider"

#     allowed_domains = ["in.indeed.com"]
#     start_urls = ["https://in.indeed.com/jobs?q=it&l=Panvel%2C+Maharashtra&fromage=1"]

#     rules = (
#         Rule(LinkExtractor(allow=r'\/rc\/clk\?jk=\w+'), callback='parse_job'),
#     )

#     def parse_job(self, response):
#         pass


import scrapy
from urllib.parse import urlencode, unquote
from datetime import datetime
import json

KEY = 'API_KEY'

def get_scrapeops_url(url):
    payload = {'api_key': KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    start_urls = ["https://in.indeed.com/jobs?q=it&l=Panvel%2C+Maharashtra&fromage=3"]

    def parse(self, response):
        extracted_date = datetime.now().date()
        extracted_date_str = extracted_date.isoformat()

        widget_links = response.css('div.job_seen_beacon a.jcs-JobTitle::attr(href)').extract()
        scraped_data = []
        with open(r'C:\Users\Tanmay\Documents\tempscrape\job\job\scraped_data\data.json', 'r') as json_file:
                    data = json.load(json_file)
                    existing_links = set(item['link'] for item in data)
        
        for widget_link in widget_links:
            widget_url = response.urljoin(widget_link)
    
            proxy_widget_url = get_scrapeops_url(widget_url)

            original_widget_url = unquote(proxy_widget_url)

            x = '&url='

            if x in original_widget_url:
                final_link = original_widget_url.split(x)[1]

                if final_link not in existing_links:
                    scraped_data.append ({
                        "date": extracted_date_str,
                        "link": final_link
                    })
                    existing_links.add(final_link)

        with open(r'C:\Users\Tanmay\Documents\tempscrape\job\job\scraped_data\data.json', 'w') as json_file:
            all_data = data + scraped_data
            json.dump(all_data, json_file, indent=2, ensure_ascii=False)