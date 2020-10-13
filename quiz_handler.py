import requests


def get_quiz():
    url = requests.get("https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda")
    content = url.json()["questions"]
    return content

def quiz():
    q_ls = ["Är T.O.A.D's bäst?"]
    q_ans = "y"
    return  q_ls, q_ans