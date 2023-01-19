import requests


class TestCheckCookie:
    def test_check_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(response.cookies))
        value_cookie = response.cookies.get('HomeWork')
        print(value_cookie)
        assert 'HomeWork' in response.cookies, f"Cookies not in response"
