"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        "Create a new serial based on the number passed"
        self.start = self.next = start

    

    def generate(self):
        "Add one to the serial number"
        self.next += 1

        return self.next -1
    
    def reset(self):
        "reset the serial number"
        self.next = self.start
        return self.start