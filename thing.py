from data import SECRET_TOKEN
from data import API_URL
from utils import send_to_telegram
import queue
import time
import requests

updates = dict()
timeout = 60
offset = -2
message_queue = queue.Queue()


def safename(name):
	result = name.replace('\'', '\\\'').replace('\"', '\\\"').replace('\\', '\\\\')
	return result


while True:
    time.sleep(1)
    start_time = time.time()
    updates = requests.get(f'{API_URL}{SECRET_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:

        command = str(updates['result'][0]['message']['text'])
        id = str(updates['result'][0]['message']['from']['id'])
        send_to_telegram(id, command)
        
        for result in updates['result']:
            offset = result['update_id']
            

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')