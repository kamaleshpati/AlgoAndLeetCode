from collections import Counter 
  
def common(str1,str2): 
    dict1 = Counter(str1) 
    dict2 = Counter(str2) 
    commonDict = dict1 & dict2 
  
    if len(commonDict) == 0: 
        print -1
        return
    commonChars = list(commonDict.elements()) 
    commonChars = sorted(commonChars) 
    print(''.join(commonChars)) 
  
str1 = 'geeks'
str2 = 'forgeeks'
common(str1, str2)