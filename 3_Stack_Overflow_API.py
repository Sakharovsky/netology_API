import requests
import pprint

def stack_posts():
    url = "https://api.stackexchange.com/"
    version = "/2.2"
    questions = "/questions"
    params = {'fromdate': '2021-03-21', 'todate': '2021-03-23', 'tagged': 'python', 'site': 'stackoverflow'}

    response = requests.get(url + version + questions, params=params)

    question_list = []

    if response.status_code // 100 == 4:
        return 'Ошибка'
    else:
        for item in response.json()['items']:
            #здесь должно быть условие, объединяющее многострочные тайтлы
            question_list.append(item['title'])
        return question_list


pprint.pprint(stack_posts())