import requests


def response_check(url):
    r = requests.get(url)

    if r.status_code == 200:
        try:
            return {'status': 'ok', 'data': r.json()}
        except Exception:
            return {'status': 'parsing error', 'data': None}
    elif r.status_code == 404:
        return {'status': 'maintenance', 'data': None}
    else:
        return {'status': 'error', 'data': None}
