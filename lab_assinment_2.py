#task 1

#a
start = 24
end = -6

while start >= end:
  if start == end:
    print(start , end= "")
  else:
     print(start, end= ", ")

  start -= 6  

print("\n")

#b

start = -10
end = 20

while start <= end:
  if start == end:
    print(start , end= "")
  else:
     print(start, end= ", ")

  start += 5 

print("\n")

#c

start = 18
end = 63

while start <= end:
  if start == end:
    print(start , end= "")
  else:
     print(start, end= ", ")

  start += 9 

print("\n")

#d

start = 18
end = 63

while start <= end:
  if start%2 ==0:
    print(start, end= ", ")

  elif start == end:  
     print(start*-1)
  else:
    print(start*-1, end= ", ")   

  start += 9

#task 2

fav_car = input("enter the name of your favorite car=")
print_num = int(input("enter a Number="))

start = 0

while start < print_num:
  print(fav_car)
  start +=1

#task 3

start = 0
end =600
sum=0

while start <= end:
  if start % 7 ==0 and start % 9 ==0:
    sum += start
  start +=1

print(sum)

#task 4

start = 0
end =600
sum=0

while start <= end:
  if start % 7 ==0 and start % 9 ==0:
    sum!=start
    
  elif start % 7 ==0 or start % 9 ==0:
    sum += start
  start +=1

print(sum)

#task 5

a=[]
for i in range(10,50,1):
    if i%2!=0:
        a.append(i)            
print(*a, sep = " ")

#task 6

n=int(input('number='))
result = 0
for i in range(1, n + 1) :
        if (i % 2 == 0):
            result = result - pow(i, 2)
        else:
            result = result + pow(i, 2)
print(result)

#Task 7

total=0 
count=0 
for i in range(0,10):
    num = int(input())
    if(num%2):
        total+=num
        count+=1 
print("The total of the odd numbers is",total,"and their average is",count)

#task 8

N=int(input('n='))
m = N // 7
sum = m * (m + 1) / 2
ans = 7 * sum
print(ans)

#task 9

count=1
sum=0
while count<=5:
  num=int(input("Number: "))
  sum +=num

  count +=1
  print(sum)

#task 10

a=int(input(''))
while a>0:
    b=a % 10
    a=a//10
    print(b,end =", ")

print(" ")

#task 11

a=int(input(''))
count=0
while a>0:
    a=a//10
    count=count+1
print(count)

#task 12

n=int(input())
x=n
track=0

while n!=0:
  n=n//10
  track +=1

power=10**(track-1)

while power>0:

  result=x//power
  x=x%power
  power=power//10

  if power==0:
    print(result)
  else:
     print(result, end=', ')

#task 13

n=int(input())

for i in range(1,n+1):
   if n%i==0:

    if i==n:
      print(i)
    else:
      print(i,end=', ')

#task 14

n=int(input())

sum=0

for i in range(1,n):

  if n%i==0:
     sum+=i

if n==sum:

    print(f"{n} is a perfect number")

else:

  print(f"{n} is not a perfect number")

#task 15

n=int(input())
track=0

for i in range(1,n+1):
   if n%i==0:
      track +=1

if track==2:
  print(n, 'is a prime number') 
else:
   print(n, 'is not a prime number')

#task 16

sum=0

min=float('inf')
max=float('-inf')

n1=int(input())

for v in range(n1):
  n2=int(input()) 
  sum +=n2

  if n2>max:
    max=n2
  elif n2<min:
     min=n2

avg=sum/n1

print('Maximum', max)

print('Minimum', min)

print('Average', avg)

"""#task 17"""

n = int(input("N:"))
i = 0

while(i < n):
    j = 0
    while(j < n):      
        j = j + 1
        print('+', end = '')
    i = i + 1
    print('')

#task 18

m = int(input('Row='))
n = int(input('Colum='))
for i in range(m):
    for j in range(1, n+1):
        print(j, end='')
    print('')

#task 19

rows = int(input())
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print('')
