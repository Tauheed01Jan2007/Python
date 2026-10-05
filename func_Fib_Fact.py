def factroial(x):
    sum = 1
    for i in range(1,x+1):
        sum = sum * i
    return sum

#fibannaci numbers
def fibannaci(x):
    fib1 = 0
    fib2 = 1
    for i in range(1,x):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    return fib3