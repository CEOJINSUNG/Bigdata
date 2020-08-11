import sys
import requests
import base64
import json
import logging

#중간에 에러가 발생하면 status_code가 바뀌고 에러가 생긴다.
#점검하기 위해서는 print(r.status_code)를 치면 알 수 있다.
client_id="spotity for develooper에서 받은 키값"
client_secret="spotity for develooper에서 받은 키값"

def main():
    headers = get_headers(client_id, client_secret)

    params = {
        "q": "BTS",
        "type": "artist"
    }

    r = requests.get("https://api.spotify.com/v1/searct", params=params, headers=headers)

    #오류 핸들링하기
    #try를 해라 안됐을 경우 except를 실행해라
    try:
        r = requests.get("https://api.spotify.com/v1/searct", params=params, headers=headers)

    except:
        logging.error(r.text)
        sys.exit(1)

    r = requests.get("https://api.spotify.com/v1/searct", params=params, headers=headers)

    if r.status_code != 200:
        logging.error(json.loads(r.text))

        if r.status_code == 429:
            retry_after = json.loads(r.headers)['Retry-After']
            time.sleep(int(retry_after))

            r = requests.get("https://api.spotify.com/v1/searct", params=params, headers=headers)

        elif r.status_code == 401:
            headers = get_headers(client_id, client_secret)
            r = requests.get("https://api.spotify.com/v1/searct", params=params, headers=headers)

        else:
            sys.exit(1)
        #paging object 관련하여
        r  = requests.get("https://api,spotify,com/v1/artists/ID값/albums", headers=headers)

        raw = json.loads(r.text)

        total = raw['total']
        offset = raw['offset']
        limit = raw['limit']
        next = raw['next']

        albums = []
        print(len(raw['item']))
        albums.extend(raw['items'])

        count = 0
        while count < 100 and next:
            r = requests.get(raw['next'], headers=headers)
            raw = json.loads(r.text)
            next = raw['next']

            albums.extend(raw['items'])
            count = len(albums)

        print(len(albums))


def get_headers(client_id, client_secret):
    endpoint ="https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

    headers= {
        "Authorization": 'Basic {}'.format(encoded)
    }

    playload = {
        "grant_type": "client_credentials"
    }

    r = requests.post(endpoint, data=payload, headers=headers)

    ##sys.exit(0) 위 코드가 잘 작동 되면 아무 문제없이  exit 함.
    #r 이 str 형식인데 밑에 있는 것처럼  loads(r.text) 하면 dic 형태로 바뀜
    access_token = json.loads(r.text)['access_token']

    headers = {
        "Authorization": "Bearer {}".format(access_token)
    }

    return headers

if __name__=='__main__':
    main()
