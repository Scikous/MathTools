#return 0=success, 1-> onwards = fail
def regexAB(inputString: str):
    #string cannot be empty
    #last character cannot be 'a', for 'a' must be succeeded by 'b'
    if inputString and inputString[-1] == 'a':
        return 1
    
    allowedChars = ('a', 'b')
    #string may only contain 'a' and 'b' characters
    notOnlyAB = any(char for char in inputString if char not in allowedChars)
    if(notOnlyAB):
        return 2
    
    cntA = inputString.count('a')
    cntB = inputString.count('b')
    if cntA == 0 or cntB < 2: #there must be at least 1 'a' and at least 2 'b'
        return 3
    if cntA >= cntB: #There must always be more 'b' characters than 'a' characters
        return 4
    
    for ind in range(0, len(inputString)):
        if inputString[ind-1] == 'a' and inputString[ind] == 'a':
            return 5
    return 0


inputStrings = ["bbabbbab", "abb", "baab", "babababab", "bbbbbabbbabaa",
            "aaaaaa", "bbbbbbbbbb", "babbba", "ABABABABA", "abababABababa",
            "babababzbab", "qwertyuiopsdfghjklzxcvnm", "1234567890", "!@#$%^&*()-_=+[]}{|;:\,.<>?/", ""]

outcomes = []
for inputString in inputStrings:
    print(inputString)
    outcomes.append(regexAB(inputString))
print(f"{inputStrings}\n{outcomes}")
