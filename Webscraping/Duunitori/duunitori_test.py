from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
import re
import html


app = Flask(__name__)

@app.route('/scrape')
def scrape_duunitori():
    # Load keywords from a JSON file
    with open('../keywords.json', 'r') as file:
        keywords = json.load(file)

    # Create a list to store the extracted job data
    job_data = []

    # Perform web scraping for eacj keyword
    for keyword in keywords:
        # Format the keyword to be used in the URL
        formatted_keyword = keyword.replace(' ', '+')
        print (keyword)

        # Construct the URL for the indeed search page
        #url =  f'https://www.indeed.com/jobs?q={formatted_keyword}' 
        url = f'https://duunitori.fi/tyopaikat?haku={formatted_keyword}'

        # Add headers to mimic a web browser
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        # }

        # Send a GET request to the indeed search page with headers
        #response = requests.get(url, headers=headers)
        response = requests.get(url)
        response.encoding= 'utf-8'

        # Random delay to avoid triggering rate limiting
        #time.sleep(random.uniform(1,3))

        # response = requests.get(url)
        #print(response.content)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)

        # Find all job listings on the page 
        #job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')
        #job_listings = soup.find_all('div', class_='job-list__item')
        #job_listings = soup.find_all('li', class_='job-card')
        job_listings = soup.find_all('div', class_='job-box__content')
        job_link = soup.find_all('div', class_='grid grid--middle job-box job-box--lg')
        

        #print(job_listings)
        #print(job_link)
        
        # jobs = []
        # for div in soup.find_all(name='div', attrs={'class':'row'}):
        #     for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
        #         jobs.append(a['title'])
        # print(jobs)

       # Extract relevant data from each job listing
        for job_listing in job_link:
            #title_element = job_listing.find('h3',class_='job-text__title')
            #title_element = job_listing.find('h3',class_='job-box__title')
            
            title = job_listing.find('h3', class_='job-box__title')
            link = job_listing.find('a')
            #location = job_listing.find('span', class_= 'job-box__job-location').text.encode('utf-8', 'replace').decode('utf-8').strip()
            location = job_listing.find('span', class_= 'job-box__job-location').text.strip("\n").replace('\n', ' ').replace('–', '').rstrip()

            #loc= location.encode('latin-1', 'replace').decode('latin-1').replace('\n', ' ')
            #text_with_special_chars = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), text_with_special_chars)

            # loc1= re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), loc)
            # loc2= html.unescape(loc1).replace('\u00e4', 'ä').replace('\u00f6', 'ö')
            #company = job_listing.find('span')
            
            company =  job_listing.find('a')['data-company']
            start_date_element = job_listing.find('div', class_='job-box__content')
            start_date = start_date_element.find('span', class_='job-box__job-posted').text.strip()
            #end_date = start_date_element.find('span', class_='job-date__end').text.strip()

            print (job_listing)

           
            # Create a dictionary to store the job data

            data = {
                'title' : title.text.strip(),
                'link' : 'https://duunitori.fi' + link['href'],
                'Company' : company,
                'location': location,
                'start_date': start_date,
                #'end_date': end_date
            }

            job_data.append(data)

    #Save the data in a JSON file
    # with open('jobs_duunitori.json', 'w') as file:
    #     json.dump(job_data, file, indent=4)
   

    with open("jobs_duunitori.json", "w", encoding="utf-8") as outfile:

        json.dump(job_data, outfile, indent=4, ensure_ascii=False)

    return jsonify(job_data)

if __name__ == '__main__':
    app.run(debug=True)