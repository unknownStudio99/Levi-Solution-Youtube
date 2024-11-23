import json
import traceback
from websocket import create_connection

from .utility.executeAutox import sendExecuteAutox

# clickDesc.js 파일 수정
def modifyClickDesc(desc):
    try:
        with open("C:\\Program Files\\Laixi\\Scripts\\clickDesc.js", "w", encoding="utf-8") as file:
            file.write(f'desc("{desc}").findOne().click();\n')
    except Exception as e:
        print(f"파일 수정 중 오류 발생: {str(e)}")
        print("상세 오류:")
        print(traceback.format_exc())

# Desc 기반 버튼 클릭
def clickDesc(desc, deviceIds, ws_url):
    modifyClickDesc(desc)
    return sendExecuteAutox(deviceIds, "Scripts/clickDesc.js", ws_url)