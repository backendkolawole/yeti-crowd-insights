from config_app.repositories.client_repository import ClientRepository

class ClientUseCase:
    def __init__(self, repository: ClientRepository):
        self.repository = repository

    def create_client(self, data):
        return self.repository.create_client(data=data)
    
    def get_all_clients(self):
        return self.repository.get_all_clients()

    def get_client(self, client_id):
        return self.repository.get_client(client_id = client_id)

    def update_client(self, client_id, data):
        return self.repository.update_client(client_id=client_id, data=data)

    def delete_client(self, client_id):
        return self.repository.delete_client(client_id=client_id)
    
    
    
