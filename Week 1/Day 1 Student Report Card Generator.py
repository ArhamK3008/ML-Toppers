def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def assign_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

# Take user input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Input marks for 3 subjects
subjects = {}
subjects["Math"] = int(input("Enter marks for Math: "))
subjects["English"] = int(input("Enter marks for English: "))
subjects["Urdu"] = int(input("Enter marks for Urdu: "))

# Ask about bonus marks
bonus = input("Do you want to add 5 bonus marks to all subjects? (yes/no): ").lower()
if bonus == "yes":
    subjects = {subj: (lambda x: x + 5)(mark) for subj, mark in subjects.items()}

# Calculate average and grade
average = calculate_average(subjects)
grade = assign_grade(average)

# Write report to a file
filename = "report_card.txt"
with open(filename, "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    for subj, mark in subjects.items():
        f.write(f"{subj}: {mark}\n")
    f.write(f"Average: {average:.2f}\n")
    f.write(f"Grade: {grade}\n")

# Read and display report
print("\n--- Report Card ---")
with open(filename, "r") as f:
    print(f.read())
