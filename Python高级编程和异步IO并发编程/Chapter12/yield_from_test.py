# python3.3新加入yield from语法
from itertools import chain


my_list = [1, 2, 3]
my_dict = {
    'b12': 'http://projectedu.com',
    'b22': 'http://www.baidu.com',
}
for value in chain(my_list, my_dict, range(5,10)):
    print(value)