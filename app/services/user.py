from app.models.user import User
class UserService(object):
    def __init__(self) -> None:
        pass
    
    def users(self, id, password):
        user = User(id, password)
        print(f'아이디 : {user.id}')
        print(f'비밀번호 : {user.password}')
        print('\n')