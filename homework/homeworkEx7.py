import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response1.status_code)
print(response1.text)

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response2.status_code)
print(response2.text)

response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"PUT"})

print(response3.status_code)
print(response3.text)

methods = ["GET", "POST", "PUT", "DELETE"]

for method in methods:
    for req in methods:
        if req == "GET":
            response4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': method})
            print(f"Запрос {req}, с методом {method}, вернул статус код {response4.status_code}")
            print(f"Текст ответа {response4.text}")
            if req != method and response4.text == '{"success":"!"}':
                print(f"Тип запроса не совпадает со значением параметра: параметр {req} и тип запроса {method} возвращает успешный результат")
        elif req == "POST":
            response4 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Запрос {req}, с методом {method}, вернул статус код {response4.status_code}")
            print(f"Текст ответа {response4.text}")
            if req != method and response4.text == '{"success":"!"}':
                print(f"Тип запроса не совпадает со значением параметра: параметр {req} и тип запроса {method} возвращает успешный результат")
        elif req == "PUT":
            response4 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Запрос {req}, с методом {method}, вернул статус код {response4.status_code}")
            print(f"Текст ответа {response4.text}")
            if req != method and response4.text == '{"success":"!"}':
                print(f"Тип запроса не совпадает со значением параметра: параметр {req} и тип запроса {method} возвращает успешный результат")
        elif req == "DELETE":
            response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Запрос {req}, с методом {method}, вернул статус код {response4.status_code}")
            print(f"Текст ответа {response4.text}")
            if req != method and response4.text == '{"success":"!"}':
                print(f"Тип запроса не совпадает со значением параметра: параметр {req} и тип запроса {method} возвращает успешный результат")