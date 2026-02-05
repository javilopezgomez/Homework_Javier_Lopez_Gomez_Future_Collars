import requests
from datetime import datetime, timedelta
import os

LAT = 51.5072
LNG = -0.1261
log_file = "log.txt"


date = input("Enter a date (YYYY-mm-dd) or press enter for tomorrow's forecast: ")

if date == "":
    searched_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
else:
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        searched_date = parsed_date.strftime("%Y-%m-%d")
    except ValueError:
        print("The date format is invalid. It needs to be YYYY-mm-dd")
        exit()

log = {}

if os.path.exists(log_file):
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d, v = line.split(",", 1)
            log[d] = v

precipitation = None

if searched_date in log:
    raw = log[searched_date]
    precipitation = None if raw == "None" else float(raw)
    print("The result was already saved in the file")

else:
    api = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LNG}"
        "&daily=precipitation_sum"
        "&timezone=Europe%2FLondon"
        f"&start_date={searched_date}&end_date={searched_date}"
    )

    try:
        response = requests.get(api, timeout=10)
        response.raise_for_status()
        data = response.json()
        precipitation = data["daily"]["precipitation_sum"][0]

    except requests.exceptions.RequestException as e:
        print("Error connecting to the API:", e)
        precipitation = None
    except (KeyError, IndexError):
        precipitation = None

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{searched_date},{precipitation}\n")

if precipitation is None or precipitation < 0.0:
    print("I don't know")
elif precipitation == 0.0:
    print("It will not rain")
else:
    print(f"It will rain (precipitation_sum = {precipitation})")