class Client:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
        
    def __str__(self):
        return self.client_name