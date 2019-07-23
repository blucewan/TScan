# -*- coding:utf-8 -*-

import requests
import json
import re

header = {
    'Host': 'api.webscan.cc',
    'Origin': 'http://webscan.cc',
    'Pragma': 'no-cache',
    'Referer': 'http://webscan.cc/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132'
}


def get_side_info(ip):
    """
    获取旁站信息
    :param ip:
    :return:
    """
    api_url = 'http://api.webscan.cc/'
    query_data = {
        'action': 'query',
        'ip': ip
    }
    try:
        html = requests.post(api_url, data=query_data, headers=header, timeout=8)
        text = html.text

        if text.startswith(u'\ufeff'):
            text = text.encode('utf8')[3:].decode('utf8')
        print(text)
        if text.find('null') > -1:
            print('[LogError WebSide]: ', 'The webside info is null')
            return False
        else:
            return json.loads(text)
    except Exception as e:
        print('[logError GetSideInfo]: ', e)
        return False