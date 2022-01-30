# This is a debugging exercise 
# James Atkins
# CTI-110 P3HW1
# 10-09-2021

# This program takes a number grade and outputs a letter grade.
# system uses 10-point grading scale
def main():    
    max_score = 100
    a_grade = 90
    b_grade = 80
    c_grade = 70
    d_grade = 60
    f_grade = 0
    
    score = int(input('Enter grade: '))

    if ((score >= a_grade) and (score <= max_score)):
        print('Your grade is: A')
    elif ((score >= b_grade) and (score < a_grade)):
        print('Your grade is: B')
    elif ((score >= c_grade) and (score < b_grade)):
        print('Your grade is: C')
    elif ((score >= d_grade) and (score < c_grade)):
        print('Your grade is: D')
    elif ((score <= d_grade) and (score >= f_grade)):
        print('Your grade is: F')
    else:
        print('That is not a valid score.')

# program start
main()
