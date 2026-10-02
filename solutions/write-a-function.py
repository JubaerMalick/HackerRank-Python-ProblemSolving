# Problem: Write a function (Leap Year Check)
# Domain: Python (Introduction)
# Difficulty: Easy

def is_leap(year):
    leap = False
    
    # Logic for checking leap year
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
        
    return leap

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))