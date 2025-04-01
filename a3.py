class Circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3*4
    def perimeter(self):
        return 2*self.radius*3.14
radius=int(input("Enter radius: "))
NewCircle=Circle(radius)
print(NewCircle.area())
print(NewCircle.perimeter())