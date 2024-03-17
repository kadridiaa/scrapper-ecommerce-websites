import requests
import json
import sys
import time

import pymysql


headers = {
    'authority': 'www.bershka.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'referer': 'https://www.bershka.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
}

params = {
    'productIds': '151697753,151697754,152605125,152611506,152857343,152954386,153280973,153280974,154122456,149434967,149434968,149434995,149434996,149434997,149435005,149435006,149435007,149435008,149435110,149435111,149435112,149435201,149435202,149435240,149435241,149435242,149435261,149435262,149435263,149435264,149435281,149435282',
    'languageId': '-2',
}



response = requests.get(
    'https://www.bershka.com/itxrest/3/catalog/store/45009589/40259544/productsArray',
    params=params,
    headers=headers,
)