import requests
import pytest


class TestUserCheck:
    heads = [
        (
        "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mobile", "No", "Android"),
        (
        "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "Mobile", "Chrome", "iOS"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "Googlebot", "Unknown", "Unknown"),
        (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "Web", "Chrome", "No"),
        (
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "Mobile", "No", "iPhone")
    ]

    @pytest.mark.parametrize('req1, res1, res2, res3', heads)
    def test_user_check(self, req1, res1, res2, res3):
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent":req1})
        response_dict = response.json()
        assert response_dict['platform'] == res1, f"Значение поля 'platform'= {response_dict['platform']}, ожидаем:{res1}"
        assert response_dict['browser'] == res2, f"Значение поля 'browser'= {response_dict['browser']}, ожидаем:{res2}"
        assert response_dict['device'] == res3, f"Значение поля 'device'= {response_dict['device']}, ожидаем:{res3}"



