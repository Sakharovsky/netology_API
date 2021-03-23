import requests
import pprint
from datetime import datetime

now = datetime.today().strftime('%Y-%m-%d')

def stack_posts(date_from, tag):
    url = "https://api.stackexchange.com/"
    version = "/2.2"
    questions = "/questions"
    params = {'fromdate': date_from, 'todate': now, 'tagged': tag, 'site': 'stackoverflow'}

    response = requests.get(url + version + questions, params=params)

    question_list = []

    if response.status_code // 100 == 4:
        return 'Ошибка'
    else:
        for item in response.json()['items']:
            question_list.append(item['title'])
        return question_list


pprint.pprint(stack_posts('2021-03-21', 'python'))