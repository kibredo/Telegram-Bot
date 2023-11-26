from data import schedule
from data import SECRET_TOKEN
from data import API_URL
from data import UTC_OFFSET
from data import URL
from data import HEADER
from data import DATA
from datetime import datetime
import http.client
import queue
import time
import requests

def send_to_telegram(id, command):
    ans = str()

    if command == "/getmonday":
        ans = "Monday"

    elif command == "/getthuesday":
        ans = "Thuesday"

    elif command == "/getwednesday":
        ans = "Wednesday"
        
    elif command == "/getthursday":
        ans = "Thursday"

    elif command == "/getfriday":
        ans = "Friday"

    elif command == "/start":
        ans = "Start"

    else:
        final = str()
        current = datetime.today().weekday()

        match current:
            case 0:
                final = "Monday"

            case 1:
                final = "Thuesday"

            case 2:
                final = "Wednesday"

            case 3:
                final =  "Thursday"

            case 4:
                final = "Friday"

            case 5:
                final = "FreeDay"

            case 6:
                final = "FreeDay"

        ans = final

    t = DATA.replace('message', schedule[ans])
    t = t.replace('ID', id)
    t_header = dict(HEADER)
    httpscon = http.client.HTTPSConnection('api.telegram.org')
    t_header['Connection'] = 'close'
    httpscon.request('POST', URL, t.encode('utf-8'), t_header)
    httpscon.getresponse().read().decode()
    httpscon.close()
