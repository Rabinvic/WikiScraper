import time

import bs4.element
import requests
import re
from bs4 import BeautifulSoup
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def getExamples(outfile, lang):
    #r = requests.get("https://en.wikipedia.org/wiki/La_Surprise_de_l%27amour")
    r = requests.get("https://"+lang+".wikipedia.org/wiki/Special:Random")

    #r = requests.get("https://en.wikipedia.org/wiki/Leeds_Zoological_and_Botanical_Gardens")
    # print(r)
    #print(r.url)

    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())

    s = soup.find('div', class_="mw-content-ltr mw-parser-output")
    #print(s.prettify())
    printables = []
    content = s.find_all('p')
    # print("\n\n\n\n\n\n")

    tagFreeString = ""
    #print(content)
    for item in content:
        if not str(item).isascii():
            continue

        p = item
        p = str(p)
        # p = p.replace("</p>", "")
        # p = p.replace("<p>", "")
        #p = p.replace("</a>", "")
        p = p.replace("<i>", "")
        p = p.replace("</i>", "")
        p = p.replace("<b>", "")
        p = p.replace("</b>", "")
        p = p.replace("<small>", "")
        p = p.replace("</small>", "")
        p = p.replace("<br>", "")
        p = p.replace("</br>", "")

        p = BeautifulSoup(p, "html.parser").find('p')
        #print(p.children)
        #print(p.get("class").__class__)
        if isinstance(p.get("class"), list):
            continue
        for thing in p.children:
            #print(thing)
            if str(thing).endswith("</a>"):
                printables.append(thing.next)
                continue
            if isinstance(thing, bs4.element.NavigableString):
                if(str(thing)=='\n'):
                    continue
                thingString = str(thing).replace("\n"," ")
                thingString = thingString.replace(".",". ")
                printables.append(thingString)
            try:
                tagFreeString = ''.join(printables)
                if len(tagFreeString.split()) >= 15:
                    break
            except:
                print(r.url)
        #print(printables)



        # print(p)

        # p = re.sub('<a href="[^"]*" title="[^"]*">', "", p)
        # p = re.sub('<a class="[^"]*" href="[^"]*" title="[^"]*">', "", p)
        # p = re.sub('<a class="[^"]*" href="(?:[^\\"]|\\\\|\\")*">',"",p)
        # p = re.sub('<.>', "", p)
        # p = re.sub('</.>', "", p)
        # p = re.sub('<sup class="reference" id="[^"]*">\[</span>1<span class="cite-bracket">\]</span></sup>', "", p)
        # p = re.sub(
        #     '<sup class="reference" id="[^"]*"><a href="[^"]*"><span class="cite-bracket">\[</span>[A-Za-z0-9]+<span class="cite-bracket">\]</span></sup>',
        #     "", p)
        # p = re.sub('<p class="[^"]*">',"",p)
        # p = re.sub('<span class="[^"]*" style="[^"]*"><span style="[^"]*">[A-Za-z][A-Za-z]</span> <span style="font-size: \d\d%;">[A-Za-z][A-Za-z][A-Za-z][A-Za-z]</span></span>',"",p)
        # p= re.sub('\([A-Za-z]+: <i lang="[A-Za-z][A-Za-z]">([A-Za-z0-9]+( [A-Za-z0-9]+)+), or  en\|<span title="[^"]*"><i lang="[A-Za-z][A-Za-z]">([A-Za-z0-9]+( [A-Za-z0-9]+)+)</span>\)',"",p)

        if len(tagFreeString.split()) >= 15:
            break
    if len(tagFreeString.split()) < 15:
        return False
    #print(p)
    #print(len(p.split()))
    # ultimateString = ''.join(words)
    words = tagFreeString.split()
    #print(ultimateString)

    #example = ""
    #for j in range(2):
    example = lang+"|"
    for i in range(15):
        example += words[i] + " "
    outfile.write(example + "\n")
    return True
    # start = p.index("<a")
    # print(start)

if __name__ == '__main__':
    outfile = open("train.dat", "w")
    j = 0
    totalRequests = 0
    timerStart = time.time()
    while j < 1000:
        if getExamples(outfile,"en"):
            totalRequests += 1
            j+=1
        else:
            continue
        foundSecond = False
        while not foundSecond:
            foundSecond = getExamples(outfile,"nl")
            totalRequests += 1
        j+=1
    timerEnd = time.time()
    print("Time:" +str(timerEnd-timerStart))
    print(totalRequests)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
