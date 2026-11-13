"""Placement Readiness Tracker | IRP-II CSE2596
Author: Soumen Kumar Dutta | URN: 2481248
"""
SUBJECTS = ("aptitude", "verbal", "coding")

students = [
    {"name": "Soumen Kumar Dutta", "roll_no": "2481248", "aptitude": 91, "verbal": 85, "coding": 87},
    {"name": "Student 02", "roll_no": "S002", "aptitude": 82, "verbal": 72, "coding": 90},
    {"name": "Student 03", "roll_no": "S003", "aptitude": 85, "verbal": 80, "coding": 87},
    {"name": "Student 04", "roll_no": "S004", "aptitude": 35, "verbal": 45, "coding": 30},
    {"name": "Student 05", "roll_no": "S005", "aptitude": 77, "verbal": 92, "coding": 88},
]

def read_score(subject):
    """Read an integer score and reject values outside 0–100."""
    while True:
        try:
            score = int(input(f"{subject.title()} score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Invalid score. Enter a value from 0 to 100.")
        except ValueError:
            print("Invalid input. Enter a whole number from 0 to 100.")

def add_student():
    """Collect one student's details and append the validated record."""
    print("\nAdd a new student")
    name = input("Name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Name: ").strip()
    roll_no = input("Roll number: ").strip()
    while not roll_no:
        print("Roll number cannot be empty.")
        roll_no = input("Roll number: ").strip()
    student = {"name": name, "roll_no": roll_no}
    for subject in SUBJECTS:
        student[subject] = read_score(subject)
    students.append(student)

def average(student):
    """Return the mean of the three practice-test scores."""
    return sum(student[subject] for subject in SUBJECTS) / len(SUBJECTS)

def grade(avg):
    """Apply the assignment grade boundaries."""
    if avg >= 80:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 40:
        return "C"
    return "Needs practice"

def top_scorer(students):
    """Return the student with the highest average."""
    return max(students, key=average)

def needs_practice(students, limit=40):
    """Return students whose average is below limit."""
    return [student for student in students if average(student) < limit]

def print_results(students):
    """Print a neatly aligned results table."""
    # Keep report columns aligned with assignment fields.
    headers = ("Name", "Roll No.", "Aptitude", "Verbal", "Coding", "Average", "Grade")
    rows = [headers]
    for student in students:
        rows.append((student["name"], student["roll_no"], str(student["aptitude"]),
                     str(student["verbal"]), str(student["coding"]),
                     f"{average(student):.2f}", grade(average(student))))
    widths = [max(len(str(row[i])) for row in rows) for i in range(len(headers))]
    print("\nPLACEMENT READINESS REPORT")
    print(" | ".join(headers[i].ljust(widths[i]) for i in range(len(headers))))
    print("-+-".join("-" * width for width in widths))
    for row in rows[1:]:
        print(" | ".join(str(row[i]).ljust(widths[i]) for i in range(len(headers))))

def main():
    print("PLACEMENT READINESS TRACKER")
    print(f"Existing student records: {len(students)}")
    add_student()
    print_results(students)
    best = top_scorer(students)
    print(f"\nTop scorer: {best['name']} ({best['roll_no']})")
    print(f"Highest average: {average(best):.2f}")
    practice_list = needs_practice(students)
    print(f"\nStudents needing practice (average below 40): {len(practice_list)}")
    if practice_list:
        for student in practice_list:
            print(f"- {student['name']} ({student['roll_no']}): {average(student):.2f}")
    else:
        print("None")

if __name__ == "__main__":
    main()
