import json
import traceback
from websocket import create_connection

def getAllDeviceList(ws_url):
    return json.dumps({
        "action": "List",
    })

def sendAllDeviceList(ws_url):
    try:
        ws = create_connection(ws_url)
        message = getAllDeviceList(ws_url)
        ws.send(message)
        result = ws.recv()
        ws.close()
        return result
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        print("상세 오류:")
        print(traceback.format_exc())
        return None
    
def printAllDeviceList(result):
    try:
        parsed_response = json.loads(result)
        devices = json.loads(parsed_response["result"])

        print("-" * 20) 
        for device in devices:
            print(f"Device ID: {device['deviceId']}")
            print(f"Number: {device['no']}")
            print(f"Name: {device['name']}")
            print(f"Is OTG: {device['isOtg']}")
            print(f"Is Cloud: {device['isCloud']}")
            print(f"Group IDs: {device['groupIds']}")
            print("-" * 20)
            
    except json.JSONDecodeError as e:
        print(f"JSON 디코딩 오류: {str(e)}")
