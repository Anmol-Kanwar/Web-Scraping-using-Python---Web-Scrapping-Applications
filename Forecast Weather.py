

import requests

from bs4 import BeautifulSoup


import pandas as pd

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

print(page.text)


soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")

tonight = forecast_items[0]
print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
print(period)

short_desc = tonight.find(class_="short-desc").get_text()
print(short_desc)

temp = tonight.find(class_="temp").get_text()
print(temp)


img = tonight.find("img")
desc = img['title']

print(desc)


period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print("\n \n",periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
print(short_descs)

temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
print(temps)

descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(descs)


weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})

print("\n \n")
print("Wheather Deatils of particular week \n",weather)

writer = pd.ExcelWriter('Weather1.xls')
weather.to_excel(writer,'Sheet1')
writer.save()
