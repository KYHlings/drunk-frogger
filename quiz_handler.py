import requests


def get_quiz():
    url = requests.get("https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda")
    content = url.json()["questions"]
    return content

def quiz():
    q_prompt= "Är T.O.A.D's bäst?"
    q_ans = ["y","n"]
    return  q_prompt, q_ans