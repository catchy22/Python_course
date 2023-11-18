class rectangle:

    def __init__(self,width,length):
        self.width=width
        self.length=length

    def get_square(self):
        return self.width*self.length

r1=rectangle(5,5)
r2=rectangle(2,2.5)

print(r1.get_square())
print(r2.get_square())