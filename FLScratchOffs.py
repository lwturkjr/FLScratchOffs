import requests as re
from bs4 import BeautifulSoup as bs


URL = "https://www.flalottery.com/"
rem_prizes = "remainingPrizes"
ticket_url = "scratch-offsGameDetails?gameNumber="

page = re.get(URL+rem_prizes)

soup = bs(page.content, "html.parser")


table = soup.find("table")

headers = [header.text for header in table.find_all('th')]
results = [{headers[i]: cell.text.strip() for i, cell in enumerate(row.find_all('td'))}for row in table.find_all('tr')]

del results[0]

for x in range(len(results)):
    print("Game Name:",results[x]["Game Name"],"| Top Prize:",results[x]["Top Prize"],
    "| Top Prizes Remaining:",results[x]["Top Prizes Remaining"],
    "| Ticket Cost:",results[x]["Ticket Cost"], end="\n")
