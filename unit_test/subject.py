import requests
import json

class TestClient(): 
    """This class will serve as a virtual 
       user that will SIGN-UP, SIGN-IN and
       DELETE ACCOUNT the the API. """

    auth_token = None

    def __init__(self, email='mock_user@testmail.com', username='mock_user', password='password', first_name='Mock', last_name='User', base_uri='http://localhost:5000'):
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.base_uri = base_uri

    def sign_up(self):
        signup_data = {
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

        res = requests.post(f'{self.base_uri}/create_account', json=signup_data)
        return res
    
    def sign_in(self):
        signin_data = {
            'email': self.email,
            'password': self.password
        }

        res = requests.post(f'{self.base_uri}/account', json=signin_data)

        res_data = res.text.replace('\'', '\"') 
        res_data = json.loads( res_data )
        self.auth_token = res_data['auth_token']    

        return res

    def update_account(self, new_data):
        user_data = {
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'new_data': new_data
        }
        
        authorization = {'Authorization': f"Bearer {self.auth_token}"}
        res = requests.put(f'{self.base_uri}/account', json=user_data, headers=authorization)

        if res.status_code == 200:
            if 'email' in new_data:
                self.email = new_data['email']
            if 'username' in new_data:
                self.username = new_data['username']
            if 'password' in new_data:
                self.password = new_data['password']
            if 'first_name' in new_data:
                self.first_name = new_data['first_name']
            if 'last_name' in new_data:
                self.last_name = new_data['last_name']

        return res

    def delete_account(self):
        del_user = {
            'email': self.email,
            'password': self.password,
            'username': self.username
        }

        authorization = {'Authorization': f"Bearer {self.auth_token}"}
        res = requests.delete(f'{self.base_uri}/account', json=del_user, headers=authorization)
        return res
    