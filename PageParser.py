import sys
import os
import requests
from BeautifulSoup import BeautifulSoup


class PageParser:

    def __init__(self, domain):
        self.domain = domain

    def page_request(self, parameter):

        # request for agent to the server
        url = self.domain + parameter
        request = requests.get(url)

        if request.status_code != 200:
            sys.exit(request.content)

        html = BeautifulSoup(requests.content)

        print html.find('table', attrs={"class": "table"})


def main():
    obj = PageParser("https://publicwww.com/websites/")
    obj.page_request("\"counter12.com%2Fad.js\"/5")


if __name__ == "__main__":
    main()

