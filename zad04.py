from typing import override


class Person:
    def __init__(self,fname:str, lname:str) -> None:
        self.firstname:str = fname
        self.lastname:str = lname
    def introduce(self) -> str:
        return f"My name is {self.firstname} {self.lastname}"

    def printname(self) -> None:
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self,fname:str,lname:str, filedofstudy:str, year:int) -> None:
        super().__init__(fname,lname)
        self.fieldofstudy: str = filedofstudy
        self.year:int = year
    @override
    def introduce(self) -> str:
        return f"My name is {self.firstname} {self.lastname}. I'm a {self.year} year student of {self.fieldofstudy}"

    def greeting(self) -> str:
        return "Hi!"
class Professor(Person):
    def __init__(self,fname:str,lname:str,subject:str,title:str) -> None:
        super().__init__(fname,lname)
        self.subject: str = subject
        self.title: str = title

    def greeting(self) -> str:
        return "Good morning"


student = Student("Jacob","Smith","Computer Science",3)
professor = Professor("Adam","Jones","Discrete Mathematics","Phd")

people = [student,professor]


#pola rozdzielono średnikiem, po jednym obiekcie w wierszu

with open("dane.txt", "w") as f:
    for person in people:
        line: str = ";".join(str(val) for val in person.__dict__.values())  # pyright: ignore[reportAny]
        _=f.write(line + "\n")


    
        
