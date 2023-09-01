# url = "https://proxy.scrapeops.io/v1/?api_key=44877922-3247-4a55-9c5e-e33e03852085&url=https://in.indeed.com/rc/clk?jk=e3d20da04d95eaa2&fccid=721030124be3382c&vjs=3"

# x = '&url='

# if x in url:
#     result = url.split(x)[1]
# print(result)

# import json
# import re

# # Load the JSON data from your file
# with open(r'C:\Users\Tanmay\Documents\tempscrape\job\job\spiders\data.json', 'r') as json_file:
#     data = json.load(json_file)

# # Define a function to clean and format job descriptions
# def clean_and_format_job_description(description):
#     # Split the description by line breaks
#     lines = description.split('\n')
    
#     # Initialize variables to store cleaned data
#     cleaned_description = []
#     skills_and_qualifications = []
#     job_details = []
    
#     # Iterate through each line
#     for line in lines:
#         # Remove leading and trailing whitespaces
#         line = line.strip()
        
#         # Check if the line contains useful information
#         if line:
#             # Use regular expressions to identify skills and qualifications
#             if re.search(r'^\w+ Skills:', line):
#                 skills_and_qualifications.extend(line.split(':')[1].split(','))
#             # Use regular expressions to identify job details
#             elif re.search(r'^Job Type:', line) or re.search(r'^Salary:', line) or re.search(r'^Benefits:', line) or re.search(r'^Schedule:', line) or re.search(r'^Experience:', line) or re.search(r'^Willingness to travel:', line):
#                 job_details.append(line)
#             else:
#                 cleaned_description.append(line)
    
#     # Join the cleaned lines into a single string
#     cleaned_description = '\n'.join(cleaned_description)
    
#     # Return the cleaned description, skills, and job details
#     return cleaned_description, skills_and_qualifications, job_details

# # Example: Clean and format the first job description
# cleaned_desc, skills, details = clean_and_format_job_description(data[0]['job_description'])

# # Print the cleaned data
# print("Cleaned Description:")
# print(cleaned_desc)
# print("\nSkills and Qualifications:")
# print(skills)
# print("\nJob Details:")
# print(details)    

# def process_job_description(x):
#     r = '\n'

#     return x

    


# x =  "Job Description\n   Job title : IT Recruiter \n   Job Location : Belapur (Navi Mumbai) \n   Job Type : Full-time \n   Company Name : Chabeztech Pvt Ltd \n   About Us : \n   ChabezTech is a fast growing IT Staffing & Software development solution firm providing services in IT Services & Technology industry. ChabezTech is headquartered in Pennsylvania with office in India based in Mumbai and Pune with a client base all around the world. ChabezTech provide a wide variety of IT Staffing & Software development solution. We have an offshore hub for back end operations and support for clients all over the world. \n   Company Website : https://chabeztech.com/ \n   Role \n   Manage the entire life cycle of the recruitment process for clients in the Indian Market. \n   Summary \n   Work closely with the Recruiting leads and hiring managers. \n   Work on strategic global hiring programs. \n   Develop an action plan for recruiting the best fit for the organization. \n   Procure people for different IT Requirements. \n   Use niche platforms related to IT, to source potential candidates. \n   Personally conduct interviews, document the same, and report as the need arises. \n   In addition to executing individual responsibility should be able to work in unison with the other departments with the Company’s growth perspective in mind. \n   Keeping abreast of the industry trends. \n  \n   Requirements \n   Minimum experience of 1 year in IT Recruitment \n   Good verbal and Written Communication \n \n  \n  \n \n Additional Information\n   All your information will be kept confidential according to EEO guidelines."

# print(process_job_description(x))

