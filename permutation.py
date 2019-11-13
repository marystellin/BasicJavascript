"""num,m=map(int,input().split())
factorial1 = 1

for i in range(1,num + 1):
	factorial1 = factorial1*i
result=num-m
factorial2=1
for i in range(1,result + 1):
	factorial2 = factorial2*i
result1=factorial1/factorial2
print(int(result1))"""

"""import math
N,M=map(int,input().split())
if(N>=M):
    print(math.gcd(N,M))
else:
    print(-1)"""


"""N=int(input())
if N%4==0:
 	print("YES")
else:
  print("NO")"""

"""def decimalToBinary(n):
return bin(n).replace("0b","")

# Driver code
if __name__ == '__main__':
    print(decimalToBinary(8))
    # print(decimalToBinary(18))
    # print(decimalToBinary(7))"""

"""N=int(input())
if N>1:
    for i in range(2,N):
        if(N%i!=0):
	        print("yes")
            break
    else:
	print("no")"""


"""number = int(input())

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("no")
            break
    else:
        print("yes")"""


"""n=int(input())
def catalan_number(num):
    if num <=1:
         return 1

    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num

for n in range(10):
    print(catalan_number(n))"""

"""num = int(input())

temp = num
rev = 0

while temp != 0:
	rev = (rev * 10) + (temp % 10)
	temp = temp // 10

if num == rev:
	print("yes")
else:
	print("no")"""

"""A,B,C=map(int,input().split())
if(A+B+C==180):
  print("yes")
else:
	print("no")"""


"""def decimalBinary(num):
    if num > 1:
        decimalBinary(num // 2)
    print(num % 2, end='')
number = int(input())

decimalBinary(number)"""

"""n=int(input())
print(bin(n)[2:])"""

"""N=int(input())
count=0
for i in range(0,len(N)):
	count=count+1
print(count)"""

"""fACTOR
N=int(input())
if(N<=100000):
  count=0;
number=int(N);
for i in range(1,number+1):
	if number%1==0:
    	print(i,end="");
		i+=1;
		count+=1;
if count==0:
	print(number)"""

"""N =input()
print(int(N,2))"""

"""N, K = map(int, input().split())
list1 = list(map(int, input().split()))[:N]
count = 0
for i in range(0, len(list1)):
    if K == list1[i]:
        count = count+1
print((count)-1)"""

"""s=input()
print(''.join([s[x:x+2][::-1]for x in range(0,len(s),2)]))"""


"""N=int(input())
list1=list(map(int,input().split()))[:N]
print(min(list1),max(list1))"""

"""N = int(input())
arr = list(map(int, input().split()))[:N]
if(N <= 100000):
    for i in range(0, int(N)):
        ans = arr[i] | arr[i+1]
        break
print(ans)"""

"""def oddswap(st)
s=list(st)
for i in range(0,len(s),2):
	t=s[i]
	s[i]=s[i+1]
	s[i+1]=t
return "".join(s)"""


"""N, K = map(int, input().split())
list1 = list(map(int, input().split()))[:N]
for i in range(0, len(list1)):
    if(K == list1[i]):
        print("yes")
        break
else:
	print("no")"""

"""N, K = map(int, input().split())
if N<K:
	result=N-K
	print(-(result))"""

"""N = int(input())
list1 = list(map(int, input().split()))[:N]
if(N <= 100000):
    for i in range(0, len(list1)):
        result = list1[i] & list1[i+1]
        break
print(result)"""


"""def checkvalid(A, B, C):
    if(A,B,C <= 100000):
        if(A+B <= C) or (A+C <= B) or (B+C <= A):
            return false
        else:
            return True
A, B, C = map(int, input().split())
if checkvalid(A, B, C):
    print("yes")
else:
    print("no")"""

"""N=int(input(),2)
print(oct(N)[2:])"""

"""N,K=map(int,input().split())
print(N<<K)"""

"""N=int(input(),2)
print(hex(N)[2:])"""

