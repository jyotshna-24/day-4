#result function with N
def result(N):
    #iterate from 0 to N
    for num in range(N):
            #short-circuit operator is used
            if num % 5 == 0 and num % 7 == 0:
                print(str(num) + " ", end ="")
            else:
                pass
#driver code
if __name__ == "__main__" :
 #   #input goes here
    N = 100
    #calling function
    result(N)



num=5
2+22+222+2222+...n terms
res=0
st='2'
for i in range(1,num+1):
    res+=int(st*i)
    
print(res)


sum=0
while input("enter any integers or q to quit")!='q':
    sum=sum+int(input())
    
print(sum)



num=int(input("enter a number: "))
fac=1
i=1
while i<=num:
    fac=fac*i
    i=i+1
print("factorial of",num,"is",fac)    




st='python language is best programming language'
for i in range(len(st)):
    end_value='-'
    if st[i]==' 'or i==len(st)-1 or st[i+1]==' ':
        end_value=''
    if i%2==0:
        print(st[i].upper(), end=end_value)
    else:
        print(st[i],end=end_value)
print()        






