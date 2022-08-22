class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def increase_salary(self):
        self.salary=self.salary+1000
    def decrease_salary(self):
        self.salary=self.salary-2000
    def display(self):
        print(self.name,self.age,self.salary)

obj=employee("nikhil",25,25000)
obj.display()
obj.increase_salary()
obj.display()
obj.decrease_salary()
obj.display()
print(obj.name)
print(obj.age)
print(obj.salary)

