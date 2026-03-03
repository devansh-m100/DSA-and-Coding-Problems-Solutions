# write your solution here
student_information_file_name = input("Student information: ")
exercises_completed_file_name = input("Exercises completed: ")
exam_points_file_name = input("Exam Points: ")
course_file_name = input("Course file name: ")

student_id_to_name = {}
with open(student_information_file_name) as student_information:
    for line in student_information:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        student_id_to_name[parts[0]] = f"{parts[1]} {parts[2].replace("\n", "")}"

student_id_to_exercise_points = {}
student_id_to_exercise_nbr = {}
with open(exercises_completed_file_name) as exercises_information:
    for line in exercises_information:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        
        curr_stu_exercise_completed = 0

        for i in range(1, 8):
            curr_stu_exercise_completed += int(parts[i])
        student_id_to_exercise_nbr[parts[0]] = curr_stu_exercise_completed
        percentage_completed = (curr_stu_exercise_completed / 40) * 100
        if 10 <= percentage_completed < 20:
            student_id_to_exercise_points[parts[0]] = 1
        elif 20 <= percentage_completed < 30:
            student_id_to_exercise_points[parts[0]] = 2
        elif 30 <= percentage_completed < 40:
            student_id_to_exercise_points[parts[0]] = 3
        elif 40 <= percentage_completed < 50:
            student_id_to_exercise_points[parts[0]] = 4
        elif 50 <= percentage_completed < 60:   
            student_id_to_exercise_points[parts[0]] = 5
        elif 60 <= percentage_completed < 70:
            student_id_to_exercise_points[parts[0]] = 6
        elif 70 <= percentage_completed < 80:
            student_id_to_exercise_points[parts[0]] = 7
        elif 80 <= percentage_completed < 90:
            student_id_to_exercise_points[parts[0]] = 8
        elif 90 <= percentage_completed < 100:
            student_id_to_exercise_points[parts[0]] = 9
        elif percentage_completed == 100:
            student_id_to_exercise_points[parts[0]] = 10
        else:
            student_id_to_exercise_points[parts[0]] = 0

student_id_to_exam_points = {}
with open(exam_points_file_name) as exam_points_info:
    for line in exam_points_info:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        student_id_to_exam_points[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3])

for id, name in student_id_to_name.items():

    total_points = student_id_to_exam_points[id] + student_id_to_exercise_points[id]

    grade = 0

    if 0 <= total_points <= 14:
        grade = 0
    elif 15 <= total_points <= 17:
        grade = 1
    elif 18 <= total_points <= 20:
        grade = 2
    elif 21 <= total_points <= 23:
        grade = 3
    elif 24 <= total_points <= 27:
        grade = 4
    elif 28 <= total_points:
        grade = 5

    print(f"{student_id_to_name[id]:30}{student_id_to_exercise_nbr[id]:<10}{student_id_to_exercise_points[id]:<10}{student_id_to_exam_points[id]:<10}{total_points:<10}{grade:<10}")

with open("results.txt", "w") as results_txt, open("results.csv", "w") as results_csv, open(course_file_name) as course_file:

    course_name_and_credits = []
    for line in course_file:
        parts = line.split(": ")
        course_name_and_credits.append(parts[1].strip())

    header_line = f"{course_name_and_credits[0]}, {course_name_and_credits[1]} credits\n"
    results_txt.write(header_line)
    results_txt.write("=" * (len(header_line) - 1) + "\n")

    results_txt.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n")

    for id, name in student_id_to_name.items():
        total_points = student_id_to_exam_points[id] + student_id_to_exercise_points[id]
        grade = 0
        if 0 <= total_points <= 14:
            grade = 0
        elif 15 <= total_points <= 17:
            grade = 1
        elif 18 <= total_points <= 20:
            grade = 2
        elif 21 <= total_points <= 23:
            grade = 3
        elif 24 <= total_points <= 27:
            grade = 4
        elif 28 <= total_points:
            grade = 5

        results_txt.write(f"{student_id_to_name[id]:30}{student_id_to_exercise_nbr[id]:<10}{student_id_to_exercise_points[id]:<10}{student_id_to_exam_points[id]:<10}{total_points:<10}{grade:<10}\n")

        results_csv.write(f"{student_id_to_name[id]};{grade}\n")
