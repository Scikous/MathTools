####deprecated
#return 0=success, 1-> onwards = fail
# def regexAB(inputString: str):
#     #string cannot be empty
#     #last character cannot be 'a', for 'a' must be succeeded by 'b'
#     if inputString and inputString[-1] == 'a':
#         return 1
    
#     allowedChars = ('a', 'b')
#     #string may only contain 'a' and 'b' characters
#     notOnlyAB = any(char for char in inputString if char not in allowedChars)
#     if(notOnlyAB):
#         return 2
    
#     cntA = inputString.count('a')
#     cntB = inputString.count('b')
#     if cntA == 0 or cntB < 2: #there must be at least 1 'a' and at least 2 'b'
#         return 3
#     if cntA >= cntB: #There must always be more 'b' characters than 'a' characters
#         return 4
    
#     for ind in range(0, len(inputString)):
#         if inputString[ind-1] == 'a' and inputString[ind] == 'a':
#             return 5
#     return 0

#{a,b},
# q0, a-> q0, b -> q1,  #q0error
#q1, a -> q2, b -> q1   #move on if b
#q2, b-> q3, a->q0 # index not final, q1
#any char -> q0
####
def regexAB(inputString: str):
    def recursiveCheck(state=1, index=0): #states 1-4, let x : x is a member of any alphabet, and x is not 'b' or 'a'
        print(state, index, len(inputString))
        if len(inputString) > index:
            match state: #case 0 is not used as it could cause confusion
                case 1:#q1, a/x -> -q1, b -> q2
                    if inputString[index] == 'b':
                        state = 2
                    else:
                        state = -1
                    index += 1
                    return recursiveCheck(state, index)
                    
                case 2:#q2, a -> q3, b -> q2, x -> -q1
                    if inputString[index] == 'a':
                        state = 3
                    elif inputString[index] == 'b':
                        state = state
                    else:
                        state = -1
                    index += 1
                    return recursiveCheck(state, index)

                case 3:#q3, a/x -> -q1, b -> q4 
                    if inputString[index] == 'b':
                        state = 4
                    else:
                        state = -1
                    index +=1
                    return recursiveCheck(state, index)
                case 4:#q4, a -> q3, b -> 4, x -> -q1,  case 4 = accepted state
                    if inputString[index] == 'b':
                        state = 4
                    elif inputString[index] == 'a':
                        state = 3
                    else:
                        state = -1
                    index += 1
                    return recursiveCheck(state, index)
                case -1:#-q1, a/b/x -> -q1, fail state, string is not accepted
                    index += 1
                    return recursiveCheck(state, index)
        else:
            return state
        
    finalState = recursiveCheck()
    if finalState != 4:#-1 is used to indicate error
        return -1
    return 0

inputStrings = ["bbabbbab", "bbbbbbbbbbbabbbbbbbbabbbbbbbbbbabbbbbb","abb", "baab", "babababab", "bbbbbabbbabaa",
            "aaaaaa", "bbbbbbbbbb", "babbba", "ABABABABA", "abababABababa",
            "babababzbab", "qwertyuiopsdfghjklzxcvnm", "1234567890", "!@#$%^&*()-_=+[]}{|;:\,.<>?/", ""]

outcomes = []
for inputString in inputStrings:
    print(inputString)
    outcomes.append(regexAB(inputString))
print(f"{inputStrings}\n{outcomes}")
