import sys

def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

def placement_eligibility(avg_marks):
    if avg_marks >= 75:
        return "Eligible for Placement"
    elif avg_marks >= 60:
        return "Eligible for Internship"
    else:
        return "Not Eligible"

if __name__ == "__main__":

    script_name = sys.argv[0]

    if len(sys.argv) > 3:
        student_name = sys.argv[1]
        department = sys.argv[2]
        marks = list(map(int, sys.argv[3:]))
        print("User provided student details:")
    else:
        student_name = "Shreya"
        department = "Computer Science"
        marks = [70, 75, 80, 85]
        print("No input given - using default values:")

    total_subjects = len(marks)
    average_marks = calculate_average(marks)
    status = placement_eligibility(average_marks)

    print("\n========== Student Placement Details ==========")
    print("Script Name:", script_name)
    print("Student Name:", student_name)
    print("Department:", department)
    print("Marks:", marks)
    print("Total Subjects:", total_subjects)
    print("Average Marks:", average_marks)
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))
    print("Placement Status:", status)