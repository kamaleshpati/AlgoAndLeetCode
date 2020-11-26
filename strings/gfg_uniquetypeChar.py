def Count(str): 
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)): 
        if str[i].isupper(): 
            upper += 1
        elif str[i].islower(): 
            lower += 1
        elif str[i].isdigit(): 
            number += 1
        else: 
            special += 1
    print('Upper:', upper) 
    print('Lower:', lower) 
    print('Number:', number) 
    print('Special:', special) 
  
str = "#GeeKs01fOr@gEEks07"
Count(str) 