from app.models.login import Login
class LoginService(object):
    def __init__(self) -> None:
        pass
    
    def login(self, id, pw):
        login = Login(id, pw)
        print(f'아이디 확인 : {login.id}')
        print(f'비밀번호 확인 : {login.pw}')
