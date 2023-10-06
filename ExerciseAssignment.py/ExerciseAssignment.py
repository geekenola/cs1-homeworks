#TASK1
x = 120  # You can change the value of x as needed

if x > 100:
    y = 20
    z = 40

#TASK2
a = 5  # You can change the value of a as needed

if a < 10:
    b = 0
else:
    b = 99

#TASK3
amount1 = 15  # You can change the values of amount1 and amount2 as needed
amount2 = 85

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
            print(amount1)
        else:
            print(amount2)
#TASK4
speed = 40  # You can change the value of speed as needed

if 24 <= speed <= 56:
    print('Speed is normal')
else:
    print('Speed is abnormal')

#TASK5
score = 85  # You can change the value of score as needed
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
