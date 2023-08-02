from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
import re
import html
from datetime import datetime
from googletrans import Translator


app = Flask(__name__)



def convert_date_format(date_string):
    try:
        # Parse the date string into a datetime object
        
        
        # Check if the year is included in the date_string
        current_year = datetime.now().year
        if date_string.endswith("."):
            # If year is not included in date_string, use the current year
            date_obj = datetime.strptime(date_string, "%d.%m.")
            date_obj = date_obj.replace(year=current_year)
        else:
            #if date_string.endswith("%Y"):
            # date_obj = datetime.strptime(date_string, "%d.%m.%Y")
            date_obj = datetime.strptime(date_string, "%d.%m.%Y")
            date_obj = date_obj.replace(year=date_obj.year)

        return date_obj.strftime("%d-%m-%y")
    except ValueError:
        # If the input date_string is None or not in the expected format
        return None
    

#@app.route('/scrape')
#def scrape_duunitori():
# Load keywords from a JSON file
with open('../keywords.json', 'r') as file:
        keywords = json.load(file)

# Create a list to store the extracted job data
job_data = []
location = "Espoo"
target_language="en"

duunitori_url = f'https://duunitori.fi/tyopaikat/{location}/'

# Perform web scraping for eacj keyword
for keyword in keywords:
        # Format the keyword to be used in the URL
        formatted_keyword = keyword.replace(' ', '+')
        #print (keyword)

        # Construct the URL for the indeed search page
        print(duunitori_url)
        #url = f'https://duunitori.fi/tyopaikat?haku={formatted_keyword}'
        url= duunitori_url+formatted_keyword
        print (url)

        

       
        response = requests.get(url)
        response.encoding= 'utf-8'

       
        soup = BeautifulSoup(response.content, 'html.parser')
       # print(soup)

        # Find all job listings on the page 
        
        job_listings = soup.find_all('div', class_='job-box__content')
        job_link = soup.find_all('div', class_='grid grid--middle job-box job-box--lg')
        

        

       # Extract relevant data from each job listing
        for job_listing in job_link:
            
            translator = Translator()
            title = job_listing.find('h3', class_='job-box__title')
           # job_title = translator.translate(title, dest=target_language)
            link = job_listing.find('a')
           
            location = job_listing.find('span', class_= 'job-box__job-location').text.strip("\n").replace('\n', ' ').replace('–', '').rstrip()

           
            current_year = datetime.now().year
            company =  job_listing.find('a')['data-company']
            start_date_element = job_listing.find('div', class_='job-box__content')
            start_date = start_date_element.find('span', class_='job-box__job-posted').text.strip().replace("Julkaistu ", "")
            #date = datetime.strptime(f"{start_date}{current_year}", "%d.%m.%Y")
            #date = start_date.strftime("%d-%m-%Y")
            date = convert_date_format(start_date)
            #date_test = date.strftime("%d-%m-%y")

           # print (job_listing)

           
            # Create a dictionary to store the job data

            data = {
                'company_name' : company,
                'job_location': location,
                'job_title' : title.text.strip(),
                'job_url' : 'https://duunitori.fi' + link['href'],
                
                'date': date,
            }

            job_data.append(data)


with open("jobs_duunitori.json", "w", encoding="utf-8") as outfile:

        json.dump(job_data, outfile, indent=4, ensure_ascii=False)

#return jsonify(job_data)

# if __name__ == '__main__':
#     app.run(debug=True)


