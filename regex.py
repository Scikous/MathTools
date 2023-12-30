####deprecated
#{a,b},
# q0, a-> q0, b -> q1,  #q0error
#q1, a -> q2, b -> q1   #move on if b
#q2, b-> q3, a->q0 # index not final, q1
#any char -> q0
####
# def regex_bab(input_string: str):
#     def recursive_check(state=1, index=0): #states 1-4
#         if len(input_string) > index:
#             letter = input_string[index].lower()
#             match state: #case 0 is not used as it could cause confusion
#                 case 1:#q1, a/x -> -q1, b -> q2
#                     if letter == 'b':
#                         state = 2
#                     else:
#                         return -1
#                     return recursive_check(state, index+1)
                    
#                 case 2:#q2, a -> q3, b -> q2, x -> -q1
#                     if letter == 'a':
#                         state = 3
#                     elif letter != 'b': #if b -> state = state
#                         return -1
#                     return recursive_check(state, index+1)

#                 case 3:#q3, a/x -> -q1, b -> q4 
#                     if letter == 'b':
#                         state = 4
#                     else:
#                         return -1
#                     return recursive_check(state, index+1)
#                 case 4:#q4, a -> q3, b -> 4, x -> -q1,  case 4 = accepted state
#                     if letter == 'b':
#                         state = 4
#                     elif letter == 'a':
#                         state = 3
#                     else:
#                         return -1
#                     return recursive_check(state, index+1)
#         else:
#             return state
        
#     final_state = recursive_check()
#     if final_state != 4:#if not accepted state, then FAIL
#         return 'FAIL'
#     return 'PASS'

###Final
def regex_bab(input_string: str):
    state = 1
    for letter in input_string:
            match letter.lower(): #states from q1-q4, and FAIL. x = anything that is not 'a', 'b', 'A' or 'B' 
                case 'b':
                    if state == 1:#q1, a or x -> -q1, b -> q2
                        state = 2
                    elif state == 3: #q3, a or x -> -q1, b -> q4
                         state = 4
                    else:#q2 or q4, b -> q2 or b -> q4
                         state = state
                case 'a':
                    if state == 2:#q2, a -> q3
                         state = 3
                    elif state == 4:#q4, a -> q3
                         state = 3
                    else:#q1 and q3, a -> FAIL
                         state = -1
                         break
                case _:#x -> FAIL
                      state = -1
                      break
    if state != 4:#case 4 = accepted state
        return 'FAIL'
    return 'PASS'

if __name__ == '__main__':
    input_strings = ["bbabbbab", "bbbbbbbbbbbabbbbbbbbabbbbbbbbbbabbbbbb","abb", "baab", "babababab", "bbbbbabbbabaa",
                "aaaaaa", "bbbbbbbbbb", "baBabbbbabBBBabbb", "babbba", "ABABABABA", "abababABababa", "BABABABBBBBABBBBAB",
                "babababzbab", "qwertyuiopsdfghjklzxcvnm", "1234567890", "!@#$%^&*()-_=+[]}{|;:\,.<>?/", ""]

    outcomes = []
    for input_string in input_strings:
        print(input_string)
        outcomes.append((input_string, regex_bab(input_string)))
    print("Results:\n",outcomes)