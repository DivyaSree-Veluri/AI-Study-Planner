subjects = input("Enter subjects separated by commas: ")
days = int(input("Days left for exam: "))
hours = int(input("Study hours per day: "))

subject_list = [subject.strip() for subject in subjects.split(",")]

hours_per_subject = hours / len(subject_list)

for day in range(1, days + 1):
    print(f"\nDay {day}")

    for subject in subject_list:
        print(f"{subject} - {round(hours_per_subject, 1)} hours")
