# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output = 3
print(b) #output = 4
print(a == b) #output false

print(a == b)   #checks for equaliity (False)
print(a != b)   #This checks if its not equal (True)
print(a > b)    #This one checks for greater than (False)
print(a < b)    #This one checks for less than (True)
print(a >= b)   #This one checks for greater than or equal to (False)
print(a <= b)   #This one checks for less than or equal to (True)


#predict the output of the following comparisons:
10 > 5 #output true
7 == 2 * 3 + 1 #output true
8 != 8 #output false
4 <= 2 + 2 #output true

# Write 3 examples that result in True and 3 that result in False.
9 > 3 #output true
8 == 8 #output true
2 <= 3 #output true
7 != 7 #output false
3 + 3 >= 7 #output false
7 < 4 #output false

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

#asking student for their score
score = int(input("What is your score?"))
#make the scoring for all grading spectrums
#If the score is between 90--100, you got an A
if score >= 90 and score <= 100:
    print("You got an A")
#If the score is between 80--89, you got a B
elif score >= 80 and score <= 89:
    print("You got a B")
#If the score is between 70--79, you got a C 
elif score >= 70 and score <= 79:
    print("You got a C")
#If the score is between 60--69, you got a D
elif score >= 60 and score <= 69:
    print("You got a D")
# else you failed 
else:
    print("You didn't pass the test.")




    
#ask for a password
password= int(input("What is your password?"))
print(password)