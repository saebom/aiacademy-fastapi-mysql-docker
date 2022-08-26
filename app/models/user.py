class User(object):
    def __init__(self, id, password):
        self.id = id
        self.password = password
        
    def id_view(self):
        return print(self.id)
    
    def pw_view(self):
        return print(self.password)
    
    