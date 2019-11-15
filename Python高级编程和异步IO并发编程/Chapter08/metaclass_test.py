# 类也是对象，type是创建类的类
def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company


# type动态创建类
class BaseClass:
    def answer(self):
        return 'i am baseclass'

def say(self):
    return 'i am {}'.format(self.name)

User = type('user', (BaseClass,), {'name':"user", 'say':say})


# 元类是创见类的类，对象<-class(对象)<-type
class MetaClass(type):
    pass
class User(metaclass=MetaClass):
    pass


# Python中类的实例化过程，会首先寻找metaclass属性，通过metaclass去创建类
# type创建类对象，实例


if __name__ == "__main__":
    # MyClass = create_class('user')
    # my_obj = MyClass()
    # print(type(my_obj))

    my_obj = User()
    print(my_obj.answer())