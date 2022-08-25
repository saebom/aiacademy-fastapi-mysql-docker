class Login(object):
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
    
    def id_view(self):
        return print(self.id)
    
    def pw_view(self):
        return print(self.pw)