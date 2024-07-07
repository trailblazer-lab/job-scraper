import requests
from bs4 import BeautifulSoup

def scrape_job_board(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')

        for job in job_listings:
            title = job.find('a', class_='jobtitle').text.strip()
            company = job.find('span', class_='company').text.strip()
            location = job.find('span', class_='location').text.strip()
            summary = job.find('div', class_='summary').text.strip()

            print(f"Title: {title}")
            print(f"Company: {company}")
            print(f"Location: {location}")
            print(f"Summary: {summary}")
            print("="*30)
    else:
        print(f"Failed to retrieve job listings from {url}")

if __name__ == "__main__":
    # List of URLs to scrape
    urls = [
    'https://www.indeed.com/q-python-developer-jobs.html',
    'https://www.linkedin.com/jobs/python-developer-jobs',
    'https://stackoverflow.com/jobs?q=python',
    'https://www.glassdoor.com/Job/python-developer-jobs-SRCH_KO0,15.htm',
    'https://www.careerbuilder.com/jobs-python-developer',
    'https://www.dice.com/jobs?q=python%20developer',
    'https://www.monster.com/jobs/search/?q=python-developer',
    ]
    
    # Scrape jobs from each URL
    for url in urls:
        scrape_job_board(url)