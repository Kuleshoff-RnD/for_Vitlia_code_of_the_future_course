'''
Реализовать родительский класс человека, 
а также дочерние классы директора, преподавателя и ученика. 
Описать для каждого класса необходимые свойства и методы.

Важно: директор помимо своих обязанностей может также и преподавать (множественное наследование). 
'''
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_speak(self):
        print('Hello!')

    def to_listen(self):
        print('I hear you')


class Student(Human):
    def __init__(self, name, age, group_num, gpa):
        super().__init__(name, age)
        self.group_num = group_num
        self.gpa = gpa

    def say_gpa(self):
        print(f' My Grade Point Average is  {self.gpa}')


class Teacher(Human):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def say_course(self):
        print(f' My course is  {self.course}')

    def teach_course(self):
        print(f' I teach a course  {self.course}')

class Director(Teacher, Human):
    def __init__(self, name, age, course, reception_hours):
        super().__init__(name, age, course)
        self.reception_hours = reception_hours

    def to_receive(self):
        print(f' I receive people at {self.reception_hours}')

st1 = Student('Vitlia', 14, '8A', 5,)
print('')
st1.to_speak()
print(f'I am a Student, my name is {st1.name}')
st1.say_gpa()


th1 = Teacher('Polina', 22, 'programing')
print('')
th1.to_speak()
print(f'I am a Teacher, my name is {th1.name}')
th1.teach_course()

dir1 = Director('Vasiliy', 35, 'math', '15 p.m')
print('')
dir1.to_speak()
print(f'I am a Director, my name is {dir1.name}')
dir1.say_course()
dir1.to_receive()
