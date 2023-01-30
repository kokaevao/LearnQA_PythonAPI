
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_create_user(self):
        # REGISTER
        register_data = self.prepare_registrations_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")


        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")


        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            cookies={"auth_sid": auth_sid},
            headers={"x-csrf-token": token},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)


        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            cookies={"auth_sid": auth_sid},
            headers={"x-csrf-token": token}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )


    def test_edit_created_user_without_authorization(self):
        # REGISTER
        register_data = self.prepare_registrations_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")


        # EDIT
        new_name = "Changed Name"

        response2 = MyRequests.put(
            f"/user/{user_id}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Auth token not supplied"



    def test_edit_user_by_other_authorization(self):
        # Login User 1
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # Create User 2
        reg_data = self.prepare_registrations_data()
        response2 = MyRequests.post("/user/", data=reg_data)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")
        user_id_from_auth_method = self.get_json_value(response2, "id")

        # Edit User 2 with token and auth_sid User 1
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id_from_auth_method}",
            cookies={"auth_sid": auth_sid},
            headers={"x-csrf-token": token},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == "Please, do not edit test users with ID 1, 2, 3, 4 or 5."


    def test_edit_created_user_without_symbol_mail(self):
        # REGISTER
        register_data = self.prepare_registrations_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")


        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")


        # EDIT
        new_mail = "learnqa.mail.ru"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            cookies={"auth_sid": auth_sid},
            headers={"x-csrf-token": token},
            data={"mail": new_mail}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == "No data to update"

    def test_edit_created_user_with_incorrect_data(self):
        # REGISTER
        register_data = self.prepare_registrations_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "d"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            cookies={"auth_sid": auth_sid},
            headers={"x-csrf-token": token},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == '{"error":"Too short value for field firstName"}'











