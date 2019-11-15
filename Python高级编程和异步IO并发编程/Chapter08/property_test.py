from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    @property   # 属性描述符
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter # 为动态属性加入逻辑
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('bobby', date(year=1993, month=1, day=1))