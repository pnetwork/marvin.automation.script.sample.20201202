import requests
from blcks import blcks


MY_FAAS_METHOD_NAME = "blcksrequests"
DEFAULT_URL = "http://ifconfig.io"
DEFAULT_ITEM = "IP Address"


@blcks
def main(event, context):
    pass


@blcks.script(MY_FAAS_METHOD_NAME)
def process():
    res = requests.get(DEFAULT_URL)
    lines = res.content.decode('utf8').split('\n')
    ip = "Not Found"
    for line in lines:
        if DEFAULT_ITEM in line:
            ip = remove_html_tags(line).strip().replace(DEFAULT_ITEM, "")
            break
    return {"result": ip}


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
