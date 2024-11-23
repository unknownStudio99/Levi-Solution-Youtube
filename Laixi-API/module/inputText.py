import json
import traceback
from websocket import create_connection

from .utility.executeAutox import sendExecuteAutox

def modifyInputText(text):
    try:
        with open("C:\\Program Files\\Laixi\\Scripts\\inputText.js", "w", encoding="utf-8") as file:
            file.write(f'setText("{text}");')
    except Exception as e:
        print(f"파일 수정 중 오류 발생: {str(e)}")

def inputText(text, deviceIds, ws_url):
    modifyInputText(text)
    return sendExecuteAutox(deviceIds, "Scripts/inputText.js", ws_url)
