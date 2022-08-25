import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.login import LoginService

def print_menu():
    print("0. 전체프로그램 종료")
    print("1. 계산기 프로그램")
    print("2. 로그인 프로그램")     # 입력받은 아이디와 비번 콘솔에 출력하기
    menu = input('메뉴 선택')
    return menu
    
def main():
    # print_menu()                            # expression(표현식) 메소드 -> 종류 2개
    # calculatorService = CalculatorService() # 변수 -> 2개(전역/지역변수)
    while 1:                                  # statement(문) 메소드 -> 종류 2개(조건/반복문)
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
            loginService = LoginService()
            first = str(input('아이디 입력 : '))
            second = str(input('비밀번호 입력: '))
            loginService.login(first, second)   # .이 있으면 메소드(.이 없으면 함수)
            
if __name__ == '__main__':
    main()
    