"""N=int(input())
list1=list(map(int,input().split()))
for i in range(0,len(list1)):
    break
print((list1[i])^(list1[i+1]))"""

"""s=input()
N=len(s)
if N<=10000000:
	print(s.swapcase())"""

"""N,M=input().split()
if N in M:
	print("yes")
else:
	print("no")"""

"""S,A=input().split()
if A in S:
	print(A)"""

"""list1=list(map(int,input().split()))
for i in range(0,len(list1)):
	result=list1[i]+list1[i-1]
print(result)"""

"""from datetime import date
def main():
    today=date.today()
    print(today)
if __name__=="__main__":
    main()
    print("yes")
else:
    print("no")"""

"""#S= input()
S = list(input().split())
count = 0
for i in range(0, len(S)):
        count = count+1
print(count)"""

"""N,M=input().split()
if N==M:
	print("yes")
else:
	print("no")"""


"""from datetime import date
def main():
    today=date.today()
    print(today)
if __name__=="__main__":
    main()
    month=month.today()
    print(month)"""

"""N=int(input())
list1=list(map(int,input().split()))[:N]
list1.sort()
print(list1)"""

"""print("Enter 'x' for exit.")
string = list(input().split())
if string == 'x':
    exit()
else:
    print("\nString after sorted in alphabetical order:")

    print(''.join(sorted(string), end=" "))"""

"""def sumOdd(n):
	terms=(n+1)//2
	sum1=terms*terms
	return sum1
def suminRange(l,r):
	return sumOdd(r)-sumOdd(l-1)
l,r=map(int,input().split())
print(suminRange(l,r))"""

"""def print_factors(x):

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = int(input("Enter a number: "))

print_factors(num)"""

"""x = int(input())
for i in range(1, x+1):
    if x % i != 0:
        if i % 2 == 0:
            print(i, end=" ")"""


"""hexdec = input()
dec = int(hexdec, 16)
print(str(dec))"""


"""list1=list(map(int,input().split()))
print(min(list1))"""

"""base,height=map(int,input().split())
area = (base*height)/2
print(int(area))"""

"""# sin 30 value for zero degrees
import math

Radians30           = math.radians(30)

sin30               = math.sin(Radians30)

sin30Rounded        = round(sin30,2)
print(format(sin30Rounded))"""


"""x = int(input())
for i in range(1, x+1):
    if x % i != 0:
        if i % 2 == 0:
            print(i, end=" ")"""

"""def computeHCF(N, K):
    if N > K:
        smaller = K
    else:
        smaller = N
    for i in range(1, smaller+1):
        if((N % i == 0) and (K % i == 0)):
            hcf = i
    return hcf
num1,num2 =map(int,(input().split()))
print(computeHCF(num1, num2))"""

"""x = int(input())
for i in range(1, x+1):
    if x % i == 0:
        if i % 2 != 0:
            print(i, end=" ")"""

"""def isPowerOfTwo(N): 
    while (N != 1): 
            if (N % 2 != 0): 
                return False
            N = N // 2
              
    return True
N=int(input())   
if(isPowerOfTwo(N)): 
    print('Yes') 
else: 
    print('No') """

"""N,K=map(int,input().split())
if(K*K==N):
    print("yes")
else:
    print("no")"""
"""
A,B,C=map(int,input().split())
triangle=A+B+C
if(triangle==180):
	print("yes")
else:
  	print("no")"""

"""a,b,x=map(int,input().split())
y=(a*x)+b
print(y)"""

"""A,B,C=map(int,input().split())
result=(C*(2*A+(C-1)*B))/2
print(int(result))"""

"""N=input()
print(int(N,2))"""
"""
def isnumeric(N)
N=input()
if(N==isnumeric()):
    print("yes")
else:
    print("no")"""

"""def nCr(n, r): 
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
def fact(n): 
    res = 1
    for i in range(2, n+1): 
        res = res * i 
    return res 
n,r=map(int,input().split())
print(int(nCr(n, r))) """

