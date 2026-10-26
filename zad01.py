class Dog:
    def __init__(self,name:str,age:int, breed:str) -> None:
        self.name: str = name
        self.age: int = age
        self.breed: str = breed
    def show(self) -> None:
        print(f"Name:{self.name}")
        print(f"Breed:{self.breed}")
        print(f"Age:{self.age}")
    def update(self, new_name:str, new_age:int, new_breed:str) -> None:
        self.name = new_name
        self.age = new_age
        self.breed = new_breed

d1:Dog = Dog("Snoopy", 5, "Beagle")
d2:Dog = Dog("Scooby", age=7, breed="Golden Retriver")
d3: Dog = Dog("Pluto", age=3, breed="Boxer")

d1.show()

d2.show()

d3.show()