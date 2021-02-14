import numpy
import numbers
class Operator:
    def __init__(self, operate, strength):
        self.operate = operate
        self.strength = strength

    def execute(self, num_one, num_two, debug=True):
        if not isinstance(num_one, numbers.Number) or not isinstance(num_two, numbers.Number):
            raise TypeError("The element must be a number")
        result = self.operate(num_one, num_two)

        if debug is True:
            print("Operation: " + self.operate.__name__ + "({:f}) = {:f}".format(num_two,num_two, result))

        return result

if __name__ == '__main__':
    add = Operator(numpy.add, 0)
    multi = Operator(numpy.multiply, 1)
    print(add.execute(2,3), " multi")
    #print(add.execute(1, multi.execute(2,3)))


