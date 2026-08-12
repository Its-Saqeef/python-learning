import csv
from pathlib import Path

from constant_data import features, student_headers, student_management, marks_management,calculations,class_analysis

STUDENTS_FILE = Path(__file__).with_name("students.csv")


def load_students():
    if not STUDENTS_FILE.exists():
        return []

    with STUDENTS_FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def get_dynamic_headers(students_data):
    existing_headers = []
    if STUDENTS_FILE.exists():
        with STUDENTS_FILE.open("r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            existing_headers = next(reader, [])

    subject_headers = sorted({
        key
        for student in students_data
        for key in student.keys()
        if key not in student_headers
    })

    combined_headers = list(dict.fromkeys(existing_headers + student_headers + subject_headers))
    return combined_headers


def save_students(students):
    fieldnames = get_dynamic_headers(students)

    with STUDENTS_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for student in students:
            row = {field: student.get(field, "") for field in fieldnames}
            writer.writerow(row)


students = load_students()


def add_student(name, rollno, age):
    student = {
        "Name": name,
        "Roll No": str(rollno),
        "Age": str(age),
    }
    students.append(student)
    save_students(students)
    print("Student Added Successfully")


def delete_student(rollno):
    global students
    students = [student for student in students if student["Roll No"] != str(rollno)]
    save_students(students)
    print("Student deleted successfully")

def get_student(rollno):
    for student in students:
        if student["Roll No"] == str(rollno):
            return student

def get_all_students():
    for student in students:
        print(student["Name"])


def update_student(rollno, **kwargs):
    global students

    student = get_student(rollno)
    if not student:
        return False

    for key, value in kwargs.items():
        student[key] = value

    save_students(students)
    return True

def add_marks(rollno, marks_dict):
    student = get_student(rollno)
    if not student:
        print("Student with such roll number does not exist..!")
        return False

    if not isinstance(marks_dict, dict):
        print("Marks must be provided as a dictionary")
        return False

    for subject, marks in marks_dict.items():
        try:
            marks_value = int(marks)
        except (ValueError, TypeError):
            print(f"Invalid marks for {subject}. Marks must be a number between 1 and 100.")
            continue

        if not 1 <= marks_value <= 100:
            print(f"Marks for {subject} must be between 1 and 100.")
            continue

        student[subject] = str(marks_value)

    save_students(students)
    print(f"Marks added successfully for student {student['Name']}")
    return True



def calculate_obtained_marks(rollno):
    student = get_student(rollno)
    if not student:
        print("Student with such roll number does not exist..!")
        return None

    obtained_marks = sum(int(marks) for subject, marks in student.items() if subject not in student_headers)
    return obtained_marks




def main():
    while True:
        print("Welcome To Student Marks Analyzer\n")
        print("\nPlease select one of the following")
        for index, feature in enumerate(features):
            print(f"{index + 1}. {feature}")

        choice = input("Enter Choice : ")

        if choice == "1":
            print("Student Management\n")
            for index, action in enumerate(student_management):
                print(f"{index + 1}. {action}")

            student_operation = input("Enter choice : ")

            match student_operation:
                case "1":
                    name = input("Enter name : ")
                    roll_no = input("Enter roll No : ")
                    age = input("Enter age : ")
                    add_student(name=name, rollno=roll_no, age=age)
                case "2":
                    roll_no = input("Enter roll No : ")
                    student = get_student(roll_no)
                    if not student:
                        print("Student with such roll number does not exist..!")
                    else:
                        print("\nUpdate student details")
                        print("Leave a field blank to keep the current value")

                        updates = {}
                        new_name = input(f"Enter new name [{student['Name']}]: ").strip()
                        if new_name:
                            updates["Name"] = new_name

                        new_age = input(f"Enter new age [{student['Age']}]: ").strip()
                        if new_age:
                            updates["Age"] = new_age

                        if updates:
                            if update_student(roll_no, **updates):
                                print("Student updated successfully")
                        else:
                            print("No changes were made")
                case "3":
                    roll_no = input("Enter roll No : ")
                    delete_student(roll_no)
                case "4":
                    roll_no = input("Enter roll No : ")
                    student = get_student(roll_no)
                    if not student:
                        print("Student with such roll number does not exist..!")
                    else:
                        print(f"Name: {student['Name']}, Roll No: {student['Roll No']}, Age: {student['Age']}")
                case "5":
                    print("All Students:")
                    get_all_students()
                case "6":
                    print("Going back to main menu")
                case _:
                    print("Invalid choice")

            print("\nReturning to main menu...\n")
            continue
        
        if choice == "2":
            print("Marks Management selected")

            for i, option in enumerate(marks_management, start=1):
                print(f"{i}. {option}")

            marks_operation = input("Enter choice : ")

            match marks_operation:
                case "1":
                    roll_no = input("Enter roll No : ")
                    student = get_student(roll_no)
                    if not student:
                        print("Student with such roll number does not exist..!")
                    else:
                        marks_data = {}
                        subject_count = int(input("How many subjects do you want to add? "))

                        for _ in range(subject_count):
                            subject = input("Enter subject name : ").strip()
                            while True:
                                try:
                                    marks = int(input(f"Enter marks for {subject} (1-100): "))
                                except ValueError:
                                    print("Marks must be a number")
                                    continue

                                if 1 <= marks <= 100:
                                    marks_data[subject] = marks
                                    break
                                print("Marks must be between 1 and 100")

                        add_marks(roll_no, marks_data)
                case "2":
                    roll_no = input("Enter roll No : ")
                    student = get_student(roll_no)
                    if not student:
                        print("Student with such roll number does not exist..!")
                        continue
                    subject = input("Enter subject name : ").strip()
                    if subject not in student:
                        print(f"Subject {subject} does not exist for this student.")
                        continue
                    marks = input(f"Enter new marks for {subject} (1-100): ")
                    student[subject] = marks
                    save_students(students)
                case "3":
                    roll_no = input("Enter roll No : ")
                    student = get_student(roll_no)
                    if not student:
                        print("Student with such roll number does not exist..!")
                        continue
                    subject = input("Enter subject name : ").strip()
                    if subject not in student:
                        print(f"Subject {subject} does not exist for this student.")
                        continue
                    del student[subject]
                    save_students(students)
                case "4":
                    roll_no = input("Enter roll No : ")
                    student = get_student(roll_no)
                    if not student:
                        print("Student with such roll number does not exist..!")
                        continue
                    for subject, marks in student.items():
                        print(f"{subject}: {marks}")
                case "5":
                    for student in students:
                        print(f"Name: {student['Name']}, Roll No: {student['Roll No']}, Age: {student['Age']}")
                        for subject, marks in student.items():
                            if subject not in student_headers:
                                print(f"  {subject}: {marks}")
                case "6":
                    print("Going back to main menu")
                case _:
                    print("Invalid choice")
            continue
        
        if choice == "3":
            print("Perform Calculations")

            for i, option in enumerate(calculations, start=1):
                print(f"{i}. {option}")
            calc_operation = input("Enter choice : ")
            match calc_operation:
                case "1":
                    roll_no = input("Enter roll No : ")
                    obtained_marks = calculate_obtained_marks(roll_no)
                    if obtained_marks is not None:
                        print(f"Total Obtained Marks for Roll No {roll_no}: {obtained_marks}")
                case "2":
                    roll_no = input("Enter roll No : ")
                    student = get_student(roll_no)
                    if not student:
                        print("Student with such roll number does not exist..!")
                        continue
                    total_subjects = len([key for key in student.keys() if key not in student_headers])
                    if total_subjects == 0:
                        print("No subjects found for this student.")
                        continue
                    obtained_marks = calculate_obtained_marks(roll_no)
                    percentage = (obtained_marks / (total_subjects * 100)) * 100
                    print(f"Percentage for Roll No {roll_no}: {percentage:.2f}%")
                    status = "Pass" if percentage >= 50 else "Fail"
                    print(f"Status for Roll No {roll_no}: {status}")
                case "3":
                    roll_no = input("Enter roll No : ")
                    student = get_student(roll_no)
                    if not student:
                        print("Student with such roll number does not exist..!")
                        continue
                    obtained_marks = calculate_obtained_marks(roll_no)
                    total_subjects = len([key for key in student.keys() if key not in student_headers])
                    if total_subjects == 0:
                        print("No subjects found for this student.")
                        continue
                    percentage = (obtained_marks / (total_subjects * 100)) * 100
                    grade = "A" if percentage >= 90 else "B" if percentage >= 75 else "C" if percentage >= 60 else "D" if percentage >= 50 else "F"
                    print(f"Grade for Roll No {roll_no}: {grade}")
                case "4":
                    print("Going back to main menu")
                case _:
                    print("Invalid choice")
            continue

        if choice == "4":
            print("Class Analysis selected")
            for i, option in enumerate(class_analysis, start=1):
                print(f"{i}. {option}")
            analysis_operation = input("Enter choice : ")
            match analysis_operation:
                case "1":
                    if not students:
                        print("No students found.")
                        continue
                    total_marks_list = [calculate_obtained_marks(student["Roll No"]) for student in students]
                    class_average = sum(total_marks_list) / len(total_marks_list)
                    print(f"Class Average: {class_average:.2f}")
                case "2":
                    if not students:
                        print("No students found.")
                        continue
                    highest_scorer = max(students, key=lambda student: calculate_obtained_marks(student["Roll No"]))
                    print(f"Highest Scorer: {highest_scorer['Name']} with Roll No {highest_scorer['Roll No']} and Marks {calculate_obtained_marks(highest_scorer['Roll No'])}")
                case "3":
                    if not students:
                        print("No students found.")
                        continue
                    ranked_students = sorted(students, key=lambda student: calculate_obtained_marks(student["Roll No"]), reverse=True)
                    print("Overall Rank List:")
                    for i, student in enumerate(ranked_students, start=1):
                        print(f"{i}. {student['Name']} - Roll No: {student['Roll No']} - Marks: {calculate_obtained_marks(student['Roll No'])}")
                case "4":
                    subject = input("Enter subject name to find topper: ").strip()
                    subject_scores = [(student, int(student.get(subject, 0))) for student in students if subject in student]
                    if not subject_scores:
                        print(f"No scores found for subject {subject}.")
                        continue
                    subject_topper = max(subject_scores, key=lambda x: x[1])
                    print(f"Subject Topper for {subject}: {subject_topper[0]['Name']} with Roll No {subject_topper[0]['Roll No']} and Marks {subject_topper[1]}")
                case "5":
                    pass_count = sum(1 for student in students if (calculate_obtained_marks(student["Roll No"]) / (len([key for key in student.keys() if key not in student_headers]) * 100)) * 100 >= 50)
                    fail_count = len(students) - pass_count
                    print(f"Pass Count: {pass_count}")
                    print(f"Fail Count: {fail_count}")
                case "_":
                    print("Invalid choice")

        if choice == "5":
            print("Reports selected")
            # Implement report generation logic here
            continue
        
        if choice == "6":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
    