# Allison Obourn and Janalee O'Bagy
# CSc 110, Spring 2017
# Lecture 8

# This program prompts two people for their CS1 and CS2 grades
# computes their CS GPA and whether or not those grades are
# high enough to get into the CS department.

# WARNING: This program is not finished and so does not work
#          properly and is NOT a good example of stlye and commenting

'''
This program reads data for two students and
computes their Computer Science GPAs

Enter next person's information:
CS 110 grade? A
CS 120 grade? B

Enter next person's information:
CS 110 grade? B
CS 120 grade? B

Person 1 GPA = 3.5
accepted
Person 2 GPA = 3.0
accepted
Difference = 0.5
'''

def main():
    print("This program reads data for two students and")
    print("computes their Computer Science GPAs")
    print()

    print("Enter next person's information:")
    grade110 = input("CS 110 grade? ")
    grade120 = input("CS 120 grade? ")

    gpa = grade_to_gpa(grade110)


    gpa2 = "A"
    if(grade120 == "A"):
        gpa2 = 4.0
    elif(grade120 == "B"):
        gpa2 = 3.0
    elif(grade120 == "C"):
        gpa2 = 2.0
    elif(grade120 == "D"):
        gpa2 = 1.0
    else:
        gpa2 = 0.0

    print("Person 1 GPA = " + str((gpa + gpa2) / 2))

# takes a letter grade as a parameter and returns
# that grade converted to a GPA value. Assumes grade
# will be an uppercase letter. 
def grade_to_gpa(grade110):
    gpa = "A"
    if(grade110 == "A"):
        gpa = 4.0
    elif(grade110 == "B"):
        gpa = 3.0
    elif(grade110 == "C"):
        gpa = 2.0
    elif(grade110 == "D"):
        gpa = 1.0
    else:
        gpa = 0.0
    return gpa
    
main()








