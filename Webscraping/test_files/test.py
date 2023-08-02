import re
import json
import asyncio 
from typing import List

import httpx


def parse_job_page(html):
    """parse job data from job listing page"""
    data = re.findall(r"_initialData=(\{.+?\});", html)
    data = json.loads(data[0])
    return data["jobInfoWrapperModel"]["jobInfoModel"]


async def scrape_jobs(client: httpx.AsyncClient, job_keys: List[str]):
    """scrape job details from job page for given job keys"""
    urls = [f"https://www.indeed.com/m/basecamp/viewjob?viewtype=embedded&jk={job_key}" for job_key in job_keys]
    scraped = []
    for response in await asyncio.gather(*[client.get(url=url) for url in urls]):
        scraped.append(parse_job_page(response.text))
    return scraped