import numpy
from function import Function
from operator_calc import Operator
from queue import Queue
from stack import Stack
import numbers
import re
class Calculator:
    def __init__(self):
        self.functions = {'EXP' : Function(numpy.exp),
                          'LOG': Function (numpy.log),
                          'SIN' : Function (numpy.sin),
                          'COS' : Function (numpy.cos),
                          'SQRT' : Function (numpy.sqrt)}

        self.operators = {'ADD' : Operator(numpy.add, 0),
                          'MULTIPLY' : Operator(numpy.multiply, 1),
                          'DIVIDE' : Operator(numpy.divide, 1),
                          'SUBTRACT' : Operator(numpy.subtract,0)}

        self.output_queue = Queue()



    def RPN(self):
        stack = Stack()
        print(self.output_queue)
        while not self.output_queue.is_empty():
            element = self.output_queue.pop()
            if(isinstance(element, numbers.Number)):
                stack.push(element)

            if(isinstance(element, Function)):
                stack.push(element.execute(stack.pop()))

            if(isinstance(element, Operator)):
                element_one = stack.pop()
                element_two = stack.pop()
                stack.push(element.execute(element_one, element_two))
        return stack.items[0]


    def convert_to_RPN(self, input_queue):
        operator_stack = Stack()

        while not input_queue.is_empty():
            element = input_queue.pop()
            if(isinstance(element, numbers.Number)):
                self.output_queue.push(element)
            if(isinstance(element, Function)):
                operator_stack.push(element)
            if(element == "("):
                operator_stack.push(element)
            if(element== ")"):
                while not operator_stack.peek() == "(":
                    self.output_queue.push(operator_stack.pop())
                operator_stack.pop()

            if(isinstance(element, Operator)):
                while True:
                    if(operator_stack.is_empty() or operator_stack.peek() == "("):
                        break
                    if(isinstance(operator_stack.peek(), Operator)):
                        if (operator_stack.peek().strength < element.strength):
                            break
                    self.output_queue.push(operator_stack.pop())
                operator_stack.push(element)

        while not operator_stack.is_empty():
            self.output_queue.push(operator_stack.pop())

        return self.output_queue


    def parse_text(self, text):
        input_queue = Queue()
        number_pattern = '^[0123456789.]+'
        function_pattern = '|'.join(['^'+func for func in self.functions])
        operation_pattern = '|'.join(['^' + op for op in self.operators])
        parantheses_pattern = r'^\(|^\)'
        text = text.replace(' ','').upper()

        while len(text) != 0:
            if(re.search(number_pattern, text) != None):
                input_queue.push(float(re.search(number_pattern, text).group(0)))
                text = text[re.search(number_pattern, text).end(0):]

            if (re.search(function_pattern, text) != None):
                input_queue.push(self.functions[re.search(function_pattern, text).group(0)])
                text = text[re.search(function_pattern, text).end(0):]

            if (re.search(operation_pattern, text) != None):
                input_queue.push(self.operators[re.search(operation_pattern, text).group(0)])
                text = text[re.search(operation_pattern, text).end(0):]
            if(re.search(parantheses_pattern, text) != None):
                input_queue.push(re.search(parantheses_pattern, text))
                text = text[re.search(parantheses_pattern, text).end(0):]
        return input_queue

    def calculate_expression(self, text):
        input_queue = self.parse_text(text)
        self.convert_to_RPN(input_queue)
        return self.RPN()



if __name__ == '__main__':
    calc = Calculator()
    #print(calc.functions['EXP'].execute(calc.operators['ADD'].execute(1,calc.operators['MULTIPLY'].execute(2,3))))
    #print("\n")
    """calc.output_queue.push(2)
    calc.output_queue.push(3)
    calc.output_queue.push(calc.operators['ADD'])
    print(calc.RPN())"""
    """queue = Queue()
    queue.push(calc.functions['EXP'])
    queue.push("(")
    queue.push(1)
    queue.push(calc.operators['ADD'])
    queue.push(2)
    queue.push(calc.operators['MULTIPLY'])
    queue.push(3)
    queue.push(")")
    queue.push(2)
    queue.push(calc.operators['MULTIPLY'])
    queue.push(3)
    queue.push(calc.operators['ADD'])
    queue.push(1)
    q = calc.convert_to_RPN(queue)
    print(q)"""
    print(calc.calculate_expression("5 add 3 multiply 5"))
