#StartCode

while True: 
 print("Welcome to Grade Calculator!")
 print("Grade Calculator is made by Md Affan. This software is used to find the grades of your subjects!")
 print("Please follow the instructions below to continue.")

#Confirm

 start= input("Start? (yes/no): ")
 if start == "yes":
  pass
 elif start == "no":
  break
 else:
   print("Invalid Input, please try again!")
   continue
 while True:
  choice= input("Would you like to know the avg or single subject? (avg/ss): ")

  #SS

  if choice == "ss":
   sub= str(input("Subject: "))
   mark= float(input("Enter your marks for " + sub + ": "))
   if mark>=90:
    print("Your", sub, "Grade is: A+")
    break
   elif mark>=80 and mark<=90:
    print("Your", sub, "Grade is: A")
    break
   elif mark>=70 and mark<=80:
    print("Your", sub, "Grade is: B")
    break
   elif mark>=60 and mark<=70:
    print("Your", sub, "Grade is: C")
    break
   elif mark>=50 and mark<=60:
    print("Your", sub, "Grade is: D")
    break
   else:
    print("Your", sub, "Grade is: F")
    break
    

  #AVG

  elif choice == "avg":
    choice2= float(input("How many subjects would you like to know the avg for? (2, 3, 4, 5): "))
  #Choice 2
    if choice2 == 2:
     subject1= str (input("Subject 1: "))
     marks1= float (input("Enter your marks for " + subject1 + ": "))
     subject2= str (input("Subject 2: "))
     marks2= float(input("Enter your marks for " + subject2 + ": "))
  
     grading1= marks1+marks2
     avg1= grading1/2
     print(subject1, "& ", subject2, ": ", avg1)
     if avg1>=90:
      print("Your Average Grade is: A+")
     elif avg1>=80 and avg1<=90:
      print("Your Average Grade is: A")
     elif avg1>=70 and avg1<=80:
      print("Your Average Grade is: B")
     elif avg1>=60 and avg1<=70:
      print("Your Average Grade is: C")
     elif avg1>=50 and avg1<=60:
      print("Your Average Grade is: D")
     else:
      print("Your Average Grade is: F")
    

  #Choice 3

    elif choice2 == 3:
     subject3= str(input("Subject 1: "))
     marks3= float(input("Enter your marks for " + subject3 + ": "))
     subject4= str(input("Subject 2: "))
     marks4= float(input("Enter your marks for " + subject4 + ": "))
     subject5= str(input("Subject 3: "))
     marks5= float(input("Enter your marks for " + subject5 + ": "))

     grading2= marks3+marks4+marks5
     avg2= grading2/3
     print(subject3, "& ", subject4, "& ", subject5, ": ", avg2)
     if avg2>=90:
      print("Your Average Grade is: A+")
     elif avg2>=80 and avg2<=90:
      print("Your Average Grade is: A")
     elif avg2>=70 and avg2<=80:
      print("Your Average Grade is: B")
     elif avg2>=60 and avg2<=70:
      print("Your Average Grade is: C")
     elif avg2>=50 and avg2<=60:
      print("Your Average Grade is: D")
     else:
      print("Your Average Grade is: F")
   
  #Choice 4 

    elif choice2 == 4:
     subject6= str(input("Subject 1: "))
     marks6= float(input("Enter your marks for " + subject6 + ": "))
     subject7= str(input("Subject 2: "))
     marks7= float(input("Enter your marks for " + subject7 + ": "))
     subject8= str(input("Subject 3: "))
     marks8= float(input("Enter your marks for " + subject8 + ": "))
     subject9= str(input("Subject 9: "))
     marks9= float(input("Enter you marks for " + subject9 + ": " ))

     grading3= marks6+marks7+marks8+marks9
     avg3= grading3/4
     print(subject6, "&", subject7, "&", subject8, "&", subject9, ": ", avg3)
     if avg3>=90:
      print("Your Average Grade is: A+")
     elif avg3>=80 and avg3<=90:
      print("Your Average Grade is: A")
     elif avg3>=70 and avg3<=80:
      print("Your Average Grade is: B")
     elif avg3>=60 and avg3<=70:
      print("Your Average Grade is: C")
     elif avg3>=50 and avg3<=60:
      print("Your Average Grade is: D")
     else:
      print("Your Average Grade is: F")

  #Choice 5 

    elif choice2 == 5:
     subject10= str(input("Subject 1: "))
     marks10= float(input("Enter your marks for " + subject10 + ":"))
     subject11= str(input("Subject 2: "))
     marks11= float(input("Enter your marks for " + subject11 + ":"))
     subject12= str(input("Subject 3: "))
     marks12= float(input("Enter your marks for " + subject12 + ":"))
     subject13= str(input("Subject 1: "))
     marks13= float(input("Enter your marks for " + subject13 + ":"))
     subject14= str(input("Subject 2: "))
     marks14= float(input("Enter your marks for " + subject14 + ":"))

     grading4= marks10+marks11+marks12+marks13+marks14
     avg4= grading4/5
     print(subject10, "&", subject11, "&", subject12, "&", subject13, "&", subject14, ": ", avg4)
     if avg4>=90:
      print("Your Average Grade is: A+")
     if avg4>=80 and avg4<=90:
      print("Your Average Grade is: A")
     if avg4>=70 and avg4<=80:
      print("Your Average Grade is: B")
     if avg4>=60 and avg4<=70:
      print("Your Average Grade is: C")
     if avg4>=50 and avg4<=60:
      print("Your Average Grade is: D")
     else:
      print("Your Average Grade is: F")
    else:
     print("Invalid Input, please try again! ")
   

 cont= input("Would you like to continue? (yes/no): ")
 if cont == "yes":
    continue
 elif cont == "no":
    print("Alright, thanks for using our tool, please come back again!")
    break
 else:
    print("Invalid Input")
    continue
 
 
  
  

    
     



    