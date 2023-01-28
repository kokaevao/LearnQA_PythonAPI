import json.decoder
from datetime import datetime
from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response:Response, headers_name):
        assert headers_name in response.headers, f"Cannot find header with the name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response:Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is nor JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON does mot have key '{name}'"
        return response_as_dict[name]

    def prepare_registrations_data(self, email=None, password=None, username=None, firstname=None, lastname=None):
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            email = f"{base_part}{random_part}@{domain}"
        if password is None:
            password = '123'
        if username is None:
            username = f"Username{random_part}"
        if firstname is None:
            firstname = f"Firstname{random_part}"
        if lastname is None:
            lastname = f"Lastname{random_part}"
        return {
            'password': password,
            'username': username,
            'firstName': firstname,
            'lastName': lastname,
            'email': email
        }


