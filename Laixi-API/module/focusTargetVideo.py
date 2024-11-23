import json
import traceback
from websocket import create_connection
from .utility.executeAutox import sendExecuteAutox
from .utility.sleepDummy import sleepDummyMs

def modifyFocusTargetVideo(title):
    try:
        js_content = f'''var i = true;
var targetTitle = "{title}";

while (i) {{
    var isUiText = textContains(targetTitle).findOnce();

    if (isUiText != null) {{
        sleep(random(500, 1500))
        i = false;
        toast("타겟을 찾았습니다.");
    }} else {{
        scrollDown();
        sleep(random(500, 1500))
    }}
}}'''
        
        with open("C:\\Program Files\\Laixi\\Scripts\\focusTargetVideo.js", "w", encoding="utf-8") as file:
            file.write(js_content)
    except Exception as e:
        print(f"파일 수정 중 오류 발생: {str(e)}")
        raise

def focusTargetVideo(title, deviceIds, ws_url, device_manager):
    try:
        # 현재 상태를 "타겟 영상 검색 중"으로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("타겟 영상 검색 중")
        else:
            device_manager.update_device_action(deviceIds, "타겟 영상 검색 중")
            
        # 스크립트 파일 수정
        modifyFocusTargetVideo(title)
        
        # 스크립트 실행
        result = sendExecuteAutox(deviceIds, "Scripts/focusTargetVideo.js", ws_url)
        
        # 충분한 시간 대기 (15~20초)
        sleepDummyMs(15000, 20000)
        
        # 상태 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("타겟 영상 검색 완료")
        else:
            device_manager.update_device_action(deviceIds, "타겟 영상 검색 완료")
        
        return True
        
    except Exception as e:
        print(f"타겟 영상 검색 중 오류 발생: {str(e)}")
        if deviceIds == "all":
            device_manager.update_all_devices_action("타겟 영상 검색 실패")
        else:
            device_manager.update_device_action(deviceIds, "타겟 영상 검색 실패")
        return False
