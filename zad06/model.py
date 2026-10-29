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