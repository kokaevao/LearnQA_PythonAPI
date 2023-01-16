import requests
import json
import time


response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
pars_json = json.loads(response1.text)
pars_token = pars_json["token"]
pars_time = pars_json["seconds"]
print(pars_token)
print(pars_time)


response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": pars_token})
get_status = response2.text
pars_status = json.loads(get_status)

key = list(pars_status.keys())
status_job = pars_status[key[0]]
if status_job == "Job is NOT ready":
    time.sleep(pars_time+2)
    response_token1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": pars_token})
    get_status1 = response_token1.text
    pars_status_job = json.loads(get_status1)
    result = int(pars_status_job["result"])
    status_job1 = pars_status_job["status"]
    if status_job1 == "Job is ready" and result is not None:
        print(status_job1, "result is", result)
else:
    print("No job associated with this token")