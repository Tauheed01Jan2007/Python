class Calculator:
    def __init__(self, n1, n2, oper):
        self.n1 = n1
        self.n2 = n2
        self.oper = oper
    
    def add(self):
        add = self.n1 + self.n2
        print("add : "+str(add))
    
    def sub(self):
        sub = self.n1 - self.n2
        print("sub : "+str(sub))
    
    def mul(self):
        mul = self.n1 * self.n2
        print("mul : "+str(mul))
    
    def div(self):
        div = self.n1 / self.n2
        print("div : "+str(div))
     
n1 = int(input(">>>"))   
n2 = int(input(">>>"))   
oper = input(">>>") 

c1 = Calculator(n1, n2, oper)
if oper == '+':
    a = c1.add()
elif oper == '-':
    s = c1.sub()
elif oper == '*':
    m = c1.mul()
elif oper == '/':
    d = c1.div()
    
    # ================ #
o = input(">>>")
n3 = int(input(">>>"))
if o == '+':
    ad = c1.a + n3
elif o == '-':
    su = c1.s - n3
elif o == '*':
    mul = c1.m * n3
elif o == '/':
    divd = c1.d / n3
