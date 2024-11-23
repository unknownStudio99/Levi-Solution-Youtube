from websocket import create_connection
import json

def executeAdbCommand(command, device_id, ws_url=None):
    """
    ADB 명령어를 직접 실행하는 함수
    
    Args:
        command (str): 실행할 ADB 명령어
        device_id (str): 대상 기기 ID
        ws_url (str): 사용하지 않음 (이전 버전과의 호환성을 위해 유지)
    """
    ws = create_connection(ws_url)
    
    command_payload = {
        "action": "adb",
        "comm": {
            "command": command,
            "deviceIds": device_id
        }
    }
    
    ws.send(json.dumps(command_payload))
    result = ws.recv()
    ws.close()
    
    return json.loads(result)
