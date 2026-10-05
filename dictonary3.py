d = {5:'lion' , 'r':89 , 7:[88,44,{'name':'Arpit', 'marks' : [45,34,41]} , 22, 77]}
name = d[7][2]['name']
marks = d[7][2]['marks']
sum(marks)
len(marks)
avg = sum(marks)/len(marks)
print(name,avg)


# sum = 0
# for i in d[7][2]['marks']:
#     sum = i + sum
#     avg = sum/3
# print(avg)