# Write your solution here
def add_student(students: dict, name: str):
    students[name] = []

def add_course(students: dict, name: str, course_info: tuple):
    if course_info[1] != 0:
        course_present = False
        for i, course_and_grade in enumerate(students[name]):
            if course_and_grade[0] == course_info[0]:
                course_present = True
                if course_and_grade[1] < course_info[1]:
                    students[name][i] = (course_and_grade[0], course_info[1])
        if not course_present:
            students[name].append(course_info)
    
def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        if not students[name]:
            print(f"{name}:")
            print(" no completed courses")
        else:
            print(f"{name}:")
            print(f" {len(students[name])} completed courses:")
            grade_sum = 0
            course_count = 0
            for course_info in students[name]:
                grade_sum += course_info[1]
                course_count += 1
                print(f"  {course_info[0]} {course_info[1]}")
            print(f" average grade {grade_sum / course_count}")

def summary(students: dict):
    print(f"students {len(students)}")
    most_courses_completed_count = 0
    most_courses_completed_student_name = ""
    best_avg_grade = 0
    best_avg_grade_student_name = ""
    for student_name, courses in students.items():
        if len(courses) > most_courses_completed_count:
            most_courses_completed_count = len(courses)
            most_courses_completed_student_name = student_name
        student_course_grade_sum = 0
        for i in range(len(courses)):
            student_course_grade_sum += courses[i][1]
        student_courses_avg_grade = student_course_grade_sum / len(courses)
        if student_courses_avg_grade > best_avg_grade:
            best_avg_grade = student_courses_avg_grade
            best_avg_grade_student_name = student_name

    print(f"most courses completed {most_courses_completed_count} {most_courses_completed_student_name}")
    print(f"best average grade {best_avg_grade:.1f} {best_avg_grade_student_name}")



