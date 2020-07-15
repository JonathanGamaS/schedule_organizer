import requests
import json
import calendar
import time

def execute_orchestrator_programming():
    programacao_total = globo_get_endpoint()
    horario = get_time_now()
    for programacao in programacao_total["programme"]["entries"]:
        if programacao["start_time"] == horario:
            programacao_atual = {
                "titulo" : programacao["title"],
                "descricao": programacao["description"]
            }
    return programacao_atual


def globo_get_endpoint():
    data = "2020-07-14"
    url = f"https://epg-api.video.globo.com/programmes/1337?date={data}"
    response = requests.get(url=url)
    data = json.loads(response.content)
    return data


def get_time_now():
    time_stamp = calendar.timegm(time.gmtime())
    return time_stamp

execute_orchestrator_programming()