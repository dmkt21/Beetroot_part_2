# task01

class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')

# task02


class Dog():
    AGE_FACTOR = 7

    def __init__(self, dogage):
        self.dogage = dogage

    def human_age(self):
        return self.AGE_FACTOR * self.dogage


def main():

    carl_johnson_26 = Person('Carl', 'Johnson', 26)
    carl_johnson_26.talk()

    dog_5 = Dog(7)
    print(dog_5.human_age())

if __name__ == '__main__':
    main()
