import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

#First Find element
results = soup.find(id='ResultsContainer')
print(results.prettify())

print("Goodbye, World!")