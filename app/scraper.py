import requests
from bs4 import BeautifulSoup
import urllib3

# remove SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_headlines():
    url = "https://news.ycombinator.com/"
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        verify=False
    )

    soup = BeautifulSoup(response.text, "html.parser")

    # ✅ Correct selector (UPDATED)
    headlines = [a.text for a in soup.select(".titleline > a")]

    return headlines[:5]

if __name__ == "__main__":
    data = scrape_headlines()

    if not data:
        print("No headlines found ❌")
    else:
        for i, title in enumerate(data, 1):
            print(f"{i}. {title}")

