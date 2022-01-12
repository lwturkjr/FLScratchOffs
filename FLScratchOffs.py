import requests as re
from bs4 import BeautifulSoup as bs


URL = "https://www.flalottery.com/"
rem_prizes = "remainingPrizes"

page = re.get(URL+rem_prizes)

soup = bs(page.content, "html.parser")