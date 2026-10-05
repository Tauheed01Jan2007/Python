ttempt , Incorrect):
    total_Ques = 100
    Q1 = 2
    neg_Incorrect = 0.5
    total_attempt = int(input("ENter your attempts:"))
    Incorrect = int(input("ENter your incorrect:"))
    correct = total_attempt - Incorrect
    total_num = correct * Q1 - Incorrect * neg_Incorrect
    print(total_num)
score()