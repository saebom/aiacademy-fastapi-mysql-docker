class Grade(object):
    def __init__(self, name, kor, eng, math) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.avg = 0.0
        
    def set_avg(self):      # set 쓰기 (set은 '=' assignment를 사용)
        self.avg = (self.kor + self.eng + self.math)/3
        
    def get_avg(self):      # get 읽기(get은 returndmf tkdyd)    
        return self.avg
    