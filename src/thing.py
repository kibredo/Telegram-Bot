from datetime import datetime
import http.client
import json

from src.data import DATA
from src.data import HEADER
from src.data import schedule
from src.data import URL

updates = dict()
def send_to_telegram(id, command):
    ans = str()

    if command == "/getmonday":
        ans = "Monday"

    elif command == "/gettuesday":
        ans = "Thuesday"

    elif command == "/getwednesday":
        ans = "Wednesday"

    elif command == "/getthursday":
        ans = "Thursday"

    elif command == "/getfriday":
        ans = "Friday"

    elif command == "/start":
        ans = "Start"

    elif command == "/help":
        ans = "Help"
    elif command[7:9] == "mo":
        ans = "cMonday"
    elif command[7:9] == "tu":
        ans = "cThuesday"
    elif command[7:9] == "we":
        ans = "cWednesday"
    elif command[7:9] == "th":
        ans = "cThursday"
    elif command[7:9] == "fr":
        ans = "cFriday"
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

    if ans[0] != 'c':
        t = DATA.replace('message', schedule[ans])
        t = t.replace('ID', id)

    else:
        arr = command.splitlines()
        final_string = str()
        final_string = '\n'.join(arr[1:])
        schedule[ans[1:]] = final_string
        final = "ready\n"
        t = DATA.replace('message', schedule[ans[1:]])
        t = t.replace('ID', id)
            

    t_header = dict(HEADER)
    httpscon = http.client.HTTPSConnection('api.telegram.org')
    t_header['Connection'] = 'close'
    httpscon.request('POST', URL, t.encode('utf-8'), t_header)
    httpscon.getresponse().read().decode()
    httpscon.close()
