class Complex:

    def __init__(self,real,image):
        self.real=real
        self.image=image

    def show(self):
        print(self.real,"+",self.image,"i")

    def sum(self,other):
        real_new=self.real + other.real
        image_new=self.image + other.image
        result=Complex(real_new,image_new)
        return result

    def sub(self,other):
        real_new=self.real - other.real
        image_new=self.image - other.image
        result=Complex(real_new,image_new)
        return result

    def mul(self,other):
        # (a+bi)(c+di)=ac+adi+bci+bdi^2=(ac-bd)+(ad+bc)i
        real_new=self.real*other.real - self.image*other.image  
        image_new=self.real*other.image + self.image*other.real
        result=Complex(real_new,image_new)
        return result


# a
a= Complex(5,8)
print("a = ",end='')
a.show()

# b
b= Complex(-7,10)
print("b = ",end='')
b.show()

# a + b
sum_ans= a.sum(b)
print("a + b = ",end='')
sum_ans.show()

# a - b
sub_ans= a.sub(b)
print("a - b = ",end='')
sub_ans.show()

# a * b
mul_ans= a.mul(b)
print("a * b = ",end='')
mul_ans.show()
