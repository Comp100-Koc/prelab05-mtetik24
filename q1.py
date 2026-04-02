def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """

    result=""
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            x = s[i:j]
            if x == x[::-1] and len(x) > len(result) and len(x)>2:
                result = x
    return result
                    
    
            