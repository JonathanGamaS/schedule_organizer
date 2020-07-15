import requests
import json
import calendar
import time
from datetime import datetime
import pytz


def execute_orchestrator_programming():
    programacao_atual = "Init"
    programacao_total = globo_get_endpoint()
    horario = get_time_now()
    for programacao in programacao_total["programme"]["entries"]:
        horario_inicial = programacao["start_time"]
        horario_final = programacao["end_time"]
        if horario_inicial <= horario <= horario_final:
            programacao_atual = {
                "titulo" : programacao["title"],
                "descricao": programacao["description"]
            }
    return programacao_atual


def globo_get_endpoint():
    data = get_date()
    url = f"https://epg-api.video.globo.com/programmes/1337?date={data}"
    response = requests.get(url=url)
    data = json.loads(response.content)
    return data


def get_time_now():
    time_stamp = calendar.timegm(time.gmtime())
    return time_stamp

def get_date():
    tz_SP = pytz.timezone('America/Sao_Paulo')
    time_sp = datetime.now(tz_SP)
    time = time_sp.strftime("%Y-%m-%d")
    return time


# execute_orchestrator_programming()