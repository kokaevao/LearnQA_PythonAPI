import pytest
import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

@allure.epic("Registration cases")
@allure.feature("Registration")
class TestUserRegister(BaseCase):

    @allure.title("Test register user successful")
    @allure.description("This test successfully register user by prepare data")
    @allure.severity(severity_level="BLOCKER")
    def test_create_user_successfully(self):
        data = self.prepare_registrations_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.title("Test register user with existing email unsuccessful")
    @allure.description("This test doesn't register user with existing email")
    @allure.severity(severity_level="CRITICAL")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registrations_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists"

    @allure.title("Test register user with email without '@' unsuccessful")
    @allure.description("This test doesn't register user with email without '@'")
    @allure.severity(severity_level="CRITICAL")
    def test_create_user_with_incorrect_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registrations_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format"


    del_param = {
        'username',
        'firstName',
        'lastName',
        'email',
        'password'
    }

    @allure.title("Test register user with missed param (unsuccessful)")
    @allure.description("This test doesn't register user with missed param")
    @allure.severity(severity_level="NORMAL")
    @pytest.mark.parametrize("delete_param", del_param)
    def test_create_user_with_delete_parameters(self, delete_param):
        data = self.prepare_registrations_data()
        data.pop(delete_param, None)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {delete_param}"


    username = {
        "a",
        "goyuxzmhkxtcohfhftcefnlbqfvxoskpsyagcuomlglrtpsytabiwblqlbclvyjnxgizyxsxibcmzaawybsvuclaiqmobdptfsiyoztdezxckenfkpapwdyhczylpnjqatagninrcfpaeobalhhuwfiboypamyydpllzqacngsfaxwrsfuqdvydyuctuslngpfabnudiocrhzxsiqvmekarwvyeitdqfjoloysufhqehmpoohegducofhzg"

    }

    @allure.title("Test register user with different name length")
    @allure.description("This test doesn't register user with different name length")
    @allure.severity(severity_level="NORMAL")
    @pytest.mark.parametrize("name", username)
    def test_create_user_with_length_different(self, name):
        data = self.prepare_registrations_data(username=name)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)

        if len(name) > 250:
            len_text = "long"
        elif len(name) == 1:
            len_text = "short"


        assert response.content.decode("utf-8") == f"The value of 'username' field is too {len_text}"

