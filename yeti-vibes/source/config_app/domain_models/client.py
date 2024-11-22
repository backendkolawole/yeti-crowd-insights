class Client:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        
    def __str__(self):
        return self.client_name