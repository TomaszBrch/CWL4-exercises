
import json
from typing import override


class Person:
    def __init__(self,fname:str, lname:str) -> None:
        self.firstname:str = fname
        self.lastname:str = lname
    def introduce(self) -> str:
        return f"My name is {self.firstname} {self.lastname}"

    def printname(self) -> None:
        print(self.firstname,self.lastname)
    def to_dict(self):
        
        ob_dict = self.__dict__
        ob_dict["type"] = type(self).__name__
        
        return ob_dict
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
    @override
    def __str__(self) -> str:
        return f"{self.firstname}, {self.lastname}, {self.fieldofstudy}, {self.year}"
class Professor(Person):
    def __init__(self,fname:str,lname:str,subject:str,title:str) -> None:
        super().__init__(fname,lname)
        self.subject: str = subject
        self.title: str = title
    @override
    def __str__(self) -> str:
        return f"{self.firstname}, {self.lastname}, {self.subject}, {self.title}"

    def greeting(self) -> str:
        return "Good morning"


s1 = Student("Jacob","Smith","Computer Science",3)
p1 = Professor("Adam","Jones","Discrete Mathematics","Phd")
s2 = Student("Cyndi", "Richards", "Physics", 2)
p2 = Professor("Peter", "Mayers", "Calculus", "Phd")
p3 = Professor("Barbra", "Hawkins", "Programming", "Ms")
s3 = Student("Alice", "Lovelace", "Mathematics", 3)
people = [s1, s2, s3, p1, p2, p3]

people_dict = [person.to_dict() for person in people]


with open("dane.json", "w") as f:
    json.dump(people_dict,f,indent=4)


