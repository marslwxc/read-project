# 需求
import numbers


class Field(type):
    pass

class IntField(metaclass=Field):
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError('min_value must be int')
            elif min_value < 0:
                raise ValueError('min_value must be positive int')
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError('max_value must be int')
            elif max_value < 0:
                raise ValueError('max_value must be positive int')
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError('min_value must be smaller than max_value')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if value < self.min_value or value > self.max_value:
            raise ValueError('value must be between min_value and max_value')
        self._value = value


class CharField(metaclass=Field):
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.max_length = max_length
        self.db_column = db_column
        if max_length is None:
            raise ValueError('you must spcify max_length or charfield')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        if len(value) > self.max_length:
            raise ValueError('value len excess len of max_length') 
        self._value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        field = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                field[key] = value
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table 
        _meta['db_table'] = db_table 
        attrs['_meta'] = _meta
        attrs['fields'] = field
        del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()


class User(metaclass=BaseModel):
    name = CharField(db_column='', max_langth=10) 
    age = IntField(db_column='', min_value=0, max_value=100)

    class Meta:
        db_table = 'user'


if __name__ == "__main__":
    user = User()
    user.name = 'bobby'
    user.age = 28
    user.save()