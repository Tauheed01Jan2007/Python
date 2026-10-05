x = [42,'s',True,86.5,'car',[23,'mango',45.6]]
x.append([1,2,3,4,5,6,7])
print(x)

x = [42,'s',True,86.5,'car',[23,'mango',45.6]]
x.extend([1,2,3,4,5,6,7])
print(x)

x = [42,'s',True,[23,'mango',45.6],86.5,'car']
print(x[3][1])


x = [42,'s',True,[23,'mango',45.6],86.5,'car']
x[3].insert(3,45)


y = [23,4,678,900]
y.append(65)
print(y)

y = [23,4,678,900,65]
y.insert(3,56)
print(y)

y = [23,4,678,900,65]
y.extend([2,3,4,5])
print(y)


y = [23,4,678,900,65]
y.remove(65)
print(y)

y = [23,4,678,900,65]
y.pop(-1)
print(y)
y.pop(0)
print(y)

x = [2, 56, 89, 112 ,68, 8]


abcd = [12,31,54,78,99,24,18,90]
sum = 0
for i in abcd:
    sum += i
print(sum)


abcd = [12,31,54,78,99,24,18,90]
sum = 0
for i in range(len(abcd)):
    sum += abcd[i]
print(sum)


abcd = [12,31,54,78,99,24,18,90]
for i in range(len(abcd)):
    abcd[i] = abcd[i]*2
print(abcd)
    
    
abcd = [12,31,54,78,99,24,18,90]
sum = 0
for i in abcd:
    sum += i
    if i%2 == 0:
        print(i,end=" ")
