class Fraction:
    def __init__(self,s,m):
        #properties
        self.soorat=s
        self.makhraj=m

    #methods
    def show(self):
        print(self.soorat,"/",self.makhraj)
        
    def sum(self,other):
        result_s=self.soorat*other.makhraj+other.soorat*self.makhraj
        result_m=self.makhraj*other.makhraj
        x=Fraction(result_s,result_m)
        return x

    def sub(self,other):
        result_s=self.soorat*other.makhraj-other.soorat*self.makhraj
        result_m=self.makhraj*other.makhraj
        x=Fraction(result_s,result_m)
        return x

    def mul(self,other):
        result_s=self.soorat*other.soorat
        result_m=self.makhraj*other.makhraj
        x=Fraction(result_s,result_m)
        return x

    def div(self,other):
        result_s=self.soorat*other.makhraj
        result_m=self.makhraj*other.soorat
        x=Fraction(result_s,result_m)
        return x

    def fraction_to_number(self):
        result=self.soorat/self.makhraj
        return result

    def simplify(self):
        for i in range(min(self.soorat,self.makhraj),0,-1):
            if (self.soorat % i ==0) and (self.makhraj % i == 0):
                new_s=int(self.soorat/i)
                new_m=int(self.makhraj/i)
                break
        x=Fraction(new_s,new_m)
        return x


a=Fraction(2,6)
print("a = ",end='')
a.show()

b=Fraction(7,5)
print("b = ",end='')
b.show()

# a+b
sum_ans=b.sum(a)
print("a + b = ",end='')
sum_ans.show()

# a-b
sub_ans=a.sub(b)
print("a - b = ",end='')
sub_ans.show()

# a*b
mul_ans=a.mul(b)
print("a * b = ",end='')
mul_ans.show()

# a/b
div_ans=a.div(b)
print("a / b = ",end='')
div_ans.show()

#convert to decimal number
to_decimal=a.fraction_to_number()
print("fraction to decimal (a) = ",end='')
print(to_decimal)

#simplify
simp_ans=a.simplify()
print("simplified (a) = ",end='')
simp_ans.show()
