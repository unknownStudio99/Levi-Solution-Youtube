from module.utility.executeAdb import executeAdbCommand

def sendKeyEvent(keycode, device_id, ws_url):
    """
    ADB를 통해 키코드를 전송하는 함수
    
    Args:
        keycode (int): Android 키코드 값
        device_id (str): 대상 기기 ID
        ws_url (str): WebSocket 서버 URL
    """
    command = f"input keyevent {keycode}"
    executeAdbCommand(command, device_id, ws_url)