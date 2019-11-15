class user:
    # __new__用来控制对象的生成过程，在对象生成之前，
    # 如果__new__不返回对象，则不会完成对象生成
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls) 

    # __init__用来完善对象的
    def __init__(self):
        pass