def checker(word, essay): 
      
    a = essay.split(" ")
    count = 0
    for i in range(0, len(a)): 
          
        if (word == a[i]): 
           count = count + 1
             
    return count

    
def removePunctuation(string): 
  
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "") 
    return string

def markEssay(essay):
    a = essay.split(" ");
    
    for i in range(0,len(a)):
        if a[i] in wordBankPunct:
            a[i] = a[i].upper()
    
    essay = " ".join(a)
    print(essay)

def markEssay2(essay):
    a = essay.split(" ");
    
    for i in range(0,len(a)):
        if a[i] in wordBankPunct:
            a[i] = a[i].upper()
    
    print(essay)

def constructEssay(orig,marked):
    print(" ")
    

#"--------------------------------------------"
wordBank = ["am", "is", "are","was", "were", "have", "has", "had", "be", "being", "been", "do", "does", "did", "can", "could", "shall", "should", "will", "would",
"remain", "appear", "seem", "may", "might", "must", "became", "become", "continue", "elect", "grow", "stand", "turn", "prove",
"get", "sound", "look", "smell", "taste", "feel"]

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
wordBankPunct = []
for i in range(0, len(punctuations)):
    wordBankPunct = wordBankPunct + [word + punctuations[i] for word in wordBank]
wordBankPunct += wordBank
    
""" This portion takes the Word Bank of linking verbs and adds all possible punctuation to the end of it.
the new Word Bank with the punctuation attached is called wordBankPunct
---------------------------------------------"""


linkVerbCount = 0

essay = input("Paste your essay here: ")
essay  = essay.lower()
#essay = (removePunctuation(essay))

option = input("Would you like a detailed (D) or basic summary (B)? Type D or B: ")
print("")
if (option.lower() == "d"):
    for i in range(0,len(wordBankPunct)):
        ans = checker(wordBankPunct[i],essay)
        if(ans > 0):
            if (ans ==1):
                print("The word \"" + str(wordBankPunct[i]) + "\" occurs " + str(ans) + " time.")
            else:
                print("The word \"" + str(wordBankPunct[i]) + "\" occurs " + str(ans) + " times.")
    
        linkVerbCount += ans
    print(" ")
    
    print(markEssay2(essay))
    
    print ("You have " + str(linkVerbCount) + " linking verbs in your essay.")
elif (option.lower() == "b"):
    for i in range(0, len(wordBank)):
        ans = checker(wordBank[i],essay)
        linkVerbCount += ans
        
    print ("You have " + str(linkVerbCount) + " linking verbs in your essay.")
else:
    print("Try again")