from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self) -> None:
        pass


class Student(Person):
    def __init__(self, name, yob, grade: str) -> None:
        super().__init__(name, yob)
        self.grade = grade

    def describe(self) -> None:
        print(f"Student - Name: {self.name} -Yob: {self.yob} -Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject: str) -> None:
        super().__init__(name, yob)
        self.subject = subject

    def describe(self) -> None:
        print(f"Teacher - Name: {self.name} -Yob: {self.yob} -Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist: str) -> None:
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self) -> None:
        print(
            f"Doctor - Name: {self.name} -Yob: {self.yob} -Specialist: {self.specialist}"
        )


class Ward:
    def __init__(self, name: str) -> None:
        self.name = name
        self.list_person = []

    def add_person(self, person: "Person") -> None:
        self.list_person.append(person)

    def describe(self) -> None:
        print(f"Ward name: {self.name}")
        for person in self.list_person:
            person.describe()

    def count_doctor(self) -> int:
        count = 0
        for person in self.list_person:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self) -> None:
        self.list_person.sort(key=lambda person: person.yob)

    def compute_average(self) -> 'float | None':
        total_yob = 0
        total_teacher = 0
        for person in self.list_person:
            if isinstance(person,Teacher):
                total_yob += person.yob
                total_teacher += 1
        average_yob = total_yob / total_teacher
        return average_yob

def main() -> None:
    # 2(a)
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()
    # output
    # >> Student - Name : studentA - YoB : 2010 - Grade : 7

    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()
    # output
    # >> Teacher - Name : teacherA - YoB : 1969 - Subject : Math

    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()
    # output
    # >> Doctor - Name : doctorA - YoB : 1945 - Specialist : Endocrinologists

    # 2(b)
    print()
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # output
    # >> Ward Name : Ward1
    # Student - Name : studentA - YoB : 2010 - Grade : 7
    # Teacher - Name : teacherA - YoB : 1969 - Subject : Math
    # Teacher - Name : teacherB - YoB : 1995 - Subject : History
    # Doctor - Name : doctorA - YoB : 1945 - Specialist : Endocrinologists
    # Doctor - Name : doctorB - YoB : 1975 - Specialist : Cardiologists

    # 2(c)
    print(f"\nNumber of doctors: {ward1.count_doctor()}")

    # output
    # >> Number of doctors : 2

    # 2(d)
    print("\nAfter sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()

    # 2(e)
    print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")

    # output
    # >> Average year of birth (teachers): 1982.0
if __name__ == "__main__":
    main()
