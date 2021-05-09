#list of numbers
list1=[10,21,4,15,66,93,1]
even_count, odd_count =0, 0
#iterating each number in list
for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers in the list: ", even_count)      
print("Odd numbers in the list: ", odd_count)



maximum=max(list1)
print(maximum)

minimum=min(list1)
print(minimum)







# Python program to count and 
# print all palindrome numbers in a list. 
  
def palindromeNumbers(list_a): 
  
    c = 0
  
    # loop till list is not empty 
    for i in list_a:             
  
        # Find reverse of current number 
        t = i 
        rev = 0
        while t > 0: 
            rev = rev * 10 + t % 10
            t = t // 10
  
        # compare rev with the current number 
        if rev == i: 
            print (i) 
            c = c + 1
  
    print()
    print ("Total palindrome nos. are", c )
    print()
  
# Driver code 
def main(): 
  
    list_a = [10, 121, 133, 155, 141, 252] 
    palindromeNumbers(list_a) 
  
    list_b = [ 111, 220, 784, 565, 498, 787, 363] 
    palindromeNumbers(list_b)                     
  
if __name__=="__main__": 
    main()             # main function call 