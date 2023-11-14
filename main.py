# Student Grade Calculator

# function to calculate GPA
def calculate_gpa(grades, credits):
    total_credits = sum(credits)
    weighted_sum = 0
    for i in range(len(grades)):
        weighted_sum += grades[i] * credits[i]
    gpa = weighted_sum / total_credits
    return gpa

# function to calculate letter grade
def calculate_letter_grade(gpa):
    if gpa >= 90:
        return "A"
    elif gpa >= 80:
        return "B"
    elif gpa >= 70:
        return "C"
    elif gpa >= 60:
        return "D"
    else:
        return "F"

# main function
def main():
    num_courses = int(input("Enter the number of courses: "))
    grades = []
    credits = []
    for i in range(num_courses):
        grade = float(input("Enter the grade for course " + str(i+1) + ": "))
        credit = int(input("Enter the credit hours for course " + str(i+1) + ": "))
        grades.append(grade)
        credits.append(credit)
    gpa = calculate_gpa(grades, credits)
    letter_grade = calculate_letter_grade(gpa)
    print("Your GPA is", round(gpa, 2))
    print("Your letter grade is", letter_grade)

# calling main function
main()
