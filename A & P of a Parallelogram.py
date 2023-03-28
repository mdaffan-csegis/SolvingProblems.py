#Start Code
print ("What is your name?") 
username= input ("Username: ")
print ("Alright, Sir/Maam", username )
#About
print ("This is a code/program made by MD Affan, a senior python developer, to find the area and perimetre of a parallelogram") 
print ("Please do not add anything else other than numbers in the calculation!")
input ("Would you like to continue?: ")
Yes= True
No= False
#Area
print ("AREA AND PERIMETRE OF A PARALLELOGRAM")
num1= input ("Height= ") 
num2= input ("Length= ")
area= int (num1) * int (num2)
print ("Area= ", num1, "X", num2, ":", area)
#Permimetre
num5= 2
perimetre= int (num1) + int (num2) 
peri= perimetre * num5
print ("Perimetre= ", num1, "+", num2, "X 2: ", peri)
rating= input ("How would you rate Affan's Area and Permimetre of a Parallelogram Calculator?: ")
print ("Thank You For Your Rating! ", rating )