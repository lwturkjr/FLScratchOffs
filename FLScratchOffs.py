import requests as re
from bs4 import BeautifulSoup as bs


URL = "https://www.flalottery.com/"
rem_prizes = "remainingPrizes"
ticket_id = "scratch-offsGameDetails?gameNumber="

page = re.get(URL+rem_prizes)

soup = bs(page.content, "html.parser")

game_num = soup.find_all("td", class_="column1")

for game_num in game_num:
    print(game_num, end="\n")