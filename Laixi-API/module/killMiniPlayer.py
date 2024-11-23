import json
import traceback
from websocket import create_connection

from .utility.executeAutox import sendExecuteAutox

def killMiniPlayer(deviceIds, ws_url):
    try:
        return sendExecuteAutox(deviceIds, "Scripts/killMiniPlayer.js", ws_url)
    except Exception as e:
        print(f"소형 플레이어 종료 중 오류 발생: {str(e)}")
        return False
