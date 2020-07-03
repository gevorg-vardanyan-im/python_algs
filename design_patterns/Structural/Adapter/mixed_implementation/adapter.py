class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def two_wheeler(self):
        return "TwoWheeler"


class Truck:
    """Class for Truck"""

    def __init__(self):
        self.name = "Truck"

    def eight_wheeler(self):
        return "EightWheeler"


class Car:
    """Class for Car"""

    def __init__(self):
        self.name = "Car"

    def four_wheeler(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.two_wheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.object = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.object, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.object.__dict__


if __name__ == "__main__":
    """list to store objects"""
    objects = []

    motor_cycle = MotorCycle()
    objects.append(Adapter(motor_cycle, wheels=motor_cycle.two_wheeler))

    truck = Truck()
    objects.append(Adapter(truck, wheels=truck.eight_wheeler))

    car = Car()
    objects.append(Adapter(car, wheels=car.four_wheeler))

    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))
