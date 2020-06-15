def singleton(singleton_class):
    """
    Declaring the decorator function to apply to a class
    which will make the class to behave as a Singleton.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        """ docstring for get_instance """
        if singleton_class not in instances:
            instances[singleton_class] = singleton_class(*args, **kwargs)
        return instances[singleton_class]
    return get_instance


@singleton
class TestClass(object):

    def __init__(self):
        self.some_field = 10


first_instance = TestClass()
print(first_instance.some_field)
first_instance.some_field = 20

second_instance = TestClass()
print(second_instance.some_field)
