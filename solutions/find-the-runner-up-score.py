# Problem: Find the Runner-Up Score!
# Domain: Python (Basic Data Types)
# Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Remove duplicates by converting to set, then sort descending
    unique_scores = sorted(set(arr), reverse=True)
    
    # The second element (index 1) is the runner-up score
    print(unique_scores[1])