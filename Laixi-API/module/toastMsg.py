import json
import traceback
from websocket import create_connection

def toastMsg(msg, deviceIds):
    return json.dumps({
        "action": "Toast",
        "comm": {
            "deviceIds": deviceIds,
            "content": msg,
        }
    })

def sendToastMsg(msg, deviceIds, ws_url):
    try:
        print("WebSocket 연결 시도 중...")
        ws = create_connection(ws_url)
        print("연결 성공!")
        
        # toastMsg 함수를 사용하여 메시지 생성
        message = toastMsg(msg, deviceIds)
        
        print("메시지 전송 중...")
        ws.send(message)  # 이미 JSON 문자열로 변환된 상태
        result = ws.recv()
        print("서버 응답:", result)
        ws.close()
        
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        print("상세 오류:")
        print(traceback.format_exc())