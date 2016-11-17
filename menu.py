import dataCleaning as dc
import collections
import numpy as np
import newsImport as ni


# TODO
#Add first menu into menu.py

def menu_Predict(clf, idDict):
    exit = ["0", "exit"]
    options1 = ["1","phrase","enter a phrase", "enter"]
    c = True
    while c == True:
        print("\nEnter a phrase to be predicted")
        print(u"\u25CF"+ "0: EXIT")
        print(u"\u25CF"+ "1: Enter a phrase")
        inp = raw_input("\nChoose an option - ")
        inp = inp.lower()
        if any(inp in s for s in exit):
            c = False
        elif any(inp in s for s in options1):
            inp = raw_input("Phrase\n -Enter full phrase: ")
            words = inp.split(' ')
            words = dc.norm_cleanData(words)
            print("\n " + u"\u25CF" + " Splitting Phrase")
            print(" " +u"\u25CF" + " Converting Phrase to Lowercase")
            print(" " +u"\u25CF" + " Cleaning Phrase \n    - Removing Stop Words \n    - Fixing Apostrophies \n    - Removing Meaningless Words")
            print(" " +u"\u25CF" + " Indexing Phrase\n")
            print("\n----------------------")
            print("     Classifing\n")
            phrase = ni.predictPhrase(inp, idDict)
            if phrase != [] :
                phrase = np.array(phrase)
                phrase = phrase.reshape(-1,1)
                predicted = clf.predict(phrase)
                data = collections.Counter(predicted)
                most_common = data.most_common(1)

                # Change this based on classififers
                # [0] - Liberal
                # [1] - Conservative
                print("\n----------------------")
                print("     Predicting\n")
                for index in range(len(predicted)) :
                    if predicted[index] == 0 :
                        print('{0:17} =+ {1:10}'.format(words[index], "Liberal"))
                    else :
                        print('{0:17} =+ {1:10}'.format(words[index], "Conservative"))
                if most_common[0][0] == 0 :
                    print('{0:17} ==> {1:15}'.format("Phrase is overall", "[ Liberal ]"))
                else :
                    print('{0:17} ==> {1:15}'.format("Phrase is overall", "[ Conservative ]"))
                print("\n----------------------\n")
            else :
                print("\n  ![No classifiable words found]!")
