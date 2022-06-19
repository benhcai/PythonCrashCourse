def split(w):
    # init array
    # track index
    # loop through word, index i
        # if el length is not 0, and w[i] is " ", iterate i
        # if char is not " ", push to el
    s = []
    curr = ""
    for l in w:
        if l != " ":
           curr += l 
        if len(curr) != 0 and l is " ":
            s.append(curr)
            curr = ""
            continue
    if len(curr) != 0:
        s.append(curr)
    return s

#print("split " + str(split(" hi there   ")))
#print("split " + str(split("hi   ")))
#print("split " + str(split("hi my name")))
#print("split " + str(split("")))
#print("split " + str(split(" ")))
#print("split " + str(split("a a")))

def split2(w):
    s = []
    i = 0
    word = ""
    for char in w:
        if char != " ":
            word += char
        if len(word) != 0 and (char == " " or i == len(w) - 1):
            s.append(word)
            word = ""
        i += 1
    return s

#print(split2('hi ab'))

def split_id(w):
    s = []
    word = ""
    for i, char in enumerate(w):
        if char != " ":
            word += char
        if len(word) != 0 and (char == " " or i == len(w) - 1):
            s.append(word)
            word = ""
    return s
#print(split_id("hi b"))
#print(split_id(" H A "))
#print(split_id(""))
#print(split_id(" "))
print(split_id(" hi me   "))
