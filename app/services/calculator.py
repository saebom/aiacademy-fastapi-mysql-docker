from app.models.calculator import Calculator
class CalculatorService(object):
    def __init__(self)-> None: 
        pass
        
    def calculate(self, first, second):
        calculator = Calculator(first, second)
        print(f'첫번째 수 : {calculator.first}')
        print(f'두번째 수 : {calculator.second}')
        print(f'더하기 : {calculator.first} + {calculator.second} = {calculator.sum()}')
        print(f'빼기 : {calculator.first} - {calculator.second} = {calculator.extract()}')
        print(f'곱하기 : {calculator.first} * {calculator.second} = {calculator.multiply()}')
        print(f'나누기 : {calculator.first} / {calculator.second} = {calculator.divide()}')
        