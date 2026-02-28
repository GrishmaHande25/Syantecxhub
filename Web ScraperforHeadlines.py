import requests
from bs4 import BeautifulSoup
import json
import csv
import time

URL = "https://www.bbc.com/news"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
DELAY = 2
KEYWORD = ""

def fetch_headlines(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = []

        for item in soup.find_all("h2"):
            title = item.get_text(strip=True)

            if not title:
                continue

            if KEYWORD and KEYWORD.lower() not in title.lower():
                continue

            headlines.append({
                "title": title,
                "url": url,
                "time": "N/A"
            })

        return headlines

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

def save_json(data, filename="headlines.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Saved to", filename)

def save_csv(data, filename="headlines.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url", "time"])
        writer.writeheader()
        writer.writerows(data)
    print("Saved to", filename)

def main():
    print("Fetching headlines...")
    headlines = fetch_headlines(URL)

    if headlines:
        for i, h in enumerate(headlines, 1):
            print(f"{i}. {h['title']}")

        save_json(headlines)
        save_csv(headlines)
    else:
        print("No headlines found.")

    time.sleep(DELAY)

if __name__ == "__main__":
    main()