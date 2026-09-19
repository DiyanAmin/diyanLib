def convert_to_perc(num:float,decimal_places:int=2):
    '''
    Converts given float number to percentage
    
    :param num: The number
    :type num: float
    :param decimal_places: Amount of digits after decimal point
    :type decimal_places: int

    :return: The percentage as string
    :rtype: str
    '''

    return str(round(num * 100, decimal_places)) + '%'

def average(array:list):
    '''
    Finds the average or given array
    
    :param array: The array of numbers
    :type array: list

    :return: The average value
    :rtype: float
    '''

    if not array:
        return 'Invalid Array'

    return sum(array)/len(array)

#Handy calculator. JUST in case i need it.

class calculator():
    def __init__(self,num1:float,operation:str,num2:float,expression:str=''):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
        self.exp = expression
    
    def evaluate(self):
        if self.exp:
            try:
                return eval(self.exp)
            except Exception as e:
                return f"Error evaluating expression: {e}"
        return "Expression not provided"
    
    def add(self):
        return self.num1+self.num2
    
    def subtract(self):
        return self.num1-self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return 'Cannot divide by zero.'
    
    def exponent(self):
        return self.num1 ** self.num2
    
    def power(self):
        return self.num1 ** self.num2