"""A,B,C=map(int,input().split())
result=(A^B)%C
print(result)"""

"""N = int(input())
Reverse = 0
while(N > 0):
    Reminder = N %10
    Reverse = (Reverse *10) + Reminder
    N = N //10

print(Reverse)"""

"""#import math
N=float(input())
print(round(N))"""

"""N=int(input())
if(N%11==0):
	print("YES")
else:
	print("NO")"""


"""def reverseWordSentence(Sentence):
	words=Sentence.split(" ")
	newWords=[word[::-1] for word in words]
	newSentence=" ".join(newWords)
	return newSentence
S=input()
print(reverseWordSentence(S))"""

"""l,r=map(int,input().split())
for i in range(10,130):
    if (l%i==0 and l%i+1==0):
        print(l)
else:
    print(r)
"""
"""
N= int(input())
list1 = list(map(int,input().split()))[:N]
for i in range(0,N-1,2):
	temp=list1[i]
	list1[i]=list1[i+1]
	list1[i+1]=temp
print(' '.join(str(x)for x in list1))"""

"""import math
N, M = map(int, input().split())
if M == 0 or N == 0:
        print(-1)
else:
    print(math.gcd(N, M))"""
# anagram example
"""
def is_anagram(str1, str2):
    list_str1 = list(str1)
    #list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()
    if(list_str1 == list_str2):
        print(1)
    else:
        print(0)
s1=input()
s2=input()
is_anagram(s1,s2)
#print(is_anagram('cat','rat'))
"""
# camel case example
"""def convert(s): 
    if(len(s) == 0): 
        return
    s1 = '' 
    s1 += s[0].upper() 
    for i in range(1, len(s) - 1): 
        if (s[i] == ' '): 
            s1 += s[i + 1].upper() 
            i += 1
        elif(s[i - 1] != ' '): 
            s1 += s[i]  
    print(s1)      
def main(): 
    s = input()
    convert(s) 
      
if __name__=="__main__": 
    main() """
# string rotating ex:i am ruby=>i ma ybur
"""s=input()
words=s.split(" ")
newword=[word[::-1] for word in words]
newSen=" ".join(newword)
print(newSen)"""

"""N=input()
print(ord(N))"""

"""s=input()
N=list(s)
for i in range(0,len(N)):
     a=ord(N[i])
     b=ord(N[i+1])
     c=ord(N[i+2])
print(a,b,c)"""
# find ascii sum
"""S=input()
N=list(S)
M=[]
for i in range(0,len(N)):
    M.append(ord(N[i]))
print(sum(M))"""

"""S=input()
N=list(S)
sum=0
for i in range(0,len(N)):
    sum=sum+i
print(sum)"""

"""N=input()
if(N.isnumeric()):
	print("yes")
else:
	print("no")"""

"""def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
    if (s == rev): 
        return True
    return False
s=input()
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") """

"""def sortSen(Sen): 
    words = Sen.split(" ")  
    words.sort() 
    newSentence = " ".join(words) 
    return newSentence 
S= input()
print(sortSen(S)) """

"""def revEachWord(Sen): 
    words = Sen.split(" ") 
    newWords = [word[::-1] for word in words]  
    newvalue = " ".join(newWords) 
    return newvalue   
S = input()
print(revEachWord(S))"""

"""s=input()
val=[]
val.append(s)
val.append("answer")
print(" ".join(val))"""

"""from collections import OrderedDict
def remove_duplicate(str1):
	return "".join(OrderedDict.fromkeys(str1))
S=input()
print(remove_duplicate(S))
"""

"""
def toString(List):
    return ''.join(List)


def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]


string = input()
n = len(string)
a = list(string)
permute(a, 0, n-1)"""

"""s1,s2=(input().split())
if s2 in s1:
	print("Yes")
else:
	priint("No")"""


def rem_vowels(s):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in s:
        if x in vowels:
            s = s.replace(x, "")
    print(s)


s = input()
rem_vowels(s)
