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


# task03

class TVController():

    def __init__(self, list_of_channels):
        self.list_of_channels = list_of_channels
        self.default_channel = 0

    def first_channel(self):
        return self.list_of_channels[0]

    def last_channel(self):
        return self.list_of_channels[-1]

    def turn_channel(self, channel_number):
        self.default_channel = channel_number - 1
        return self.current_channel()

    def previous_next(self, delta):
        self.default_channel = (self.default_channel + delta) % \
                               len(self.list_of_channels)
        return self.current_channel()

    def next_channel(self):
        return self.previous_next(1)

    def previous_channel(self):
        return self.previous_next(-1)

    def current_channel(self):
        return self.list_of_channels[self.default_channel]

    def is_exist(self, channel_name):
        if isinstance(channel_name, int):
            x = 0 <= channel_name < len(self.list_of_channels)
        else:
            x = channel_name in self.list_of_channels
        return ('No', 'Yes')[x]


def main():

    carl_johnson_26 = Person('Carl', 'Johnson', 26)
    carl_johnson_26.talk()

    dog_5 = Dog(7)
    print(dog_5.human_age())

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = TVController(CHANNELS)
    print(controller.first_channel() == 'BBC')
    print(controller.last_channel() == 'TV1000')
    print(controller.turn_channel(1) == 'BBC')
    print(controller.next_channel() == 'Discovery')
    print(controller.previous_channel() == 'BBC')
    print(controller.current_channel() == 'BBC')
    print(controller.is_exist(4) == "No")
    print(controller.is_exist("BBC") == "Yes")


if __name__ == '__main__':
    main()





