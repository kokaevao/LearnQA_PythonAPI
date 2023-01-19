import requests

class TestCheckHeader:
    def test_check_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)

        assert 'Date' in response.headers, f"'Date' not in headers"
        assert 'Content-Type' in response.headers, f"'Content-Type' not in headers"
        assert 'Content-Length' in response.headers, f"'Content-Length' not in headers"
        assert 'Connection' in response.headers, f"'Connection' not in headers"
        assert 'Keep-Alive' in response.headers, f"'Keep-Alive' not in headers"
        assert 'Server' in response.headers, f"'Server' not in headers"
        assert 'x-secret-homework-header' in response.headers, f"'x-secret-homework-header' not in headers"
        assert 'Cache-Control' in response.headers, f"'Cache-Control' not in headers"
        assert 'Expires' in response.headers, f"'Expires' not in headers"
