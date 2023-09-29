from scrapy.exceptions import DropItem
from scrapy import Spider
import psycopg2
from scrapy.exceptions import DropItem
from job.items import JobItem
from job.settings import DATABASE_CONFIG
from job.database_manager import database_manager
import re

                

class DataBaseLinkPipeline:
    
    def process_item(self, item, spider):
        connection, cursor = database_manager.get_connection()

        try:
            final_link = item.get('final_link', '')
            fccid = None

            fccid_match = re.search(r'fccid=([^&]+)', final_link)
            if fccid_match:
                fccid = fccid_match.group(1)

            cursor.execute("SELECT fccid FROM link_data WHERE fccid = %s", (fccid,))
            existing_fccid = cursor.fetchone()

            if existing_fccid is None:
                cursor.execute(
                    """
                    INSERT INTO link_data (fccid, date, final_link)
                    VALUES (%s, %s, %s)
                    """,
                    (
                        fccid,
                        item['date'],
                        final_link,
                    ),
                )
                connection.commit()
            
            else:
                raise DropItem(f"Duplicate: {fccid}")
        except psycopg2.Error as e:
            spider.logger.error(f"Error saving data to the database: {e}")
        return item


    
class DatabaseSavePipeline:

    def process_item(self, item, spider):
        connection, cursor = database_manager.get_connection()
        try:
            date = item.get('date', '')
            job_title = item.get('job_title', '')
            company_name = item.get('company_name', '')
            company_location = item.get('company_location', '')
            salary = item.get('salary', '')
            job_description = item.get('job_description', '')
            url = item.get('url', '')

            final_url = item.get('url', '')
            fccid = None

            fccid_match = re.search(r'fccid=([^&]+)', final_url)
            if fccid_match:
                fccid = fccid_match.group(1)

            cursor.execute("SELECT fccid FROM scraped_data WHERE fccid = %s", (fccid,))
            existing_fccid = cursor.fetchone()

            if existing_fccid is not None:
                raise DropItem(f"Duplicate fccid found: {fccid}")

            
            
            cursor.execute(
                """
                INSERT INTO scraped_data (fccid, date, job_title, company_name, company_location, salary, job_description, url)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    fccid,
                    date,
                    job_title,
                    company_name,
                    company_location,
                    salary,
                    job_description,
                    url,
                ),
            )
            connection.commit()
        except psycopg2.Error as e:
            spider.logger.error(f"Error saving data to the database: {e}")
        return item