# Problem: Nested Lists
# Domain: Python (Basic Data Types)
# Difficulty: Easy

if __name__ == '__main__':
    students = []
    
    # Read number of students and their details
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Extract unique scores and find the second lowest score
    scores = sorted(set(student[1] for student in students))
    second_lowest_score = scores[1]
    
    # Collect names of students with the second lowest score
    second_lowest_students = [
        student[0] for student in students if student[1] == second_lowest_score
    ]
    
    # Sort names alphabetically and print
    for name in sorted(second_lowest_students):
        print(name)