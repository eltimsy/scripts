def count_feelings(s, arr):
    word = {}
    feelings = 0
    sentence = ''
    for letter in s:
        try:
            word[letter] += 1
        except:
            word[letter] = 1
    for b in arr:
        add = True
        newword = {}
        for let in b:
            try:
                newword[let] += 1
            except:
                newword[let] = 1
        for key, value in newword.iteritems():
            if add:
                try:        
                    if word[key] >= value:
                        pass
                    else:
                        add = False
                except:
                    add = False
        if add == True:
            feelings += 1
    if feelings == 1:
        sentence = '1 feeling.'
    else:
        sentence = str(feelings) + ' feelings.'
    return sentence

print(count_feelings('yliausoenvjw', ['anger', 'awe', 'joy', 'love', 'grief']))