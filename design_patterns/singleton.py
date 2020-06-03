class Singleton(object):
    """Singleton realisation via Python"""

    _instance = None

    def __new__(cls):
        """
            Create an intance for the first time with some field
            or return an already created one
        """
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls.some_field = 10
        return cls._instance


# create the first instance
first_instance = Singleton()
print(first_instance.some_field)

# change the field value of the created instance
first_instance.some_field = 20

# create the second instance and view the updated field
second_instance = Singleton()
print(second_instance.some_field)
