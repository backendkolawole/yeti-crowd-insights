# config_app/repositories/user_repository.py
from django.contrib.auth.models import User
from config_app.domain_models.client import Client
from rest_framework.exceptions import NotFound



class ClientRepository:
    def create_client(self, data):
        client = User(**data)
        client.save()
        return Client(id=client.id, username=client.username, email=client.email)
    
    def get_all_clients(self):
        clients = User.objects.all()
    
        return [Client(id=client.id, username=client.username, email=client.email) for client in clients]

    def get_client(self, client_id):
        try:
            client = User.objects.get(id=client_id)
        except User.DoesNotExist:
            raise NotFound("User not found")
            
        return client


    def update_client(self, client_id, data):
        try:
            client = User.objects.get(pk=client_id)
        except User.DoesNotExist:
            raise NotFound("User not found")
        print(data)
        for key, value in data.items():
            setattr(client, key, value)
        client.save()
        return Client(id=client.id, username=client.username, email=client.email)

    def delete_client(self, client_id):
        try:
            client = User.objects.get(pk=client_id)
        except User.DoesNotExist:
            raise NotFound("User not found")
        client.delete()
        return {"success": True}
    
