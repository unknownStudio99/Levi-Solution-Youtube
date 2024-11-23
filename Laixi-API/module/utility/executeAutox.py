import json
import traceback
from websocket import create_connection

def executeAutox(deviceIds, script, ws_url):
    return json.dumps({
        "action": "ExecuteAutoJs",
        "comm": {
            "deviceIds": deviceIds,
            "filePath": script,
        }
    })

def sendExecuteAutox(deviceIds, script, ws_url):
    try:
        ws = create_connection(ws_url)
        message = executeAutox(deviceIds, script, ws_url)
        ws.send(message)
        result = ws.recv()
        ws.close()
        return result
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        print("상세 오류:")
        print(traceback.format_exc())
        return None
