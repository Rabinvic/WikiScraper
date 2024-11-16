import requests
import re
from bs4 import BeautifulSoup
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def getExamples(outfile):
    r = requests.get("https://en.wikipedia.org/wiki/Special:Random")

    #r = requests.get("https://en.wikipedia.org/wiki/Byaban_Rural_District")
    # print(r)
    # print(r.url)

    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())

    s = soup.find('div', class_="mw-content-ltr mw-parser-output")
    #print(s.prettify())
    content = s.find_all('p')
    #print(content)
    # print("\n\n\n\n\n\n")

    p = ''
    for item in content:
        if not str(item).isascii():
            continue
        p = item
        p = str(p)
        p = p.replace("</p>", "")
        p = p.replace("<p>", "")
        p = p.replace("</a>", "")
        p = p.replace("<i>", "")
        p = p.replace("</i>", "")
        p = p.replace("<small>", "")
        p = p.replace("</small>", "")
        p = p.replace("<br>", "")
        p = p.replace("</br>", "")

        # print(p)

        p = re.sub('<a href="[^"]*" title="[^"]*">', "", p)
        p = re.sub('<a class="[^"]*" href="[^"]*" title="[^"]*">', "", p)
        p = re.sub('<a class="[^"]*" href="(?:[^\\"]|\\\\|\\")*">',"",p)
        p = re.sub('<.>', "", p)
        p = re.sub('</.>', "", p)
        p = re.sub('<sup class="reference" id="[^"]*">\[</span>1<span class="cite-bracket">\]</span></sup>', "", p)
        p = re.sub(
            '<sup class="reference" id="[^"]*"><a href="[^"]*"><span class="cite-bracket">\[</span>[A-Za-z0-9]+<span class="cite-bracket">\]</span></sup>',
            "", p)
        p = re.sub('<p class="[^"]*">',"",p)
        p = re.sub('<span class="[^"]*" style="[^"]*"><span style="[^"]*">[A-Za-z][A-Za-z]</span> <span style="font-size: \d\d%;">[A-Za-z][A-Za-z][A-Za-z][A-Za-z]</span></span>',"",p)
        p= re.sub('\([A-Za-z]+: <i lang="[A-Za-z][A-Za-z]">([A-Za-z0-9]+( [A-Za-z0-9]+)+), or  en\|<span title="[^"]*"><i lang="[A-Za-z][A-Za-z]">([A-Za-z0-9]+( [A-Za-z0-9]+)+)</span>\)',"",p)

        if len(p.split()) >= 30:
            break
    if len(p.split()) < 30:
        return False
    #print(p)
    #print(len(p.split()))
    # ultimateString = ''.join(words)
    ultimateString = p.split()
    #print(ultimateString)

    example = ""
    for j in range(2):
        example = "en|"
        for i in range(15):
            example += ultimateString[15 * j + i] + " "
        outfile.write(example + "\n")
    return j
    # start = p.index("<a")
    # print(start)

if __name__ == '__main__':
    outfile = open("train.dat", "w")
    j = 0
    while j < 250:
        if(getExamples(outfile)):
            j+=1


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
