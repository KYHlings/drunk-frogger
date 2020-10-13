import requests
from random import shuffle
from pathlib import Path
import json
def get_quiz():
    p = Path("quiz.json")
    #url = requests.get("https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda")
    content = json.loads(p.read_text(encoding='utf8'))['questions']
    shuffle(content)
    return content

def quiz():
    quiz_content=get_quiz()
    for q in quiz_content:
        return q["prompt"],q["rightAnswer"],q["wrongAnswers"]





