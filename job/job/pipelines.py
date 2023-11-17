# job\job\pipelines.py
from scrapy.exceptions import DropItem
from scrapy import Spider
import psycopg2
from scrapy.exceptions import DropItem
from job.items import JobItem
from job.settings import DATABASE_CONFIG
from job.database_manager import database_manager
import re

                
    
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
            jobid = None

            jobid_match = re.search(r'fccid=([^&]+)', final_url)
            if jobid_match:
                jobid = jobid_match.group(1)

            cursor.execute("SELECT jobid FROM scraped_data WHERE jobid = %s", (jobid,))
            existing_jobid = cursor.fetchone()

            if existing_jobid is not None:
                raise DropItem(f"Duplicate jobid found: {jobid}")

            
            
            cursor.execute(
                """
                INSERT INTO scraped_data (jobid, date_scraped, job_title, company_name, company_location, salary, job_description, url)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    jobid,
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
        
        finally:
            database_manager.close_connection()
            
        return item