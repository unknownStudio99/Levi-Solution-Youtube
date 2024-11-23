import json
import traceback
from websocket import create_connection

from .utility.executeAutox import sendExecuteAutox

def modifyClickText(text):
    try:
        with open("C:\\Program Files\\Laixi\\Scripts\\clickText.js", "w", encoding="utf-8") as file:
            file.write(f'click("{text}");')
    except Exception as e:
        print(f"파일 수정 중 오류 발생: {str(e)}")
        print("상세 오류:")
        print(traceback.format_exc())

# Text 기반 버튼 클릭
def clickText(text, deviceIds, ws_url):
    modifyClickText(text)
    return sendExecuteAutox(deviceIds, "Scripts/clickText.js", ws_url)