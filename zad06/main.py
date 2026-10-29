from .model import Professor, Student
from .operations import write_to_txt

if __name__ == "__main__":
    s1 = Student("Jacob","Smith","Computer Science",3)
    p1 = Professor("Adam","Jones","Discrete Mathematics","Phd")
    s2 = Student("Cyndi", "Richards", "Physics", 2)
    p2 = Professor("Peter", "Mayers", "Calculus", "Phd")
    p3 = Professor("Barbra", "Hawkins", "Programming", "Ms")
    s3 = Student("Alice", "Lovelace", "Mathematics", 3)
    people = [s1, s2, s3, p1, p2, p3]

    write_to_txt(people)
    