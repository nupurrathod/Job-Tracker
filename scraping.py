import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def fetch_job_data(page_number):
    url = f'https://www.shine.com/job-search/jobs-{page_number}?job_type=2&top_companies_boost=true&sort=1'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {url}")
    return response.content

def parse_job_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract job titles
    req = soup.select('div h2[itemprop="name"]')
    titles = [r.text.strip().replace("  ", "") for r in req]

    # Extract company names
    orgs = soup.find_all('div', class_='jobCard_jobCard_cName__mYnow')
    orgs1 = [o.text.split("Hiring")[0].strip() for o in orgs]

    # Extract locations
    loc = soup.find_all('div', class_='jobCard_jobCard_lists__fdnsc')
    location = [re.findall("Yrs?(.*)$", l.text)[0].replace("+4", ", ").strip() for l in loc]

    # Extract experience
    experience = [re.findall("^(.*) Yrs?", l.text)[0] for l in loc]

    # Extract vacancies
    vac = soup.find_all('ul', class_='jobCard_jobCard_jobDetail__jD82J')
    vac = [v.text for v in vac]
    vacancies = [int(re.findall(r'\d+', text)[0]) if re.findall(r'\d+', text) else 1 for text in vac]

    # Construct DataFrame
    data = {'Titles': titles, 'Firm Name': orgs1, 'Job Location': location, 'Experience': experience, 'Positions': vacancies}
    df = pd.DataFrame(data)

    return df
