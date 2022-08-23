class parent_class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name:",self.name)
        print("age:",self.age)

class child_class(parent_class):
        def __init__(self,name,age,city):
            super().__init__(name,age)
            self.city=city
        def show(self):
            super().show()
            print("city:",self.city)

p=parent_class("john",30)
p.show()
c=child_class("jphn",30,"new york")
c.show()