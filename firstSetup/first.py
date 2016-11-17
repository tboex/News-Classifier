import numpy as np
import pickle
import requests, webbrowser, bs4
import unicodedata
from stop_words import get_stop_words
from sklearn.naive_bayes import GaussianNB

APOSTROPHIES = {"'s" : "is", "'re" : "are", "'t" : "not", "'ll" :"will", "'ve" : "have", "'d" : "would"}
stop_words = get_stop_words('english')

def cleanData(arr) :
	arr = [APOSTROPHIES[word] if word in APOSTROPHIES else word for word in arr]
	for index in range(len(stop_words)) :
		arr = [x for x in arr if x != stop_words[index]]
	finArr = [x for x in arr if x != "Photo"]
	for index in range(len(finArr)):
		finArr[index] = unicodedata.normalize('NFKD', finArr[index]).encode('ascii', 'ignore')
		finArr[index] = finArr[index].strip()
		finArr[index] = finArr[index].replace("''", " ")
		finArr[index] = finArr[index].replace("-", " ")
		finArr[index] = finArr[index].replace(".", " ")
		finArr[index] = finArr[index].replace(":", " ")
		finArr[index] = finArr[index].replace("\u2019", " ")
        finArr[index] = finArr[index].lower()
	finArr = [item for item in finArr if not item.isdigit()]
	return(finArr)


def removeUnicode(arr):
	tempArr = arr
	for index in range(len(arr)) :
		tempArr[index] = str(tempArr[index])


def nytimes(link):
    print("Pulling down New York Times...")
    try :
        res = requests.get(link)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
    res.raise_for_status()

    soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
    title = soupedUp.select('#headline')

    print(u"\u25CF"+ " NY Times -  " + title[0].getText())

    document = soupedUp.select('.story-body-supplemental')
    words = (document[0].getText()).split()
    words = words[18:]
    return cleanData(words)

def foxnews(link):
    print("Pulling down Fox News...")
    try:
        res = requests.get(link)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
    res.raise_for_status()

    soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
    print(u"\u25CF"+ " Fox News - " + soupedUp.title.string)

    document = soupedUp.select('.article-text')
    words = (document[0].getText()).split()
    return cleanData(words)

def msnbc(link):
    print("Pulling down MSNBC...")
    try:
        res = requests.get(link)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
    res.raise_for_status()

    soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
    print(u"\u25CF"+ " MSNBC - " + soupedUp.title.string)

    document = soupedUp.select('.main-Copy')
    words = (document[0].getText()).split()
    return cleanData(words)

def guardian(link):
    print("Pulling down theGuardian...")
    try:
        res = requests.get(link)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print e
    res.raise_for_status()

    soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
    print(u"\u25CF"+ " theGuardian - " + soupedUp.title.string)

    document = soupedUp.select('.content__article-body')
    words = (document[0].getText()).split()
    return cleanData(words)

def townhall(link):
    print("Pulling down Townhall")
    try:
        res = requests.get(link)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
    res.raise_for_status()

    soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
    print(u"\u25CF"+ " Townhall - " + soupedUp.title.string)

    document = soupedUp.select('#article-body')
    words = (document[0].getText()).split()
    return cleanData(words)

def csm(link):
    print("Pulling down Christian Science Monitor")
    try:
        res = requests.get(link)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
    res.raise_for_status()

    soupedUp = bs4.BeautifulSoup(res.text, "html.parser")
    print(u"\u25CF"+ " Chistian Science Monitor - " + soupedUp.title.string)

    document = soupedUp.select('#story-body')
    words = (document[0].getText()).split()
    return cleanData(words)

nytArr = nytimes("http://www.nytimes.com/2016/11/08/world/asia/india-delhi-smog.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news")
foxArr = foxnews("http://www.foxnews.com/politics/2016/11/08/floridas-marco-rubio-wins-re-election-in-senate-race.html")
msnbcArr = msnbc ("http://www.msnbc.com/specials/migrant-crisis")
guardianArr = guardian("https://www.theguardian.com/us-news/2016/nov/08/us-congress-election-results-senate-house-democrats-republicans")
townhallArr = townhall("http://townhall.com/news/politics-elections/2016/11/08/defiant-into-final-day-trump-warns-of-election-fraud-n2243118")
csmArr = csm("http://www.csmonitor.com/USA/Politics/2016/1108/On-Election-Day-hope-energy-and-anxiety-but-also-calm")

combinedArr = nytArr + foxArr + msnbcArr + guardianArr + townhallArr + csmArr

idDict = {}
for s in range(len(combinedArr)) :
	if not combinedArr[s] in idDict :
		idDict.setdefault(combinedArr[s], len(idDict))

def arrStrToUniInt(arr) :
	tempArr = arr
	for index in range(len(arr)):
		tempArr[index] = idDict[arr[index]]
 	return tempArr

nytArr = arrStrToUniInt(nytArr)
foxArr = arrStrToUniInt(foxArr)
msnbcArr = arrStrToUniInt(msnbcArr)
guardianArr = arrStrToUniInt(guardianArr)
townhallArr = arrStrToUniInt(townhallArr)
csmArr = arrStrToUniInt(csmArr)

X = nytArr  + msnbcArr + guardianArr + townhallArr + csmArr + foxArr
X = np.array(X)
X = X.reshape((len(X), 1))

y = []
for index in range(len(nytArr)) :
	y.append(0)
for index in range(len(msnbcArr)) :
	y.append(0)
for index in range(len(guardianArr)) :
	y.append(0)
for index in range(len(townhallArr)) :
	y.append(1)
for index in range(len(csmArr)) :
	y.append(1)
for index in range(len(foxArr)) :
	y.append(1)
y = np.array(y)

clf = GaussianNB()
clf.fit(X,y)

s = pickle.dump(clf, open( "../save.p", "wb" ))
m = pickle.dump(idDict, open( "../dict.p", "wb"))
