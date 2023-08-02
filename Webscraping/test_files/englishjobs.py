from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
# import random
# import time

app = Flask(__name__)

@app.route('/scrape')
def scrape_engjobs():
    # Load keywords from a JSON file
    with open('keywords.json', 'r') as file:
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
        url = f'https://englishjobs.fi/jobs/{formatted_keyword}'
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
            #com_div = listing.find('div', class_='col-sm-5')
            com = listing.find("ul", class_="fa-ul")
            com_li = com.find_all('li')[0]
            loc_li = com.find_all('li')[1]
            #print(com_li)
            # com_list = com_li[1]
            # print(com_list)
            company = com_li.find('i').next_sibling.strip()
            print(company)
            location = loc_li.find('i').next_sibling.strip()
            # company = com_text.text
            
            #company = com_li[0].find('i', class_='fa-li fa fa-bank').text
           # print (company)
            #print(com_li)
            # for i in com_li:

            #     print(i.text)
            #     company = i.text
                
                #location = i.find("i", class_="fa-li fa fa-map-marker").text
            #company = listing.find("div", class_="col-sm-5").get_text().strip().replace('\n', ' ')
           # description =listing.find("div", class_="content").get_text().strip()
           # location = listing.find("div", class_="location mt-xxsm").get_text().strip()

            #print (listing)

           
            # Create a dictionary to store the job data
            job_data = {
                "title": title,
                "link": link,
                "company": company,
                #"description": description
                "location": location
            }

            jobs.append(job_data)

    #Save the data in a JSON file
    with open("job_englishjobs.json", "w") as outfile:
        json.dump(jobs, outfile, indent=4)

    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)


