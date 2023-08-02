# from flask import Flask, jsonify
# import requests
# from bs4 import BeautifulSoup
# import json
# from datetime import datetime

# app = Flask(__name__)


# def convert_date_format(date_string):
#     try:
#         # Parse the date string into a datetime object
        
        
#         # Check if the year is included in the date_string
#         current_year = datetime.now().year
#         if date_string.endswith("."):
#             # If year is not included in date_string, use the current year
#             date_obj = datetime.strptime(date_string, "%d.%m.")
#             date_obj = date_obj.replace(year=current_year)
#         else:
#             #if date_string.endswith("%Y"):
#             # date_obj = datetime.strptime(date_string, "%d.%m.%Y")
#             date_obj = datetime.strptime(date_string, "%d.%m.%Y")
#             date_obj = date_obj.replace(year=date_obj.year)

#         return date_obj.strftime("%d-%m-%y")
#     except ValueError:
#         # If the input date_string is None or not in the expected format
#         return None

# # def convert_date_format(date_string):
# #     try:

# #         # Check if the year is included in the date_string
# #         current_year = datetime.now().year
       
           
        
# #         date_obj = datetime.strptime(date_string, "%d.%m.%Y")
# #         #date_obj = date_obj.replace(year=date_obj.year)

# #         return date_obj.strftime("%d-%m-%y")
# #     except ValueError:
# #         # If the input date_string is None or not in the expected format
# #         return None

# # Load keywords from a JSON file
# with open('../keywords.json', 'r') as file:
#         keywords = json.load(file)
#         #print (keywords)

# # Create a list to store the extracted job data
# jobs = []
# locations="Espoo"
# # Perform web scraping for eacj keyword
# for keyword in keywords:
#         # Format the keyword to be used in the URL
#         formatted_keyword = keyword.replace(' ', '%20')
#         #print (formatted_keyword)

#         # Construct the URL for the indeed search page
        
#         #url = f'https://www.jobly.fi/en/jobs?search={formatted_keyword}'
       

       
#         url = f'https://www.jobly.fi/en/jobs?search={formatted_keyword}&job_geo_location={locations}'
        
#         #print(url)

#         # Send a GET request to the indeed search page with headers
        
#         response = requests.get(url)
#         response.encoding = 'utf-8'
        
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         next_page_list = soup.find('ul', class_='pager')
#         page = next_page_list.find_all('li')[1]
#         print(page)
#         next_page_link = page.find('a')["href"]
#         jobly_url = f'https://www.jobly.fi/{next_page_link}'
#         #jobly_url = next_page_link['href'] if next_page_link else None
#         print(next_page_link)

#         response_2 = requests.get(jobly_url)
#         response_2.encoding = 'utf-8'

#         soup_2 = BeautifulSoup(response_2.content, 'html.parser')

#         job_listings = soup.find_all('div', class_='node__content') + soup_2.find_all('div', class_='node__content')
        
# # Extract relevant data from each job listing
# for listing in job_listings:
            
#             job_title = listing.find("h2", class_="node__title")
            
#             title = job_title.find("a").text.strip()
    
#             link = job_title.find("a")["href"]

#             company = listing.find("span", class_="recruiter-company-profile-job-organization").text.strip()

#             job_loc = listing.find("div", class_="location")

#             location = job_loc.find("span").text.strip()

#             published = listing.find("div", class_="description")

#             date = published.find('span', class_="date").text.strip().replace(",", "")

#             job_date = convert_date_format(date)


#             #date = published.find("span").replace(",", "")
            
    
#    # Create a dictionary for the job data


#             job_data = {
#                 "company_name": company,

#                 "job_location": location,

#                 "job_title": title,

#                 "job_url": link,

#                 "date": job_date

#             }



#             # Add the job data to the list

#             jobs.append(job_data)



# with open("jobs_jobly.json", "w", encoding="utf-8") as outfile:
#         json.dump(jobs, outfile, indent=4, ensure_ascii=False)


# New Code

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

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

# def convert_date_format(date_string):
#     try:

#         # Check if the year is included in the date_string
#         current_year = datetime.now().year
       
           
        
#         date_obj = datetime.strptime(date_string, "%d.%m.%Y")
#         #date_obj = date_obj.replace(year=date_obj.year)

#         return date_obj.strftime("%d-%m-%y")
#     except ValueError:
#         # If the input date_string is None or not in the expected format
#         return None

# Load keywords from a JSON file
with open('../keywords.json', 'r') as file:
        keywords = json.load(file)
        #print (keywords)

