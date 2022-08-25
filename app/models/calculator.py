class Calculator(object):
    def __init__(self, first, second):  # 생성자 
        self.first = first              # 생성자에 속성(property) 등록
        self.second = second
        
    def sum(self):                      # 메소드
        return self.first + self.second
    
    def extract(self):
        return self.first - self.second
    
    def multiply(self):
        return self.first * self.second
    
    def divide(self):
        return self.first / self.second
    