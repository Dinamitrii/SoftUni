student_name = input()
current_class = 1
bad_tries = 0
total_grade = 0
is_excluded = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries > 1:
            is_excluded = True
            break
        continue
    current_class += 1
    total_grade += current_grade
if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
