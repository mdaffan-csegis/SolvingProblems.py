#Print the first 10 natural numbers using for loop

print("__________")
print("Print the first 10 natural numbers using for loop")
print("__________")

givenNumber1= int(input("What's the limit?: "))
for i in range (0, givenNumber1):
    print(i)

print("__________")

#Print even number till given number

print("Print even number till given number")
print("__________")

givenNumber2= int(input("What's the limit?: "))
for i in range (0, givenNumber2, 2):
    print(i)

print("__________")

#Calculate the sum of all numbers from 1 to given number

print("Calculate the sum of all numbers from 1 to given number")
print("__________")

sum=0
givenNumber3= int(input("What's the limit?: "))
for i in range (1, givenNumber3 + 1):
    sum+=i
    print (sum)

print("__________")

#Python program to print a multiplication table of a given number

print("Python program to print a multiplication table of a given number")
print("__________")

givenNumber4= int(input("What's the number you need for multiplication table?: "))
multiply1= int(input("What's the limit of the multiplication?: "))
for i in range (multiply1):
    print(givenNumber4, "x", i, "= ", i*multiply1)

print("__________")

#Python program to display numbers from a list using a for loop.

print("Python program to display numbers from a list using a for loop.")
print("__________")

list1= [1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i)

print("__________")







