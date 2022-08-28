import os
import sys
from icecream import ic
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.score import ScoreService
from app.services.grade import GradeService
from app.services.pandas_quiz import PandasQuiz

def print_menu():
    print("0. 전체프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램")     # 입력받은 아이디와 비번 콘솔에 출력하기
    print("3. 성적표 프로그램")     
    print("4. 판다스 퀴즈 풀기")
    menu = input('메뉴 선택')
    return menu

def main():
    # print_menu()                            # expression(표현식) 메소드 -> 종류 2개
    # calculatorService = CalculatorService() # 수 (변수 -> 2개 : 전역/지역변수 -> self가 있는지 없는지)

    while 1:                                  # statement(문) 메소드 -> 종류 2개(조건/반복문) : 
        menu = print_menu()
        if menu == '0':
            print('전체 프로그램을 종료합니다')
            break
        
        elif menu == '1':
            calculatorService = CalculatorService()
            first = int(input('첫번째 값 입력: '))
            second = int(input('두번째 값 입력: '))
            calculatorService.calculate(first, second)   # .이 있으면 메소드(.이 없으면 함수)

        elif menu == '2':
            userService = UserService()
            id = str(input('아이디 입력 : '))
            password = str(input('비밀번호 입력 : '))
            userService.users(id, password)
        
        elif menu == '3':
            scoreService = ScoreService()
            # gradeService = GradeService()
            name = str(input('이름 입력 : '))
            korean = int(input('국어 성적 입력 : '))
            english = int(input('영어 성적 입력 : '))
            math = int(input('수학 성적 입력 : '))
            score = scoreService.get_score(name, korean, english, math)   
            # grade = gradeService.get_grade(name, korean, english, math)   
            print(f'이름 : {name} 학점 : {score}')
            # print(f'이름 : {name} 학점 : {grade}')
            
        elif menu == '4':
            quiz = PandasQuiz()
            while 1:
                quiz_number = input('퀴즈번호 선택. 종료는 0 : ')
                if quiz_number == '0':
                    print('프로그램을 종료합니다.')
                    break
                elif quiz_number == '1':
                    quiz.quiz1()                    
                elif quiz_number == '2': 
                    quiz.quiz2()   
                elif quiz_number == '3': 
                    quiz.quiz3()      
                    
if __name__ == '__main__':
    main()
    