#task 1

var1 = int(input("please input first number"))
var2 = int(input("please input second number"))

total = var1 + var2

product = var1 * var2

difference = var1 - var2

print("Sum =", total)

print("Product =", product)

print("Difference =", difference)

#task 2

import math

r = float(input("enter redius"))

area = math.pi * (r**2)

print("Area:",area)

#task 3

num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

if num1 > num2:
  print("first one is greater")

elif num1 < num2:
  print("secoond one is greater")

elif num1 == num2:
    print("both are equal")

"""#task 4

"""

num1 = int(input(print("please enter a number")))

num2 = int(input(print("please enter a number")))

sum1= num1 - num2

sum2= num2 - num1

if num1 > num2:
  print("Sum",sum1)

else:
  print("Sum",sum2)

"""#task 5"""

num1 = int(input(print("please enter a number")))

var1 = num1 % 2
 
if var1 == 0:
  print("even")

else:
  print("odd")

"""#task6

"""

num1 = int(input(print("please enter a integer number")))

var1 = num1 % 2

var2 = num1 % 5

if var1==0 or var2==0:
  print(num1)

else:
   print("Not a multiple of 2 OR 5")

"""#task7"""

num1 = int(input(print("please enter a integer number")))

var1 = num1 % 2

var2 = num1 % 5

if var1==0 and var2==0:
  print(num1,"\nMultiple of 2 and 5 both")


elif var1==0 or var2==0:
  print(num1)

else:
   print("Not a multiple of 2 OR 5")

"""#task8"""

num1 = int(input(print("please enter a integer number")))

var1 = num1 % 2

var2 = num1 % 5

if var1==0 and var2==0:
  print(num1,"\nMultiple of 2 and 5 both")

else:
   print("Not a multiple of 2 OR 5 both")

"""#task9"""

num1 = int(input(print("please enter The number of seconds")))

var1 = num1//3600

var2 = num1%3600

var3 = var2//60

var4 = var2%60


print("Hours:",var1 ,"\nMinutes:",var3,"\nSeconds:",var4)

"""#task10"""

num1 = int(input(print("please enter The number of hours")))

if num1 < 0:
  print("Hour cannot be negative")

elif num1 <= 40:
  var1= num1 * 200
  print(var1)

elif num1 > 40:
  var2 = 8000 + ((num1-40) *300)
  print(var2)

elif num1 > 168:
  print("Impossible to work more than 168 hours weekly")

"""#task11"""

S = int(input(print("please enter a value of S which integer number")))

if S < 100:
  L = 3000-(125*(S**2))
  print("L=",L)

elif S >= 100:
  L = 12000 / (4 + ((S**2) / 14900))
  print("L=",L)

"""#task12"""

num1 = int(input(print("please enter The number of hours")))

if num1 < 0 or num1 >= 24: 
  print( "Wrong Time")

elif num1>=4 and num1<=6:
  print("Breakfast")

elif num1 >=12 and num1 <=13:
  print(" Lunch")

elif  num1 >=16 and num1 <=17:
  print("Snacks")

elif  num1 >=19 and num1 <=20:
  print("Dinner")

else:
  print("Patience is a virtue")

"""## task 13"""

num1 = int(input(print("please enter marks")))

if num1 < 0 or num1 > 100: 
  print( "invalid marks")

elif num1>=0 and num1<=49:
  print("F")

elif num1 >=50 and num1 <=59:
  print("E")

elif  num1 >=60 and num1 <=69:
  print("D")

elif  num1 >=70 and num1 <=79:
  print("C")

elif  num1 >=80 and num1 <=89:
  print("B") 

else:
  print("A")

"""## task 14"""

a=float(input('meter '))
b=int(input('second '))
c=float(a/b*3.6)
print(c,' km/h')
if c<60:
  print('Too slow. Needs more changes.')
elif c>= 60 and c<= 90:
  print('Velocity is okay. The car is ready!')
elif c>90:
  print('Too fast. Only a few changes should suffice.')

"""#task 15"""

a=float(input('cgpa- '))
b=int(input('credit- '))

if a>=3.8 and b>=30:
  if a>=3.8 and a<=3.89:
    c=25
  elif a>=3.9 and a<=3.94:
    c=50
  elif a>=3.95 and a<=3.99:
    c=75
  elif a==4:
    c=100
  print('The student is eligible for a waiver of',c, '%')
else:
  print('The student is not eligible for a waiver')
