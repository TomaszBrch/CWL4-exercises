from typing import override


class Dog:
    def __init__(self,name:str,age:int, breed:str,owner:str ) -> None:
        self.name: str = name
        self.age: int = age
        self.breed: str = breed
        self.__owner : str = owner
    def show(self) -> tuple[str,str,int]:
        return self.name, self.breed, self.age
    def update(self, new_name:str, new_age:int, new_breed:str) -> None:
        self.name = new_name
        if type(new_age) is not int:
            raise ValueError("Error: invalid value")
        self.age = new_age
        
        self.breed = new_breed
    @override
    def __str__(self) -> str:
        return f"{self.name} ({self.age}, {self.breed})"
    @override
    def __repr__(self) -> str:
        return f"Dog(name={self.name},age={self.age}, breed={self.breed})"


d1:Dog = Dog("Snoopy", 5, "Beagle", "Mr Smith" )

print(d1)

print(repr(d1))
# class Car:
#     def __init__(self,make,model,year,vin,color) -> None:  
#         self.__make = make
#         self.__model = model
