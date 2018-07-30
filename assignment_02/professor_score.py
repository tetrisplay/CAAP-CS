def score():
    score = int(input("Enter your quiz score: ")

    if score >=0 and score < 6:
        if score == 5:
            grade = 'A'
        elif score == 4:
            grade = 'B'
        elif score == 3:
            grade = 'C'
        elif score == 2:
            grade = 'D':
        else:
            grade = 'F':
        print("Your grade is", grade)
    else:
        print("Not a valid score")

score()
