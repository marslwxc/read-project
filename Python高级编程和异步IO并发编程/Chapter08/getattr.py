# __getattr__    __getattribute__
from datetime import date, datetime

# __getattr__ 在查找不到属性时调用
# __getattribute__ 第一时间访问
class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        # return 'not find attr'
        return self.info[item]

    def __getattribute__(self, item):
        return 'first_time'

if __name__ == '__main__':
    user = User('bobby', date(year=1993, month=1, day=1), info={'company_name':'name'})
    # print(user.age) # not find attr
    # print(user.company_name) # name
    print(user.name) # first_time