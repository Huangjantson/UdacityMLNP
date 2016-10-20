def NextWordProbability(sampletext,word):
    
    splited_memo = sample_memo.split()
    
    counted = {}
    
    for i in range(1,len(splited_memo)):
        #finding the key in dict
        this_word = splited_memo[i]
        word_before = splited_memo[i-1]
        if word_before == word:
            if counted.get(this_word,-1) == -1:
                #not exist then add to the dict
                counted[this_word] = 1
            else:
            #exist then increase the logged number
                counted[this_word] += 1
            
    return counted