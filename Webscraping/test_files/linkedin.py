import requests

from bs4 import BeautifulSoup

import json

#def scrape_news():

#url = "https://www.linkedin.com/jobs/search?keywords=Software%20Quality%20Assurance%20Tester&location=Finland&geoId=100456013&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
url = f'https://www.linkedin.com/jobs/search?keywords='
response = requests.get(url)

#soup = BeautifulSoup(response.text, 'lxml')

soup = BeautifulSoup(response.content, "html.parser")

res=soup.title

print(res.prettify())

#print(soup)

# Create a list to store the job data

jobs = []

#to extract job titles

job_listings = soup.find_all ('div', class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")




#print(job_listings)

#job_titles = [title.get_text() for title in job_titles]

for listing in job_listings:

#     # Extract the title, link, company, and location

    title = listing.find("h3", class_="base-search-card__title").text.strip()
    #print(title)

#     print(title)

    link = listing.find("a")["href"]

    #print(link)

    company = listing.find("h4", class_="base-search-card__subtitle").text.strip()

    #print(company)

    location = listing.find("span", class_="job-search-card__location").text.strip()

    #print(location)

   

    # Create a dictionary for the job data

    job_data = {

        "title": title,

        "link": link,

        "company": company,

        "location": location

    }

     # Add the job data to the list

    jobs.append(job_data)




# # Save the job data as JSON

with open("job_data.json", "w") as outfile:

    json.dump(jobs, outfile, indent=4)