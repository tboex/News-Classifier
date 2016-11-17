import unicodedata
from stop_words import get_stop_words

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

def norm_cleanData(arr) :
	arr = [APOSTROPHIES[word] if word in APOSTROPHIES else word for word in arr]
	for index in range(len(stop_words)) :
		arr = [x for x in arr if x != stop_words[index]]
	finArr = [x for x in arr if x != "Photo"]
	for index in range(len(finArr)):
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
