from datetime import date, datetime


class IntField:
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass


class User:
    age = IntField()


if __name__ == '__main__':
    user = User() 