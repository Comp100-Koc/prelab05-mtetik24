def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while True:
        res=""
        i=0
        while i < len(s):
            if i+1<len(s) and s[i]==s[i+1]:
                i+=2
                
            
            else:
                res+=s[i]
                i+=1
        if s==res:
            return s
        s=res
    return s