"""
class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house # Property (without _)

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("house: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
"""



class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house # Property (without _)

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    @property       # Name Getter
    def name(self):
        return self._name
    
    @name.setter    # Name Setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    @property       # House Getter
    def house(self):
        return self._house
    
    @house.setter   # House Setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house # Instance Variable (with _)


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("house: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
