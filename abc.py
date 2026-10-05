
total_ques=int(input("toal no of question: "))
total_attempt=int(input("total attampt question: "))
incorrect_attempt=int(input("no. of incorrect question: "))
correct_marks=int(input("marks for current attempt: "))
incorrect_marks=eval(input("marks for current attempt: "))
correct_mark=total_attempt-incorrect_attempt
incorrect_mark=incorrect_attempt * incorrect_marks
final_score=correct_mark - incorrect_mark
print("Your final score is: ",final_score)
