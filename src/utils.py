from datetime import datetime
import http.client

from src.data import DATA
from src.data import HEADER
from src.data import schedule
from src.data import URL


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

    elif command == "/help":
        ans = "Help"

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
