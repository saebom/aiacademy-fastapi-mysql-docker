from operator import index
from icecream import ic
import pandas as pd
import numpy as np
from torch import index_fill

class PandasQuiz(object):
    def __init__(self) -> None:
        pass
    
    """   Q1. 다음 결과 출력
        a  b  c
    1  1  3  5
    2  2  4  6
    ic| df1:       a  b  c
                1  1  3  5
                2  2  4  6
    """
    
    def quiz1(self) -> None :
       df = pd.DataFrame.from_dict(
           {'1' : [1, 3, 5], '2' : [2, 4, 6]},
           orient='index',
           columns=['a', 'b', 'c'])
       ic(df)

    """Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
    ic| df3:     0   1   2
                0  95  25  74
                1  44  24  97"""
                    
    def quiz2(self) -> None :
        df = pd.DataFrame.from_dict(
            {'1' :[np.random.randint(10, 100) for p in range(0, 3)], 
             '2' : [np.random.randint(10, 100) for p in range(0, 3)]},
            orient='index',
            columns=index)
        ic(df)
       
        
    
