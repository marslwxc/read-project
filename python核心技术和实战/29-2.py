class Foo:

    def __init__(self):
        print('__init__ called')

    def __enter__(self):
        print('__enter__ called')

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('__exit__ called')
        if exc_type:
            print('exc_type:{},exc_value:{},exc_traceback{},exception handled'.format(exc_type, exc_value, exc_tb))
        return True


with Foo() as obj:
    raise Exception('exception raised').with_traceback(None)