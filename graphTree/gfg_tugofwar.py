import sys 

def solveRecur(arr, n, curr_elements, num_of_encounters,soln, min_diff, Sum, curr_sum, curr_position): 
      
    
    if (curr_position == n):  
        return
  
    if ((int(n / 2) - num_of_encounters) >  (n - curr_position)): 
        return

    solveRecur(arr, n, curr_elements, num_of_encounters, soln, min_diff, Sum, curr_sum, curr_position + 1)  
  
    num_of_encounters += 1
    curr_sum = curr_sum + arr[curr_position]  
    curr_elements[curr_position] = True
  
    if (num_of_encounters == int(n / 2)): 
          
        if (abs(int(Sum / 2) - curr_sum) < min_diff): 
            min_diff = abs(int(Sum / 2) - curr_sum) 
            for i in range(n): 
                soln[i] = curr_elements[i] 
    else: 
        solveRecur(arr, n, curr_elements, num_of_encounters,soln, min_diff, Sum, curr_sum, curr_position + 1) 
        
    curr_elements[curr_position] = False
  
def solve(arr, n): 
    curr_elements = [False] * n  
    soln = [False] * n  
    min_diff = sys.maxsize  
    Sum = 0
    for i in range(n): 
        Sum += arr[i]  
  
    solveRecur(arr, n, curr_elements, 0,soln, min_diff, Sum, 0, 0)  
  
    print("The first subset is: ") 
    for i in range(n): 
        if (soln[i] == True): 
            print(arr[i], end = " ") 
    print() 
    print("The second subset is: ") 
    for i in range(n): 
        if (soln[i] == False): 
            print(arr[i], end = " ") 
  
arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]  
solve(arr, len(arr)) 
  
     
  
