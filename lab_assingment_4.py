#task1 wrong way

#n = int(input("Enter number of elements: "))
#lst= []  
#for i in range(0, n):
 #   a=int(input())
  #  lst.append(a)
#print(lst)

#task1

lst= []
for i in range(5):
    n = int(input("Enter a number: "))
    lst.append(n)
    print("Numbers in the list:",lst)

#task2

list1=[int(item) for item in input("enter a list: ").split(",")]

if len(list1)<4:
  print("Not possible")
else:
  print(list1[2:-2])

#task2 wrong way

#var=int(input("enter the number"))
#l=[]
#if var<4:
 # print("Not possible")
#else:
 # for i in range(var):
  #  num=int(input("number="))
   # l.append(num)
  #print(list1[2:-2])

#task3 wrong way

#n = int(input("Enter number of elements: "))
#lst=[]  
#for i in range(0, n):
 #   a=int(input())
  #  lst.append(a)
#for i in lst[::-1]:
 # print(i)

#task3 wrong way

#lst=[int(item) for item in input("enter a list: ").split(",")] 
#for i in lst[::-1]:
 # print(i)

#task3

lst=[]
for i in range (5):
   var = int (input ("")) 
   lst.append(var)
print("Input data:",lst)
for i in lst[::-1]:
  print(i)

#task4 wrong way

#l1=
#l2=[]
#for item in l1:
 # l2.append(item**2)

 #print(l2)

#task4 wrong way

#lst=[int(item) for item in input("enter a list: ").split(",")] 

#for i in range(len(lst)): 
 #   lst[i]=lst[i]**2 

#print(lst)

#task4

lst=[1, 2, 3, 4, 5, 6, 7] 

for i in range(len(lst)): 
    lst[i]=lst[i]**2 

print(lst)

#task5

list_given = ["hey", "there", "", "what's", "", "up", "", "?"]
new_list =[]
for x in list_given:
    if x!='':
        new_list.append(x)
print("original List:",list_given)        
print("Modified List:",new_list)

#task6 wrong way

#n = int(input("Enter number of elements:"))
#lst=[]  
#for i in range(0, n):
 #   a=int(input())
  #  lst.append(a)
#max=lst[0]
#maxindex=0    
#for i in range(1,len(lst),1):
 # if i>max:
  #  max=i
   # maxindex +=1
#print(max)
#print(maxindex)

#task6 wrong way

#a = []
#num = int(input("Enter the Number: "))
#max = num
#sum = num
#i = 2
#a.append(num)
#while i < 8:
#    num = int(input("Enter the Number: "))
 #   sum += num
  #  if num > max:
   #     max = num
    #i += 1
    #a.append(num)
#q = a.index(max)

#print('list: ', a)
#print('Lagest number ', max, 'was found at location ', q)

#task6 wrong way

#var1 = input ("Enter the number's: ")
#lst1 =[]

#count=0

#var2 =var1[1:-1]
#var3 = var2.split(',')
#for i in var3:
 # lst1.append((i))
#max=lst1[0]
#for i in lst1:
#  if i>max:
 #   max=i

#for i in lst1:
 # if i!=max:
  #   count += 1
  #elif i == max:
   # break
#print("my list",lst1)
#print("largest",count)

#task6

lst = input().split(',')

for i in range(0,len(lst)) :
	lst[i] = int(lst[i])

print("My list:",lst)

max_num = lst[0]

for i in lst:
  if max_num < i :
    max_num = i

ind = lst.index(max_num)
print("Largest number in the list is", max_num , "which was found at index", ind)

#task7 wrong way

#List_one = [int(item) for item in input("enter a list: ").split(",")]
#List_two = [int(item) for item in input("enter a list: ").split(",")]
#List_one[-1:] = List_two
#print(List_one)

#task7

List_one = [1, 4, 7, 5]
List_two = [6, 1, 3, 9]
List_one[-1:] = List_two
print(List_one)

#task8 wrong way

#list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#list_two = [10, 11, 12, -13, -14, -15, -16]
#a = list_one + list_two
#print(a[1::2])

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
list1=[]
list2=[]
for i in list_one:
  if i%2==0:
    list1.append(i)
for j in list_two:
  if j%2==0:
    list2.append(j)    
a = list1 + list2
print(a)

#task9

s=input("enter values of list using space:")
list1=[]
list2=[]
s1=""
for character in s:
  if character!=" ":
    s1=s1+character
  else:
     list1.append(int(s1))
     s1=""
list1.append(int(s1))     
print("Original list:",list1)
for i in list1:
  if i%2!=0:
    list2.append(i)
print("Modified list",list2)

#task 10 wrong way

#a = input("Enter a list of numbers: ")
#a = a.split(",")
#list  =  []
#for i in a:
 # if i == "[" or i =="]" or i =="," or i==" ":    
  #  continue
  #elif int(i) not in list:
   # list.append(int(i))
#print("Modified list:",list)

#task 10 wrong way

#s=input("enter values of list using comma:")
#list1=[]
#list2=[]
#s1=""
#for character in s:
 # if character!=",":
  #  s1=s1+character
  #else:
   #  list1.append(int(s1))
    # s1=""
#list1.append(int(s1))     
#for i in list1 :
 # if i == "[" or i =="]" or i =="," or i==" ":    
  #  continue
  #elif int(i) not in list1:
   # list2.append(int(i))
#print("Original list:",list1)    
#print("Modified list:",list2)

#task 10

a=input().split(', ')

lst1=[]
lst2=[]

for i in a :
  lst1.append(int(i))

print('Original list:', lst1)

for j in lst1 :
  if j not in lst2:
    lst2.append(j)
print("Modified list:", lst2)

#task11

List_one=[1, 4, 3, 2, 6]
List_two=[5, 6, 9, 8, 7]
common=False
for item in List_one:
  if item in List_two:
    common=True
    break
print(common)
