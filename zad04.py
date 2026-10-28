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


s1 = Student("Jacob","Smith","Computer Science",3)
p1 = Professor("Adam","Jones","Discrete Mathematics","Phd")

people = [s1,p1]


#pola rozdzielono średnikiem, po jednym obiekcie w wierszu

with open("dane.txt", "w") as f:
    for person in people:
        line: str = str(type(person).__name__) + ";" + ";".join(str(val) for val in person.__dict__.values())  # pyright: ignore[reportAny]
        _=f.write(line + "\n")

recreated_people = []

classes = {

    "Student": Student,
    "Professor": Professor
}

file = None
try:
    with open(file="dane.txt", mode="r") as f:

        file = f.read().splitlines()
except FileNotFoundError:
    print("Error: file not found")



if file is not None:
    for line in file:

        line_number: int = file.index(line) + 1

        line = line.strip()

        data = line.split(";")

        class_name = data[0]

        attributes = data[1:]

        if len(attributes) != 4:
            print(f"Error: malformed line {line_number}")
            continue

  

        if class_name in classes:

            _class = classes[class_name]

            new_object = _class(*attributes)  # pyright: ignore[reportArgumentType]

            recreated_people.append(new_object)  # pyright: ignore[reportUnknownMemberType]
        else:
            print(f"Unknown class type {class_name}")