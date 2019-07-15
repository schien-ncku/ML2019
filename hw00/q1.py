import sys

index = int(sys.argv[1])
filename = str(sys.argv[2])

target = index-1  # the selected column
answers = []  # the list to store answers

with open(filename) as f:
    for line in f:
        n = line.split()
        answers.append(float(n[target]))
        
sorted_answers = sorted(answers)  # sort the answers and save the result to a new list

open('ans1.txt', 'w').write(str(sorted_answers))
