class Student(object):
    def __init__(self, name, number):
        self.name = name

    def getName(self):
        return self.name

    def __eq__(self, student):
        return self.name == student.name 

    def __lt__(self, student):
        return self.name < student.name 

    def __gt__(self, student):
        return self.name > student.name or self.name == student.name

def main():
    s1 = Student("Taylor", 10)
    s2 = Student("Brent", 20)
    print(s1.getName() + " is equal to " + s2.getName() + " = " + str(s1.__eq__(s2)))
    print(s1.getName() + " is less than " + s2.getName() + " = " + str(s1.__lt__(s2)))
    print(s1.getName() + " is greater than or equal to " + s2.getName() + " = " + str(s1.__gt__(s2)))

if __name__ == "__main__":
 main()
