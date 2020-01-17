from subject import TestClient
from datetime import datetime
import requests
import unittest
import json

class TestLoginService(unittest.TestCase):
    """ TestLoginService classwill interact with 
        the /account endpoint following the CRUD
        interactions available:
            - Create Account.
            - Issue a token (sign in).
            - Update account data.
            - Remove account from API. """

    @classmethod
    def setUpClass(cls):
        cls.test_user = TestClient()
        cls.signup = cls.test_user.sign_up()
        cls.signin = cls.test_user.sign_in()
        print('[ setUpClass ] - MockUser Account Created - {}'.format(datetime.now()))
    
    @classmethod
    def tearDownClass(cls):
        cls.del_account = cls.test_user.delete_account()
        print('[ tearDownClass ] - MockUser Account Removed - {}'.format(datetime.now()))

    def test_signup_response(self):
        """ After SIGN UP the TestClient, check 
            body response be same as actual TestClient
            data. """
        signup_data = self.signup.text.replace('\'', '\"')
        signup_data = json.loads( signup_data )

        self.assertEqual( self.signup.status_code, 201)
        self.assertEqual( signup_data['email'], self.test_user.email)
        self.assertEqual( signup_data['username'], self.test_user.username)
        self.assertEqual( signup_data['first_name'], self.test_user.first_name)
        self.assertEqual( signup_data['last_name'], self.test_user.last_name)
        self.assertEqual( signup_data['last_name'], self.test_user.last_name)

    def test_signin_response(self):
        """ TestClient will be SIGNED IN and 
            will generate an Authentication 
            token used to UPDATE and DELETE 
            the account. """ 
        signin_data = self.signin.text.replace('\'', '\"')
        signin_data = json.loads( signin_data )

        self.assertEqual(self.signin.status_code, 200)
        self.assertIsNotNone(self.test_user.auth_token)

    def test_update_account(self):
        """ New data will be injected to 
            the registered user. """
        new_username = 'EDITED_USERNAME_99'
        new_email = 'EDITED_EMAIL_99@bluetrailsoft.com'
        new_first_name = 'Albus Percival Wulfric Brian Dumbledore'

        # UPDATE REQUEST
        update = self.test_user.update_account({ 'username': new_username, 'email': new_email, 'first_name': new_first_name })    
        update_res = update.text.replace('\'', '\"')
        update_res = json.loads( update_res )

        self.assertEqual(update.status_code, 200)
        self.assertEqual(update_res['username'], new_username)
        self.assertEqual(update_res['email'], new_email)
        self.assertEqual(update_res['first_name'], new_first_name)

    def test_fail_to_update_existing_account(self):
        """ Here will be issued a new TestClient user
            and will update the previous subject to check
            error message if updates are applied to an 
            already owned account. """

        owned_email = 'ALREADY_OWNED_ACCOUNT@email.com'
        owned_userame = 'ALREADY_OWNED_USERNAME'
        # New TestClient registry
        new_registry = TestClient(email=owned_email, username=owned_userame)
        new_signup = new_registry.sign_up()
        new_signin = new_registry.sign_in()

        self.assertEqual(new_signup.status_code, 201)
        self.assertEqual(new_signin.status_code, 200)
        self.assertIsNotNone(new_registry.auth_token)

        # UPDATING EXISTING TestClient user.
        new_update = self.test_user.update_account({ 'email': owned_email, 'username': owned_userame })    
        new_update_res = new_update.text

        self.assertEqual(new_update.status_code, 400)
        self.assertIn('TRANSACTION_ERROR', new_update_res)
        self.assertIn('Duplicate entry', new_update_res)

        with self.subTest('DELETE THE SECONDARY ACCOUNT REGISTERED'):
            new_registry.delete_account()
