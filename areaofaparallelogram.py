#Start Code
print ("What is your name?") 
username= input ("Username: ") 
print ("Okay,", username )
#About
print ("This is a sofware made by MD Affan, a senior python developer, to find the area and perimetre of a parallelogram") 
input ("Would you like to continue?: ")
Yes= True
No= False
#Area
print ("AREA OF THE PARALLELOGRAM")
num1= input ("Height= ") 
num2= input ("Length= ")
area= int (num1) * int (num2)
print ("Area= ", num1, "X", num2, ":", area)
#Perimetre
print ("PERIMETRE OF A PARALLELOGRAM")
num3= input ("Height= ")
num4= input ("Length= ")
num5= 2
perimetre= int (num3) + int (num4) 
peri= perimetre * num5
print ("Perimetre= ", num3, "+", num4, "X 2: ", peri)
rating= input ("How would you rate Affan's Area Calculator?: ")
print ("Thank You For Your Rating! ", rating )
print ("Your calculations are: ")
print ("Area= ", num1, "X", num2, ":", area )
print ("Perimetre= ", num3, "+", num4, "X 2: ", peri)