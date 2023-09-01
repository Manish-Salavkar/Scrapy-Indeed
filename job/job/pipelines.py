# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy import Spider
import psycopg2
from scrapy.exceptions import DropItem

class JobPipeline:
    def process_item(self, item, spider):
        return item

class DataDuplicationPipeline:
    def __init__(self, database_config):
        self.database_config = database_config

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            database_config={
                'database': 'scrapy_data',
                'user': 'postgres',
                'password': 'man',
                'host': 'localhost',
                'port': '2018',
            }
        )
    
    def open_spider(self, spider):
        self.conn = psycopg2.connect(**self.database_config)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("SELECT * FROM scraped_data WHERE url = %s", (item['url'],))
            existing_data = self.cursor.fetchone()
            if existing_data is not None:
                raise DropItem(f"Duplicate item found: {item['url']}")
        except Exception as e:
            spider.logger.error(f"Error checking data existence: {e}")
        return item
    
class DatabaseSavePipeline:
    def __init__(self, database_config):
        self.database_config = database_config

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            database_config={
                'database': 'scrapy_data',
                'user': 'postgres',
                'password': 'man',
                'host': 'localhost',
                'port': '2018',
            }
        )
    
    def open_spider(self, spider):
        self.conn = psycopg2.connect(**self.database_config)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """
                INSERT INTO scraped_data (date, job_title, company_name, company_location, salary, job_description, url)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    item['date'],
                    item['job_title'],
                    item['company_name'],
                    item['company_location'],
                    item['salary'],
                    item['job_description'],
                    item['url'],
                ),
            )
            self.conn.commit()
        except Exception as e:
            spider.logger.error(f"Error saving data to the database: {e}")
        return item