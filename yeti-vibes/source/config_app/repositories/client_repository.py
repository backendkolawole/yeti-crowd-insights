# config_app/repositories/user_repository.py
from config_app.models import Client as ClientModel
from config_app.domain_models.client import Client
from rest_framework.exceptions import NotFound


class ClientRepository:
    # def create_client(self, data):
    #     print(data)
    #     client = ClientModel(**data)
    #     client.save()
    #     return client

    def create_client(self, data):
        client = ClientModel(**data)  # Create client without email
        client.set_password(data['password'])  # Hash the password
        client.save()
        return client

    def get_all_clients(self):
        clients = ClientModel.objects.all()

        return clients

    def get_client(self, client_id):
        try:
            client = ClientModel.objects.get(id=client_id)
        except ClientModel.DoesNotExist:
            raise NotFound("User not found")

        return client

    def update_client(self, client_id, data):
        try:
            client = ClientModel.objects.get(pk=client_id)
        except ClientModel.DoesNotExist:
            raise NotFound("User not found")
        for key, value in data.items():
            setattr(client, key, value)
        client.save()
        return client

    def delete_client(self, client_id):
        try:
            client = ClientModel.objects.get(pk=client_id)
        except ClientModel.DoesNotExist:
            raise NotFound("User not found")
        client.delete()
        return {"success": True}

    def get_client_account(self, client):
        try:
            client = ClientModel.objects.get(client=client)
        except ClientModel.DoesNotExist:
            raise NotFound("Account not found")

        return client
