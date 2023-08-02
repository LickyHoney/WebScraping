from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
# import random
# import time

app = Flask(__name__)

@app.route('/scrape')
def scrape_jobly():
    # Load keywords from a JSON file
    with open('keywords.json', 'r') as file:
        keywords = json.load(file)
        print (keywords)

    # Create a list to store the extracted job data
    jobs = []

    # Perform web scraping for eacj keyword
    for keyword in keywords:
        # Format the keyword to be used in the URL
        formatted_keyword = keyword.replace(' ', '%20')
        print (formatted_keyword)

        # Construct the URL for the indeed search page
        #url =  f'https://www.indeed.com/jobs?q={formatted_keyword}' 
        url = f'https://www.glassdoor.com/Search/results.htm?keyword={formatted_keyword}'
        print(url)

        # Add headers to mimic a web browser
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        # }

        # Send a GET request to the indeed search page with headers
        #response = requests.get(url, headers=headers)
        response = requests.get(url)
        
        #print (response.content)

        # Random delay to avoid triggering rate limiting
        #time.sleep(random.uniform(1,3))

        # response = requests.get(url)
        #print(response.content)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)

        
        
        job_listings = soup.find_all("a")
        print(job_listings)
        

        
       # Extract relevant data from each job listing
#         for listing in job_listings:
            
#             job_title = listing.find("h2", class_="node__title")
#             print (job_title)
#             title = job_title.find("a").text.strip()
    
#             link = job_title.find("a")["href"]

#             job_loc = listing.find("div", class_="location")

#             company = listing.find("span", class_="recruiter-company-profile-job-organization").text.strip()

#             location = job_loc.find("span").text.strip()

    
#    # Create a dictionary for the job data

#             job_data = {

#                 "title": title,

#                 "link": link,

#                 "company": company,

#                 "location": location

#             }

#             # Add the job data to the list

#             jobs.append(job_data)

    #Save the data in a JSON file
    with open('jobs_jobly.json', 'w') as file:
        json.dump(jobs, file, indent=4)

    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)


