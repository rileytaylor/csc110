# Allison Obourn and Janalee O'Bagy
# CSc 110, Spring 2017
# Lecture 9

# This program prompts two people for their CS1 and CS2 grades
# computes their CS GPA and whether or not that GPA is
# high enough (so far) to be a CS major.

def main():
    intro()

    gpa1 = get_person_info()
    gpa2 = get_person_info()

    results(gpa1, 1)
    results(gpa2, 2)

# prints out an introduction explaining what the program does
def intro():
    print("This program reads data for two students and")
    print("computes their Computer Science GPAs")
    print()

# Takes a GPA (float) and person number (int) as parameters
# and outputs the person's GPA as well as whether or not the
# GPA is high enough to potentially be a CS major
def results(gpa, person):
    print("Person " + str(person) + " GPA = " + str(gpa))
    if(gpa >= 2.5):
        print("accepted")
    else:
        print("not accepted")

# prompts the user for a 110 grade and a 120 grade.
# Assumes those grades will be capital single letters
# Returns the average GPA of those two grades as a float
def get_person_info():
    print("Enter next person's information:")
    grade110 = input("CS 110 grade? ")
    grade120 = input("CS 120 grade? ")
    print()

    gpa110 = grade_to_gpa(grade110) 
    gpa120 = grade_to_gpa(grade120)

    return (gpa110 + gpa120) / 2

# takes a string letter grade as a parameter and returns
# that grade converted to a GPA value (float). Assumes grade
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
