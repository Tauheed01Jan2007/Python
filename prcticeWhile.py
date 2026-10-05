t =input()
while t>0:
    s = input()
    count_a = 0
    count_b = 0
    for i in s:
        if i == 'a':
            count_a
        else:
            count_b
    if count_b<count_a:
        print(count_a)
    else:
        print(count_b)
    t-=1