import sys
import operator

def removeall(mylist,obj):
    while obj in mylist:
        mylist.remove(obj)

try:
    storyFile = str(sys.argv[1])
    print("Story file name: ",storyFile)
    skipWordsFile = str(sys.argv[2])
    print("Skip word file name: ",storyFile)
except:
    print("Program Usage : python3 assignment9 <storyFile> <wordToSkipFile>")
    sys.exit(1)  # abort


wordList = []
skipwordList = []
pairCount = dict()

with open(sys.argv[1], 'r') as storyFile:
    data = storyFile.read()
    data = data.lower()
    erasures = ['\n','\t','.','?','!',',',';',':','\'','\"']
    for char in erasures:
            data = data.replace(char, ' ')    
    
    for word in data.split():
        wordList.append(word)
        
    with open(sys.argv[2], 'r') as skipWordsFile:
        data = skipWordsFile.read()
        for skipWord in data.split(','):
            skipwordList.append(skipWord)
            # skipWord = skipWord.lower()
            removeall(wordList,skipWord)

    print("Skip words: ",skipwordList)

for i, word in enumerate(wordList):
    if(i+2 != len(wordList)):
        keyString = word + " " +wordList[i+1]
        if keyString in pairCount:
            pairCount[keyString] = pairCount.get(keyString) + 1
        else:
            pairCount[keyString] = 1
    else:
        break


newDict = sorted(pairCount.items(), key=operator.itemgetter(1))
print("The five most frequently occurring word pairs are:")
for x in list(reversed(list(newDict)))[0:5]:
    print (x)
