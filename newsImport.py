import requests, webbrowser, bs4
import dataCleaning as dc

def predictPhrase(str, idDict):
    #Change Classifiers based on goal
    #[0] - Liberal
    #[1] - Conservative
    words = str.split(' ')
    for index in range(len(words)) :
        words[index] = words[index].lower()
    words = dc.norm_cleanData(words)
    idArr = []
    for index in range(len(words)) :
        try:
            idArr.append(idDict[words[index]])
        except Exception, e:
            print("Unclassified Word:")
            print(e)
    return idArr

def nytimes(link):
    print("\nPulling down New York Times...\n")
    try :
        if "nytimes" in link :
            print("[-"),
            res = requests.get(link)
            print('-'),
            res.raise_for_status()
            print('-'),
            soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
            print('-'),
            title = soupedUp.select('#headline')
            print("-]"),
            print("Done\n\n Title:")
            print("  " + u"\u25CF"+ " NY Times -  " + title[0].getText())

            document = soupedUp.select('.story-body-supplemental')
            words = (document[0].getText()).split()
            words = words[18:]
            return dc.cleanData(words)
        else :
            print("Link isn't a New York Times article")
            return []
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("\n")
        print(e)
        return []

def foxnews(link):
    print("Pulling down Fox News...\n")
    try:
        if "foxnews" in link :
            print("[-"),
            res = requests.get(link)
            print('-'),
            res.raise_for_status()
            print('-'),
            soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
            print('-'),
            print("-]"),
            print("Done\n\n Title:")
            print(u"\u25CF"+ " Fox News - " + soupedUp.title.string)

            document = soupedUp.select('.article-text')
            words = (document[0].getText()).split()
            return dc.cleanData(words)
        else :
            print("Link isn't a Fox News article")
            return []
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        return []


def msnbc(link):
    print("Pulling down MSNBC...\n")
    try:
        if "msnbc" in link :
            print("[-"),
            res = requests.get(link)
            print('-'),
            res.raise_for_status()
            print('-'),
            soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
            print('-'),
            print("-]"),
            print("Done\n\n Title:")
            print(u"\u25CF"+ " MSNBC - " + soupedUp.title.string)

            document = soupedUp.select('.main-Copy')
            words = (document[0].getText()).split()
            return dc.cleanData(words)
        else :
            print("Link isn't a MSNBC article")
            return []
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        return []


def guardian(link):
    print("Pulling down theGuardian...\n")
    try:
        if "theguardian" in link :
            print("[-"),
            res = requests.get(link)
            print('-'),
            res.raise_for_status()
            print('-'),
            soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
            print('-'),
            print("-]"),
            print("Done\n\n Title:")
            print(u"\u25CF"+ " theGuardian - " + soupedUp.title.string)

            document = soupedUp.select('.content__article-body')
            words = (document[0].getText()).split()
            return dc.cleanData(words)
        else :
            print("Link isn't a Guardian article")
            return []
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        return []


def townhall(link):
    print("Pulling down Townhall...\n")
    try:
        if "townhall" in link :
            print("[-"),
            res = requests.get(link)
            print('-'),
            res.raise_for_status()
            print('-'),
            soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
            print('-'),
            print("-]"),
            print("Done\n\n Title:")
            print(u"\u25CF"+ " Townhall - " + soupedUp.title.string)

            document = soupedUp.select('#article-body')
            words = (document[0].getText()).split()
            return dc.cleanData(words)
        else :
            print("Link isn't a Townhall article")
            return []
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        return []

def csm(link):
    print("Pulling down Christian Science Monitor...\n")
    try:
        if "csmonitor" in link:
            print("[-"),
            res = requests.get(link)
            print('-'),
            res.raise_for_status()
            print('-'),
            soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
            print('-'),
            print("-]"),
            print("Done\n\n Title:")
            print(u"\u25CF"+ " Chistian Science Monitor - " + soupedUp.title.string)

            document = soupedUp.select('#story-body')
            words = (document[0].getText()).split()
            return dc.cleanData(words)
        else :
            print("Link isn't a Christian Science Monitor article")
            return []
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        return []