# "Job ID:  37655 |  Location:  Airoli, Maharashtra, India \n    \n    \n   Responsible for translating business requirements into detailed function specifications of the respective Sub-Domain. Is responsible for the delivery of global IT business application services, including consulting, projects and maintenance. \n    \n     What will you be doing?  \n   \n   Development and implementation of Sub-Domain product  \n   1.Setting up (customising) the corresponding systems configuration and documentation  \n   2. Define project brief, initial cost assessment of projects, and the integration of other projects, and in potentially suppliers  \n   3. Analyse, evaluate and define system requirements and change requests  \n   4. Plan and monitor small and medium projects (incl. Resources) towards OTIF implementation of selected solution (On Time In Full) \n    \n    \n   Ensure effective support of Sub-Domain products  \n   1. Responsible for the implementation of service/product roadmap, ensuring alignment with business needs  \n   2. Responsible for specifying required service levels based on business criticality  \n   3. Responsible to ensure that service levels are met  \n   4. Responsible of deliver support/maintenance services according to agreed service levels and defined KPIs  \n   5. Plans and coordinates project resources  \n   6. Creation and development and/or implementation of user training/instruction  \n   7. Does Monitoring of and assures ticket handling in accordance with defined service level \n    \n    \n   Increase of efficiency  \n   1. Analyze the information requirements and information flows required to support better processes  \n   2. Identify process waste and improve within given application to ensure better data quality/connectivity \n    \n    \n   Leadership / People Management  \n   1. May lead a small team of IT Consultants in progressing the detail of the projects  \n   2. Effectively manage vendors to maintain support and deliver new features in a cost effective manner. \n    \n    \n   What do we expect?  \n   \n   Education:  \n   Higher education in a technical or business direction (e.g., computer science or MBA) at bachelor’s level or higher.  \n   At least 5 years of experience in the application environment and development tools relevant to the job \n    \n    \n   Business experience:  \n   More than 5 years of experience with relevant IT systems.  \n   Good consulting and project management skills, is familiar with an international, multi- cultural environment  \n   If needed: Specific SubDomain relevant knowledge \n    \n    \n   Additional Qualifications:  \n   Languages: Good written and spoken English is a must, other international languages desired  \n   International Cross-Culture experience  \n   Can deal with constantly changing problems, processes and technologies  \n   Works independently and proactively  \n   Communicative, initiates and maintains contacts with relevant business partners  \n   Analytical thinking, argues convincingly and fact-based \n    \n    \n   What´s in it for you?  \n   \n   \n    Be part of an amazing team, who will be there to support you.  \n    A forward-looking company, with a culture of innovation and a strong portfolio in sustainable technologies.  \n    Long term growth opportunity  \n    Employee Wellbeing & Assistance Program  \n    Work-Life Balance  \n    Hybrid Work Model  \n    On-site Recreation Center  \n    30 Days Annual Paid Leaves  \n    In-house Gym  \n    Subsidized Cafeteria Meals  \n    Centralized Company Transport For Designated Routes  \n    On-site Employee Health Center  \n    Group Medical Insurance  \n    Day Care facility (100% sponsored by Clariant)  \n    Inclusive Work Environment  \n    Ongoing Professional Development Opportunities  \n    Approachable Leadership  \n    Speak Up Culture \n   \n    \n    \n     \n   \n   Clariant is a focused, sustainable and innovative specialty chemical company based in Muttenz near Basel/Switzerland. On 31 December 2021, Clariant totaled a staff number of 11 537 and recorded sales of CHF 4.372 billion in the fiscal year for its continuing businesses. The company reports in three business areas: Care Chemicals, Catalysis and Natural Resources. Clariant’s corporate strategy is led by the overarching purpose of ‘Greater chemistry – between people and planet’ and reflects the importance of connecting customer focus, innovation, sustainability, and people. Join us and help create sustainable value through chemistry for customers all over the globe."


import psycopg2
from psycopg2 import Error

database_config={
                'database': 'scrapy_data',
                'user': 'postgres',
                'password': 'man',
                'host': 'localhost',
                'port': '2018',
            }

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(**database_config)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Define your SQL query
    sql_query = "SELECT job_description FROM public.scraped_data WHERE company_name = 'IBSAR Institute of Business Studies and Research'"

    # Execute the SQL query
    cursor.execute(sql_query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the retrieved data
    for row in rows:
        print(row)

except Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()