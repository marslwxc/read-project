# Python.ext会用一个叫做PyEval_EvalFamEx(c函数)去执行函数，
# 首先会创建一个栈帧对象，当函数调用子函数，又会创建一个栈帧
# 所有的栈帧都是分配在堆内存上，这就决定了栈帧可以独立于调用者存在 
from collections import UserList