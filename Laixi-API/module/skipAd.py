import json
import traceback
from websocket import create_connection

from .utility.executeAutox import sendExecuteAutox

def skipAd(deviceIds, ws_url):
    try:
        return sendExecuteAutox(deviceIds, "Scripts/skipAd.js", ws_url)
    except Exception as e:
        print(f"광고 건너뛰기 중 오류 발생: {str(e)}")
        return False
