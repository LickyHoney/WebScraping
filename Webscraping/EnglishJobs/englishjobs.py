from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
import html
# import random
# import time
from datetime import datetime


def check_datetime_format(input_string, format_string):
    try:
        # Try to parse the input string using the specified format
        datetime_obj = datetime.strptime(input_string, format_string)
        return True
    except ValueError:
        # If the parsing fails, the format doesn't match
        return False

def convert_date_format(date_string):
    try:

        # Check if the year is included in the date_string
        current_year = datetime.now().year
        format_string_linkedin = "%Y-%m-%d"
        format_string_englishjobs = "%B %d"
        if date_string.endswith("."):
            # If year is not included in date_string, use the current year
            date_obj = datetime.strptime(date_string, "%d.%m.")
            date_obj = date_obj.replace(year=current_year)
        else:
            if check_datetime_format(date_string, format_string_linkedin):
                date_obj = datetime.strptime(date_string, "%Y-%m-%d")
                date_obj = date_obj.replace(year=date_obj.year)
            else:
                if check_datetime_format(date_string, format_string_englishjobs):
                    # Combine the date string with the current year
                    full_date_str = f"{date_string}, {current_year}"

                    # Parse the full date string to a datetime object
                    date_obj = datetime.strptime(full_date_str, "%B %d, %Y")

                else:

                    date_obj = datetime.strptime(date_string, "%d.%m.%Y")
                    date_obj = date_obj.replace(year=date_obj.year)

       

        # # Format the datetime object to the desired format
        # formatted_date = date_obj.strftime("%d-%m-%y")
        # return formatted_date
    

        return date_obj.strftime("%d-%m-%y")
    except ValueError:
        # If the input date_string is None or not in the expected format
        return None
    
# def convert_to_datetime(date_str):
#     try:
#         # Assuming the current year
#         current_year = datetime.now().year

#         # Combine the date string with the current year
#         full_date_str = f"{date_str}, {current_year}"

#         # Parse the full date string to a datetime object
#         date_obj = datetime.strptime(full_date_str, "%B %d, %Y")

#         # Format the datetime object to the desired format
#         formatted_date = date_obj.strftime("%d-%m-%y")
#         return formatted_date
#     except ValueError as e:
#         print(f"Error converting date: {e}")
#         return None

# Load keywords from a JSON file
with open('../keywords.json', 'r') as file:
        keywords = json.load(file)

# Create a list to store the extracted job data
job_data = []
location='espoo'

    # Perform web scraping for eacj keyword
for keyword in keywords:
        # Format the keyword to be used in the URL
        formatted_keyword = keyword.replace(' ', '+')
        #print (keyword)

        url = f'https://englishjobs.fi/jobs/{location}?q={formatted_keyword}'
        #url = f'https://englishjobs.fi/jobs/{formatted_keyword}'
        print(url)

        # Add headers to mimic a web browser
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        # }

        # Send a GET request to the indeed search page with headers
        #response = requests.get(url, headers=headers)
        response = requests.get(url)
        response.encoding = 'utf-8'

        # Random delay to avoid triggering rate limiting
        #time.sleep(random.uniform(1,3))

        # response = requests.get(url)
        #print(response.content)
        soup = BeautifulSoup(response.content, 'html.parser')
     


        # Find all job listings on the page 
        #job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')
        #job_listings = soup.find_all('div', class_='job-list__item')
        #job_listings = soup.find_all('li', class_='job-card')
        job_listings = soup.find_all("div", class_="row job js-job")
        

        #print(job_listings)
        #print(job_link)
        
        jobs = []
        # for div in soup.find_all(name='div', attrs={'class':'row'}):
        #     for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
        #         jobs.append(a['title'])
        # print(jobs)

       # Extract relevant data from each job listing
        for listing in job_listings:
            # Extract the title, link, company, and location
            title = listing.find("div", class_="col-md-12").get_text().strip()
            job_url = listing.find("a")["href"]
            link = 'https://englishjobs.fi' + job_url
            com = listing.find("ul", class_="fa-ul")
            com_li = com.find_all('li')[0]
            loc_li = com.find_all('li')[1]
            date_li = com.find_all('li')[2]
           
            company = com_li.find('i').next_sibling.strip()
           
            location = loc_li.find('i').next_sibling.strip()
            date_test = date_li.find('i').next_sibling.strip()
            date = convert_date_format(date_test)
           
               
           
            # Create a dictionary to store the job data
            job_data = {
                "title": title,
                "link": link,
                "company": company,
                #"description": description
                "location": location,
                "date" : date

            }

            jobs.append(job_data)

    #Save the data in a JSON file
with open("jobs_englishjobs.json", "w", encoding="utf-8") as outfile:
        json.dump(jobs, outfile, indent=4, ensure_ascii=False)

    

# from flask import Flask, jsonify
# import requests
# import bs4
# from bs4 import BeautifulSoup
# import json
# import time
# import pandas as pd

# app = Flask(__name__)

# @app.route('/scrape')
# def scrape_duunitori():
#     # Load keywords from a JSON file
#     with open('keywords.json', 'r') as file:
#         keywords = json.load(file)

#     # Create a list to store the extracted job data
#     job_data = []

#     # Perform web scraping for each keyword
#     for keyword in keywords:
#         # Format the keyword to be used in the URL
#         formatted_keyword = keyword.replace(' ', '+')
#         print (formatted_keyword)
#         # Construct the URL for the Duunitori search page
#         url = f'https://www.indeed.com/jobs?q={formatted_keyword}' 


#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#         }
#         # Send a GET request to the Duunitori search page
#         response = requests.get(url, headers=headers)
#         #response = requests.get(url)
#         print(response)
#         soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")
#         #print(soup)
#         # Find all job listings on the page
#         #job_listings = soup.find_all('div', class_='jobs-list__item')
#         job_listings = soup.find_all(name='div', attrs={'class':'row'})
#         #job_listings = []
#         # for div in soup.find_all(name='div', attrs={'class':'row'}):
#         #     num = (len(sample_df))
#         # for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
#         #         job_listings.append(a['title'])
        
#         print(job_listings)
#         # Extract relevant data from each job listing
#         for job_listing in job_listings:
#             #title_element = job_listing.find('h3', class_='job-title').find('a')
#             title_element = job_listings.find(name='a', attrs={'data-tn-element':'jobTitle'})
#             # Create a dictionary to store the job data
#             data = {
#                 'title': title_element.text.strip(),
#                 'link': 'https://duunitori.fi' + title_element['href']
#             }

#             job_data.append(data)
#             #print (job_data)
#     # Save the data in a JSON file
#     with open('duunitori_data.json', 'w') as file:
#         json.dump(job_data, file)

#     return jsonify(job_data)



# if __name__ == '__main__':
#     app.run(debug=True)