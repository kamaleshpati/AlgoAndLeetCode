MAX_CHARS = 26
   
def longestSubseqWithK(str, k):     
  
    n = len(str)                   
    freq = [0]*MAX_CHARS                  
    for i in range(n):   
        freq[ord(str[i]) - ord('a')]+=1              

    for i in range(n ): 
        if (freq[ord(str[i]) - ord('a')] >= k):                
            print(str[i],end="") 
            
str = "geeksforgeeks"
k = 2
longestSubseqWithK(str, k)