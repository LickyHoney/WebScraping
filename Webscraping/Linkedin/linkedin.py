from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
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
        if date_string.endswith("."):
            # If year is not included in date_string, use the current year
            date_obj = datetime.strptime(date_string, "%d.%m.")
            date_obj = date_obj.replace(year=current_year)
        else:
            if check_datetime_format(date_string, format_string_linkedin):
                date_obj = datetime.strptime(date_string, "%Y-%m-%d")
                date_obj = date_obj.replace(year=date_obj.year)
            else:

                date_obj = datetime.strptime(date_string, "%d.%m.%Y")
                date_obj = date_obj.replace(year=date_obj.year)
    

        return date_obj.strftime("%d-%m-%y")
    except ValueError:
        # If the input date_string is None or not in the expected format
        return None
# Load keywords from a JSON file
with open('../keywords.json', 'r') as file:
        keywords = json.load(file)
        print (keywords)

    # Create a list to store the extracted job data
jobs = []

# Perform web scraping for eacj keyword
for keyword in keywords:
        # Format the keyword to be used in the URL
        formatted_keyword = keyword.replace(' ', '%20')
        

        
        url = f'https://www.linkedin.com/jobs/search?keywords={formatted_keyword}&location=Finland'
        print(url)

        
        # Send a GET request to the indeed search page with headers
        
        response = requests.get(url)
        response.encoding = 'utf-8'
       
       
        soup = BeautifulSoup(response.content, 'html.parser')

        res=soup.title

        #print (soup)
        
        job_listings = soup.find_all ('div', class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")
        

        
       # Extract relevant data from each job listing
        for listing in job_listings:
            
            
            title = listing.find("h3", class_="base-search-card__title").text.strip()
    
            link = listing.find("a")["href"]

            company = listing.find("h4", class_="base-search-card__subtitle").text.strip()

            location = listing.find("span", class_="job-search-card__location").text.strip()

            job_date = listing.find("time")

            date = job_date.get('datetime')

            date_test = convert_date_format(date)
            
   # Create a dictionary for the job data

            job_data = {

                "title": title,

                "link": link,

                "company": company,

                "location": location,

                "date": date_test

            }

            # Add the job data to the list

            jobs.append(job_data)

    #Save the data in a JSON file
    # with open('jobs_linkedin.json', 'w') as file:
    #     json.dump(jobs, file, indent=4)

with open("jobs_linkedin.json", "w", encoding="utf-8") as outfile:
        json.dump(jobs, outfile, indent=4, ensure_ascii=False)

    



