'''Moduk'''
import numbers
import numpy

class Function:
    '''Function class'''
    def __init__(self, func):
        '''Constructor'''
        self.func = func

    def execute(self, element, debug=True):
        '''Exectues'''
        if not isinstance(element, numbers.Number):
            raise TypeError("The element must be a number")
        result = self.func(element)

        if debug is True:
            print("Function: " + self.func.__name__ + "({:f}) = {:f}".format(element, result))

        return result
if __name__ == '__main__':
    exp = Function(numpy.exp)
    sin = Function(numpy.sin)
    print(exp.execute(sin.execute(0)))
