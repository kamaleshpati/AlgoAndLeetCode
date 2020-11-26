def strMatching(str, pattern, n, m): 
      
    if (m == 0): 
        return (n == 0) 
          
    lookup = [[False for i in range(m + 1)] for j in range(n + 1)] 
      
    lookup[0][0] = True
      
    for j in range(1, m + 1): 
        if (pattern[j - 1] == '*'): 
            lookup[0][j] = lookup[0][j - 1] 
              
    for i in range(1, n + 1): 
        for j in range(1, m + 1): 
            if (pattern[j - 1] == '*'): 
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j] 
            elif (pattern[j - 1] == '?' or str[i - 1] == pattern[j - 1]): 
                lookup[i][j] = lookup[i - 1][j - 1] 
            else: 
                lookup[i][j] = False
      
    return lookup[n][m] 


str = "baaabab"
pattern = "*****ba*****ab" 
  
if (strMatching(str, pattern, len(str),len(pattern))): 
    print("Yes") 
else: 
    print("No") 
