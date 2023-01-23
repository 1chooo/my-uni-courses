# -*-coding: utf-8 -*-

import requests
import bs4

url = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467050&stname=%25E6%2596%25B0%25E5%25B1%258B&datepicker=2022-09-20&altitude=20.6m"

r = requests.get(url)
r.encoding = "utf-8"
soup = bs4.BeautifulSoup(r.text, "html.parser")

print(soup.prettify())