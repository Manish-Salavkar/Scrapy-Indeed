# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(scrapy.Item):
    date = scrapy.Field()
    final_link = scrapy.Field()


class DataItem(scrapy.Item):
    date = scrapy.Field()
    job_title = scrapy.Field()
    company_name = scrapy.Field()
    company_location = scrapy.Field()
    salary = scrapy.Field()
    job_description = scrapy.Field()
    url = scrapy.Field()