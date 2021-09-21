#Laboratory_Activity_No_2_Emerging-Tech
# Author: Jeny Biscocho
#	  John Michael Cabral

print("Computation of Student Average Grade Program")
print("")
print("Enter Student Grades")
Prelim = float(input("Prelims: "))
Midterm = float(input("Midterms: "))
Semifinal = float(input("Semifinals: "))
Final = float(input("Finals: "))

sum = Prelim + Midterm + Semifinal + Final
avg = sum/4

if avg>=99 and avg<=100:
    print("Your Average is {} " .format(avg) + "you PASSED and your grade is A. Superb!")
elif avg>=90 and avg<98:
    print("Your Average is {} " .format(avg) + "you PASSED and your grade is B. Excellent!")
elif avg>=80 and avg<89:
    print("Your Average is {} " .format(avg) + "you PASSED and your grade is C. Very Good!")
elif avg>=75 and avg<79:
    print("Your Average is {} " .format(avg) + "you PASSED and your grade is D. Good!")
elif avg>=70 and avg<74:
    print("Your Average is {} " .format(avg) + "you FAILED and your grade is D. Focus and you can Pass!")
elif avg>=61 and avg<69:
    print("Your Average is {} " .format(avg) + "you FAILED and your grade is E. More focus on the study!")
elif avg<60:
    print("Your Average is {} " .format(avg) + "you FAILED and your grade is F. You need to prioritize you studies!")
else:
    print("You had entered an invalid value. Please Try Again!")
