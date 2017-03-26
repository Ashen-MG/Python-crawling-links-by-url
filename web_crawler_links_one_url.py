import requests
from bs4 import BeautifulSoup
import os

try:

    url_input = input("Enter a url that you want to crawl: ").replace(" ", "")
    request = requests.get(str(url_input))

    if request.status_code == 200:

        print("Crawling " + url_input)

        url = request.text
        soup = BeautifulSoup(url, "lxml")

        file_path = input("Put full path (key sensitive) where you want to save links (file) Tip: Put / before: ")

        if os.path.exists(file_path) and os.path.isfile(file_path):
            f = open(file_path, "w")
            f.write("Links for " + url_input + "\n\n")

            for link in soup.findAll("a"):
                href = link.get("href")

                if href is not "#":
                    print(href)

                    f.write(href + "\n")

            f.close()

        else:
            print("Path doesn't exist or place where you want to save links is not file.")

except KeyboardInterrupt:
    print("")
except:
    print("That url doesn't exist or you typed it wrong. Tip: Make sure you're copying it from website and watch "
          "out for protocols (http, https)")
