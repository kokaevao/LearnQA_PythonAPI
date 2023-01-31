import allure
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
from lib.assertions import Assertions


@allure.epic("Deletion cases")
@allure.feature("Deletion")
class TestUserDelete(BaseCase):
    @allure.title("Test delete user with id 2 (unsuccessful)")
    @allure.description("This test doesn't delete user with id=2")
    @allure.severity(severity_level="CRITICAL")
    def test_delete_user_id2(self):
        # Login User id=2
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # Delete User id=2
        response2 = MyRequests.delete(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

        # Get User id=2

        response3 = MyRequests.get(
            f"/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response3, 200)

    @allure.title("Test delete just create user successful")
    @allure.description("This test successfully delete just create user")
    @allure.severity(severity_level="NORMAL")
    def test_create_and_delete_user(self):
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

        # DELETE
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response3, 200)

        # GET delete USER
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode("utf-8") == "User not found"

    @allure.title("Test delete user with different user authorization unsuccessful")
    @allure.description("This test doesn't delete user with different user authorization")
    @allure.severity(severity_level="NORMAL")
    def test_delete_user_by_other_authorization(self):
        # REGISTER USER1
        user1_register_data = self.prepare_registrations_data()
        response1 = MyRequests.post(
            "/user/",
            data=user1_register_data
        )

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user1_email = user1_register_data["email"]
        user1_first_name = user1_register_data["firstName"]
        user1_password = user1_register_data["password"]
        user1_user_id = self.get_json_value(response1, "id")

        # REGISTER USER2
        user2_register_data = self.prepare_registrations_data()
        response2 = MyRequests.post(
            "/user/",
            data=user2_register_data
        )

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        user2_email = user2_register_data["email"]
        user2_first_name = user2_register_data["firstName"]
        user2_password = user2_register_data["password"]
        user2_user_id = self.get_json_value(response2, "id")

        # LOGIN BY USER2
        login_data = {
            "email": user2_email,
            "password": user2_password
        }

        response3 = MyRequests.post(
            "/user/login",
            data=login_data
        )

        user2_auth_sid = self.get_cookie(response3, "auth_sid")
        user2_token = self.get_header(response3, "x-csrf-token")

        # DELETE USER1 WITH USER2 AUTHORIZATION

        response4 = MyRequests.delete(
            f"/user/{user1_user_id}",
            headers={"x-csrf-token": user2_auth_sid},
            cookies={"auth_sid": user2_token}
        )
        Assertions.assert_code_status(response4, 400)
        assert response4.content.decode("utf-8") == "Auth token not supplied"

        # LOGIN BY USER1. CHECK THAT USER1 NOT DELETED
        login_data = {
            "email": user1_email,
            "password": user1_password
        }

        response5 = MyRequests.post(
            "/user/login",
            data=login_data
        )
        Assertions.assert_code_status(response5, 200)
        Assertions.assert_json_has_key(response5, "user_id")






