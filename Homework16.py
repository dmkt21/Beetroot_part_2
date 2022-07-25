# task01

class Person():
    is_human = True

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

class Student(Person):
    def __init__(self, first_name, last_name, gender, age, course, faculty):
        super().__init__(first_name, last_name, gender, age)
        self.course = course
        self.faculty = faculty


class Teacher(Person):
    def __init__(self, first_name, last_name, gender, age, salary, years_of_service):
        super().__init__(first_name, last_name, gender, age)
        self.salary = salary
        self.years_of_service = years_of_service

#task02
import calendar


class Mathematician:

    @staticmethod
    def square_nums(square_number):
        return [x ** 2 for x in square_number]

    @staticmethod
    def remove_positives(all_numbers):
        return [x for x in all_numbers if x < 0]

    @staticmethod
    def filter_leaps(all_years):
        return [x for x in all_years if calendar.isleap(x) is True]

#task04

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as x:
            x.write(msg + '\n')

def main():

    # task02
    m = Mathematician()

    print(m.square_nums([7, 11, 5, 4]))
    print(m.remove_positives([26, -11, -8, 13, -90]))
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))


if __name__ == '__main__':
    main()
