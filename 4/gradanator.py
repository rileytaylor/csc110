# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Gradanator
#
# This calculates a students grade based on their input of scores from
# their two midterms, final, and homework assignments.

MAX_SCORE = 100
ATTENDANCE_MAX = 34


def main():
    intro()
    midterm_1 = midterm_one()
    midterm_2 = midterm_two()
    final_score = final()
    homework_score = homework()
    total(midterm_1, midterm_2, final_score, homework_score)


# --------------------------------------------------------------------
# intro() simply provides the introductory text to let the user know
# what this program does.
# --------------------------------------------------------------------
def intro():
    print("This program reads exam/homework scores")
    print("and reports your overall course grade.")
    print("")


# --------------------------------------------------------------------
# get_total_points() calculates the total score by adding the raw
# input grade and the shift (if any) together.
#
# PARAMETERS: score -- an int. The raw score.
#             shift -- an int. The shift.
# --------------------------------------------------------------------
def get_total_points(score, shift):
    total = int(score) + int(shift)
    if (total > MAX_SCORE):
        total = MAX_SCORE
    return total


# --------------------------------------------------------------------
# get_weighted_score() calculates the weighted score.
#
# PARAMETERS: score -- an int. The raw score.
#             total -- an int. The total possible points.
#             weight -- an int. The weight given.
# --------------------------------------------------------------------
def get_weighted_score(score, total, weight):
    weighted_score = round(int(score) / total * int(weight), 1)
    return weighted_score


# --------------------------------------------------------------------
# test_input() gets user input and calculates the weighted score of
# the test.
#
# PARAMETERS: name -- a string. The test name.
# --------------------------------------------------------------------
def test_input(name):
    print(name + ":")
    weight = input("Weight (0-100)? ")
    score = input("Score earned? ")
    shifted = input("Were scores shifted (1=yes, 2=no)? ")
    if (shifted == "1"):
        shift_amount = input("Shift amount? ")
    else:
        shift_amount = 0
    total_points = get_total_points(score, shift_amount)
    print("Total points = " + str(total_points) + " / 100")
    weighted_score = get_weighted_score(total_points, 100, weight)
    print("Weighted score = " + str(weighted_score) + " / " + str(weight))
    print()
    return weighted_score


# --------------------------------------------------------------------
# get_grade_letter() matches the final grade with a grade letter.
#
# PARAMETERS: grade -- an int. The grade to be matched.
# --------------------------------------------------------------------
def get_grade_letter(grade):
    if (grade >= 90):
        return "A"
    elif (grade >= 80):
        return "B"
    elif (grade >= 70):
        return "C"
    elif (grade >= 60):
        return "D"
    else:
        return "F"


# --------------------------------------------------------------------
# midterm_one() prompts the user for input and then calculates the
# score for midterm one, inluding the weight and shift (if any)
# --------------------------------------------------------------------
def midterm_one():
    weighted_score = test_input("Midterm 1")
    return weighted_score


# --------------------------------------------------------------------
# midterm_two() prompts the user for input and then calculates the
# score for midterm one, inluding the weight and shift (if any)
# --------------------------------------------------------------------
def midterm_two():
    weighted_score = test_input("Midterm 2")
    return weighted_score


# --------------------------------------------------------------------
# final() prompts the user for input and then calculates the
# score for the final, inluding the weight and shift (if any)
# --------------------------------------------------------------------
def final():
    weighted_score = test_input("Final")
    return weighted_score


# --------------------------------------------------------------------
# homework() prompts the user for input and then calculates the
# score for all homework and section attendance, inluding the weight
# and shift (if any)
# --------------------------------------------------------------------
def homework():
    score_total = 0
    score_max = 0
    loop = 0

    print("Homework:")
    weight = input("Weight (0-100)? ")
    count = input("Number of assignments? ")
    for assignment in range(1, int(count) + 1):
        loop += 1
        score_total += int(input("Assignment " + str(loop) + " score? "))
        score_max += int(input("Assignment " + str(loop) + " max? "))
    attendance = int(input("How many sections did you attend? ")) * 3
    if (attendance > ATTENDANCE_MAX):
        attendance = ATTENDANCE_MAX
    print("Section points = " + str(attendance) + " / " + str(ATTENDANCE_MAX))
    score_total += attendance
    score_max += ATTENDANCE_MAX
    weighted_score = get_weighted_score(score_total, score_max, weight)
    print("Total points = " + str(score_total) + " / " + str(score_max))
    print("Weighted score = " + str(weighted_score) + " / " + str(weight))
    print()
    return weighted_score


# --------------------------------------------------------------------
# total() calculates the overall score and letter grade.
# --------------------------------------------------------------------
def total(midterm_1, midterm_2, final, homework):
    grade = round(midterm_1 + midterm_2 + final + homework, 1)
    print("Overall percentage = " + str(grade))
    letter = get_grade_letter(grade)
    print("Your grade will be at least: " + str(letter))
    print("Don't Panic.")

main()
