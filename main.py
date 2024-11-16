import requests
from bs4 import BeautifulSoup
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    r = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    print(r)

    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
