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

sort_dict = sorted(results, key=lambda i:i["Game Number"])
#sort_dict = sorted(results, key=lambda i: i["Ticket Cost"])

#print(sort_dict)

for x in range(len(sort_dict)):
    print(
    #"Game Number:",sort_dict[x]["Game Number"],
    #"Ticket Cost:", sort_dict[x]["Ticket Cost"],
    "Game Name:",sort_dict[x]["Game Name"],"| Top Prize:",sort_dict[x]["Top Prize"],
    "| Top Prizes Remaining:",sort_dict[x]["Top Prizes Remaining"],
    "| Ticket Cost:",sort_dict[x]["Ticket Cost"], 
    end="\n"
    )
