#Start Code

print ("What is your name?") 
username= input ("Username: ")
print ("Alright, Sir/Maam", username )

#About
while True:
 print ("This is a code/program made by MD Affan, a senior python developer, to find the hypotenuse of a right-angled triangle, also known as the Pythagorean Theorem method") 
 print ("Please do not add anything else other than numbers in the calculation!")
 start= input ("Would you like to start? (yes/no) : ")
 if start == "yes":
    pass
 elif start == "no":
    break
 else:
    print('Invalid Input, please try again!')
    
 #calculation   
 a = float(input("Give side a: "))
 b = float(input("Give side b: "))
 c = (a ** 2 + b ** 2) 
 hypo= c ** (1/2)
 print (f"The length of the hypotenuse C is {hypo}")

 #next_calculation
 next_calc= input ("Continue to your next calculation? (yes/no): ")
 if next_calc == "yes":
    continue
 elif next_calc == "no":
    pass
    print("All your calculations are: ", a, " ** 2 +", b, " ** 2 = ", hypo)
    break
 else:
    pass
    print ("Invalid Input, please try again!")
    continue
 
