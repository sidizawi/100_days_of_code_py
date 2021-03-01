import requests as req
import html

res = req.get(url="https://opentdb.com/api.php?amount=15&type=boolean")
res.raise_for_status()
data = res.json()['results']

question_data = []

for ques in data:
    ques['question'] = html.unescape(ques['question'])
    question_data.append(ques)
