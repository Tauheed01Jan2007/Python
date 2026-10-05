# total_attempt = int(input("ENter your attempts:"))
# Incorrect = int(input("ENter your incorrect:"))
# def score(total_attempt , Incorrect):
#     total_Ques = 100
#     Q1 = 2
#     neg_Incorrect = 0.5
#     correct = total_attempt - Incorrect
#     total_num = correct * Q1 - Incorrect * neg_Incorrect
#     print(total_num)
# score(total_attempt , Incorrect)

ta = int(input("ENter your attempts:"))
ic = int(input("ENter your incorrect:"))
def mark_sco(ta, ic):
    crr = ta - ic
    tcm = crr *2
    tim = ic * 0.5
    sc = tcm - tim
    print("your final score: ",sc)
mark_sco(ta, ic)