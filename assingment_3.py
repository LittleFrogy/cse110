# -*- coding: utf-8 -*-


#task 1 wrong way


#B=input("enter somthing=")

#print(B[::-1])

#task 1

word=str(input("please enter word word="))
n=len(word)*-1
while n !=0:
  print(word[n],end==" ")
  n -= 1

print("")

#task 2 wrong way

#a=(input("enter a word length greater than 1="))

#b=int(input("enter a number="))

#c= str(a). index[b]

#c=a[b::-1]

#print(c[::-1])

#print(c)

#Task 2

a=input("enter a number length greater than 1=")

index=int(input("enter a number="))

b=""

for i in range(index,-1,-1):
  b=b+a[i]
if index==len(a)-1:
   print(b)
else:
  b=b+a[index+1:]
  print(b)

#task 2 wrong way

#word = str(input("Please enter a word: "))
#num = int(input("Please enter an index: "))

#first = word[:num+1]
#second = word[num+1:]
#rev = ""
#for r in range(1,len(first)+1):
  
#  rev = rev + first[-r]

#print(rev + second)

#task 3 wrong way

#number=(input("enter a number="))

#i=0

#while i < len(number):
  #digit = number[i]

  #if digit == '1' or digit == '0':
    #binary= True

  #else:
    #binary= False 
  #i +=1
#if binary:
  #print("binary number")

#else:
  #print("not binary number")

#task 3

a=input("enter a number=")

i=0

binary= True

while i < len(a) and binary:
  digit = a[i]

  if not (digit == '1' or digit == '0'):
    binary= False 
  i +=1
if binary:
  print("binary number")

else:
  print("not binary number")

"""#task4"""

a=input("enter a word=")

if len(a)>3:
  print(a+"er")

elif len(a)<4:
  print(a)

elif a.endswith('er'):
  print(a[:-2]+'est')

elif a.endswith('est'):
  print(a)

#task4 wrong way

#a=input("enter a word=")

#if len(a)<4:
  #print(a)

#elif len(a)>3:
  #if a.endswith('er'):
    #print(a[:-2]+'est')
  #elif a.endswith('est'):
    #print(a)
  #else:
    #print(a+'er')

#task4 wrong way

#n = str(input("Enter a word: "))
#s = len(n)

#if s>3:
 #   if n.endswith("er"):
  #      a=n.replace("er","est")
   #     print(a)
    #elif n.endswith("est"):
   #     print(n)
#    else:

#        print(n + "er")
#else:
 #   print(n)

#task4 wrong way

#a=input("enter a word=")
#size = len(a)
#b=a[-2:]
#c=a[-3:]
#est='est'
#if len(a)>3 and b=='er' :
#  ans= a.replace(a[size - 2:], est)
#  print(ans)
#elif len(a)<4 and b=='er':
#  ans= a.replace(a[size - 2:], est)
#  print(ans)

#elif len(a)>3 and c=='est':
#  print(a)

#elif len(a)<4 and c=='est':
#  print(a)

#elif len(a)<4:
#  print(a)
#elif len(a)>3:
#  print(a+'er')

#task5

a =str(input("Enter a word :"))
n=len(a)

for i in range(n):
    for len in range(i + 1, n + 1):
        print(a[i: len])
    break

#task 6

a = input("Enter a word :")
for i in a:
    b = ord(i)
    print(i ,':', b)

#task 6 wrong way

#a= input()

#for i in range(0,len(a),1):
 # print(a[i],":", ord(a[i]))

#task 7

a=input("Enter a word:")
for i in a:
    if i =="z":
        print("a", end="")
    else:
        print(chr(ord(i)+1) , end="")

#task 7 wrong way

#a=str(input("enter a word containing all small letters="))
#for i in range(0,len(a)):
#  ascii = ord(a[i])
#  ascii = ascii +1

#  if ascii>122:
#    ascii=97
#  else:  
#    ascii=chr(ascii)

#  print(ascii)

#task 7 wrong way

#a=str(input("enter a word containing all small letters="))

#b = ord(a)

#ascii = b +1

#if ascii>122:
#  z=97
#else:  
#  ascii=chr(ascii)

#print(ascii)

#task8

a = str(input("enter a word:"))
b =""

c = 0
d = ord('a') - ord('A')
for i in a:
    if c%2 == 1:
        e = chr(ord(i) - d)
        b += e
    c += 1

print(b)

#task9 wrong way

#a = input("Enter a word:")
#b =""

#for i in a:
#    if i not in b:
#        b=b + i
#print(b)

#task9

a=input('word')
b=''
b=b + a[0]
n=0
for i in a[1:]:
    if b[n]!=i:
        b=b+i
        n=n+1
print(b)

#task10

a = input()
b = 0
c = 0
while a[b] != ',':
    b += 1
a1 = b + 2
b2 = len(a)

temp = ''
while c < b and a1 < b2:
    temp += a[c] + a[a1]
    c += 1
    a1 += 1

if c < b:
    temp += a[c:b]
else:
    temp += a[a1:b2]

print(temp)

#task10 wrong way

#x=input() 
#a=""

#for i in range(len(x)):
   #if x[i]=="," :
     #y=x[0:i:]
     #z=x[i+2:len(x)+1:]

#print(y,z) 
#if len(y)>len(z) or len(y)==len(z):
   #for i in range(len(z)):
      #a=a+y[i]+z[i]
      #b=x[len(z): len(y):]
   #print(a+b)

#else:
  #for i in range(len(y)):
     #a=a+y[i]+z[i] 
     #b=x[len(y)+len(z)+1:len(x)+1:]
  #print(a+b)
