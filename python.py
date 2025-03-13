mySet = list(("baan", "yo", "YEh", "lu", "tr"))
print(mySet)

thisDictionary = dict(
  apple = "yellow"
)
del(thisDictionary["apple"])
print(thisDictionary)


listOne = ["orange", "apple", "mango", "ice"]
listTwo = ["green", "red", "green", "white"]
myDict = dict(zip(listOne, listTwo))
print(myDict)

# arithemetic operators
print(10 * 5) #multiplication
print(4 - 11) #substraction
print(12/6)   #division
print(5+9)    #addition
print(6//2)    #floor divion
print(10 % 4)   #modulus
print(2**4)     #exponential


#Assignment Operators
x = 5
x += 6
x -= 7
x *= 8
print(x)


# conditional operators
x = 5
y = 10 
print(x==y)
print(x < y)
print(x > y)
print(x!=y)
print(x or y)
print(x and y)

# conditional statement
a = 10
b =30
if a > b:
  print("a is greater than b")
elif a == b:
  print("a  is equals to b")
else:
  print("a is less than b")

Name = "my name is vivian cherry"
if "vivian" in Name:
  print("hello vivian")
elif "cherry" in Name:
  print("Hello, cherry")
else:
  print("name vivian isnt found")

listOne = ["a", "b","c"]
listTwo = []

Name = input("Enter your name:")
program = input("Enter your program(techrise / stream B): ")
if "techrise" == program:
  print("hello", Name, "Your program is techrise")
elif "stream B"== program:
  print("Hello", Name,"Your track is stream B" )
else:
  print(f"we do not recognize {Name} in this class")

  # third Assignment
first = [""]
myVar = input("Enter your local government: ")
clarity = input("Are you through (yes/no): ")
if clarity == "no":
  print(myVar )
else:
  print(first)

mybar = ["an", "to", "so"]
print("te" in mybar)
print("to" not in mybar)
i = 1
while i < 5000:
 print(i)
 if i == 4998:
  break  
 i += 1

ybar = ["an", "to", "so"]
for x in ybar:
  if x == "to":
   continue
print(x)


age = int(input("Enter your age: "))
if age < 10:
  print("children")
elif age > 60:
  print("Senior citizens")
else:
    print("normal citizen")

list = [1, 2, 3, 4, 5, 6,]
for num in list:
  if num % 2 == 0:
    print(num)

mynum = int(input("Enter an input: "))
if mynum % 2 == 0:
  print("it is an even number")
else:
  print("It is odd")


# create a program that ask users their ages and classify them into age gropus:
# teen: 13 - 19
# Adult: 20 -64
# Senior: 65+


age = int(input("Please can i have your age: "))
if age < 19:
  print("teen")
elif  age >=20 and age <=64:
   print("Adult")
elif age >= 65:
  print("senior")
else:
  print()
str = "WESTAFRICA"
myList = ["solace", "lekwauwa", "kind", "vivian" ]
for i in str:
  print(i)
  
  
  
for i in myList:
    print(i)
    print(i)
    
    
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num:
  i *= 10
  print(i)
    
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_squared = []
for i in num:
  i **= 2
  num_squared.append(i)
  print(num_squared)
    
i = 1
while i < 14:
 print(i)
 if i == 7:
  continue
 i += 1
fruits = ["apple", "banana", "cherry"]
print(fruits[0][1])

for x in fruits :
  print(x) 


adj = ["red", "big", "tasty"]
fruits =["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x,y) 
  
  

print("# ")
print("# ")
print("# ")
print("# ")
for i in range(4):
  for j in range(4):
    print('#', end='')
  print()


