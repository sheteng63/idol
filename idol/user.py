import requests
from django.http import HttpResponse
import logging

from requests import Response

from idol import settings

logger = logging.getLogger(__name__)
def login(req):
    logger.info(req.GET)
    print(req.GET)
    return HttpResponse("success")

def request_access_token(code):
    appid = settings.WX_APPID
    secret: str = settings.WX_SECRET
    api: str = f"https://api.weixin.qq.com/sns/oauth2/access_token?appid={appid}&secret={secret}&code={code}&grant_type=authorization_code"
    r: Response = requests.get(api)
    return r.json()