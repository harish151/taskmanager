import requests
from databases import extract_username
def sentmail(task,date,time,email):
    name = extract_username(email)
    url = "https://mail-sender-api1.p.rapidapi.com/"
    content = f"Dear {name}, Your Task '{task}' is completed in {date} at {time}"
    payload = {
        "sendto": email,
        "name": "PersonalTaskManger Team",
        "replyTo": "hr2946352@gmail.com",
        "ishtml": "false",
        "title": "Task Completion Notification",
        "body": content
    }
    headers = {
        "x-rapidapi-key": "a576603aa2msh6e3b4855bc70b31p1c5001jsnb2573c21c4ed",
        "x-rapidapi-host": "mail-sender-api1.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())
    return response.json()