# Create a list to store the extracted job data
jobs = []
all_jobs_data = []
locations="Helsinki"
total_pages =0
# Perform web scraping for eacj keyword
for keyword in keywords:
    #for page in range(1, total_pages + 1):

        # Format the keyword to be used in the URL
        formatted_keyword = keyword.replace(' ', '%20')
        #print (formatted_keyword)

        # Construct the URL for the indeed search page
        
        #url = f'https://www.jobly.fi/en/jobs?search={formatted_keyword}'
       

    
        url = f'https://www.jobly.fi/en/jobs?search={formatted_keyword}&job_geo_location={locations}'
        print(url)
        
        #print(url)

        # Send a GET request to the indeed search page with headers
        
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        soup = BeautifulSoup(response.content, 'html.parser')
        all_jobs_data.extend(soup)
        next_page_list = soup.find('ul', class_='pager')
        page = next_page_list.find_all('li')[1]
        test = next_page_list.find_all('li')
        #print(test)
        test1 = next_page_list.select('li a')
        #print(test1)
        # if [a.text != 'next' for a in test1]:
        if ([a.text for a in test1] != 'next'):
            all_href_values = [a['href'] for a in test1]
            #print(all_href_values)
        values = [a.text for a in test1]
        print(len(values))
        total_pages = len(values)
        next_page_link = page.find('a')["href"]
        #npl = test.find_all('a')
        next_page_links = []
        #jobly_url = ''
        # npl = []
        #j_url = ""
        scraped_urls = []

        for page in range(1, total_pages + 1):
            jobly_pages_url = f'https://www.jobly.fi/en/jobs?search={formatted_keyword}&job_geo_location={locations}&page={page}'
            print(jobly_pages_url)
        
            response_2 = requests.get(jobly_pages_url)
            response_2.encoding = 'utf-8'
            #print(response_2.content)
            soup_2 = BeautifulSoup(response_2.content, 'html.parser')
            #print(soup_2)
            #scraped_urls.extend(soup_2) 
            job_page_listings = soup_2.find_all('div', class_='node__content')

        job_listings = soup.find_all('div', class_='node__content') 
        #job_listings.append(job_page_listings)
        # for page_list in all_href_values:
            
        #         jobly_url = f'https://www.jobly.fi/{page_list}'
        #         print(jobly_url)
        #         response_2 = requests.get(jobly_url)
        #         response_2.encoding = 'utf-8'
        #         soup_2 = BeautifulSoup(response_2.content, 'html.parser')
                #scraped_urls.append(soup_2)  
                #job_listings = soup.find_all('div', class_='node__content') + soup_2.find_all('div', class_='node__content')

            # for j_url in jobly_url:
                
            #       response_2 = requests.get(jobly_url)
            #       response_2.encoding = 'utf-8'
            #       soup_2 = BeautifulSoup(response_2.content, 'html.parser')
            #       scraped_urls.append(soup_2)  
            #   j_url=jobly_url
            #   print(j_url)
            #   response_2 = requests.get(jobly_url)
            #   response_2.encoding = 'utf-8'
            #   soup_2 = BeautifulSoup(response_2.content, 'html.parser')
            #   #print(soup_2) 
            #   abc = soup_2
            #   #print(abc)
        #print(scraped_urls)
        #job_listings = soup.find_all('div', class_='node__content') + scraped_urls.find_all('div', class_='node__content')
        #print(job_listings)

        #     pages = page_list['href']
        #     #npl.append(pages) 
        #     #print(pages)
        #     # next_page_links = [a['href'] for a in pages]
        #     # print(next_page_links)
        #     #print(pages)
        #     npl = [item for sublist in pages for item in sublist]
        #     #print(npl)
        # for p_link in pages:

        #     page_link = p_link["href"]
        #     next_page_links.append(page_link)
        #     print(next_page_links)

            # if pages:
            # # Extract the 'href' attribute from the <a> element
            #     page_link = pages['href']
            #     next_page_links.append(page_link)
            #     print(next_page_links)
        # for page_links in next_page_links:
        #     jobly_url = f'https://www.jobly.fi/{page_links}'
        #     #print(jobly_url)
        #     response_2 = requests.get(jobly_url)
        #     response_2.encoding = 'utf-8'

        #     soup_2 = BeautifulSoup(response_2.content, 'html.parser')
        #job_listings = soup.find_all('div', class_='node__content') 
            #print(soup_2)
       
        #jobly_url = next_page_link['href'] if next_page_link else None
      

        

        
        
# Extract relevant data from each job listing
for listing in job_listings:
            
            job_title = listing.find("h2", class_="node__title")
            
            title = job_title.find("a").text.strip()
    
            link = job_title.find("a")["href"]

            company = listing.find("span", class_="recruiter-company-profile-job-organization").text.strip()

            job_loc = listing.find("div", class_="location")

            location = job_loc.find("span").text.strip()

            published = listing.find("div", class_="description")

            date = published.find('span', class_="date").text.strip().replace(",", "")

            job_date = convert_date_format(date)


            #date = published.find("span").replace(",", "")
            
    
   # Create a dictionary for the job data


            job_data = {
                "company_name": company,

                "job_location": location,

                "job_title": title,

                "job_url": link,

                "date": job_date

            }



            # Add the job data to the list

            jobs.append(job_data)



with open("jobs_jobly.json", "w", encoding="utf-8") as outfile:
        json.dump(jobs, outfile, indent=4, ensure_ascii=False)







