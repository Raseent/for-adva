class library:
    def __init__(self,name,number,books):
        self.name=name
        self.number=number
        self.books=[]

    def taken_books(self,book):
        self.books.append(book)
    def returned_books(self,book):
        self.books.remove(book)
    def display(self):
        print(self.name,self.number,self.books)
        print("books:")
        print(self.books)

obj=library("nikhil",25,3)
obj.taken_books("python")
obj.taken_books("java")
obj.taken_books("c++")
obj.display()
obj.returned_books("java")
obj.display()
obj.taken_books("c")
obj.display()


print(obj.name)
print(obj.number)
print(obj.books)



