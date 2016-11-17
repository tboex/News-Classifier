import collections
import numpy as np
import newsImport as ni
import dataCleaning as dc
import menu
from sklearn.naive_bayes import GaussianNB
import pickle

clf = pickle.load( open( "save.p", "rb" ) )
idDict = pickle.load( open( "dict.p", "rb" ) )
print("-----------------------------")
print("News Classifier  "+ u"\u00A9" + " Tim Boex")

nytArr = []
foxArr = []
msnbcArr = []
guardianArr = []
townhallArr = []
csmArr = []
foxArr = []
#-------------------------------------
exit = ["0", "exit"]
options1 = ["1","nyt","new york times", "new york"]
options2 = ["2", "fox", "fox news", "foxnews"]
options3 = ["3", "msnbc"]
options4 = ["4", "theguardian", "the guardian", "guardian"]
options5 = ["5", "townhall"]
options6 = ["6", "csm", "christian science monitor"]

y = []
c = True
while c == True :
	print("\nEnter more Sources (Help me Learn)")
	print(u"\u25CF"+ "0: EXIT")
	print(u"\u25CF"+ "1: New York Times")
	print(u"\u25CF"+ "2: Fox News")
	print(u"\u25CF"+ "3: MSNBC")
	print(u"\u25CF"+ "4: the Guardian")
	print(u"\u25CF"+ "5: Townhall")
	print(u"\u25CF"+ "6: Christian Science Monitor")
	inp = raw_input("\nChoose an option - ")
	inp = inp.lower()

	if any(inp in s for s in exit):
		c = False
	elif any(inp in s for s in options1):
		inp = raw_input("New York Times\n -Enter full URL: ")
		nytArr = nytArr + ni.nytimes(inp)
	elif any(inp in s for s in options2):
		inp = raw_input("Fox News\n -Enter full URL: ")
		foxArr = foxArr + ni.foxnews(inp)
	elif any(inp in s for s in options3):
		inp = raw_input("MSNBC\n -Enter full URL: ")
		msnbcArr = msnbcArr + ni.msnbc(inp)
	elif any(inp in s for s in options4):
		inp = raw_input("the Guardian\n -Enter full URL: ")
		guardianArr = guardianArr + ni.guardian(inp)
	elif any(inp in s for s in options5):
		inp = raw_input("Townhall\n -Enter full URL: ")
		townhallArr = townhallArr + ni.townhall(inp)
	elif any(inp in s for s in options6):
		inp = raw_input("Christian Science Monitor\n -Enter full URL: ")
		csmArr = csmArr + ni.csm(inp)
	else :
		print("\nSorry " + inp + " is not a valid input")
#end Loop
combinedArr = nytArr + foxArr + msnbcArr + guardianArr + townhallArr + csmArr

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
if len(X) > 0:
	clf.partial_fit(X,y)

menu.menu_Predict(clf, idDict)

s = pickle.dump(clf, open( "save.p", "wb" ))
