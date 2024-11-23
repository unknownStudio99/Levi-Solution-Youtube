from module.utility.executeAutox import sendExecuteAutox
from module.clickText import clickText
from module.utility.sleepDummy import sleepDummyMs

def openYoutube(deviceIds, ws_url, device_manager):
    try:
        # 현재 상태를 "유튜브 앱 실행 중"으로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("유튜브 앱 실행 중")
        else:
            device_manager.update_device_action(deviceIds, "유튜브 앱 실행 중")
            
        # 유튜브 앱 실행
        sendExecuteAutox(deviceIds, "Scripts/openYoutube.js", ws_url)   
        sleepDummyMs(3000, 5000)
        
        # 유튜브 홈 화면으로 이동
        clickText("홈", deviceIds, ws_url)
        sleepDummyMs(700, 1200)
        
        # 완료 상태를 "유튜브 앱 실행 완료"로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("유튜브 앱 실행 완료")
        else:
            device_manager.update_device_action(deviceIds, "유튜브 앱 실행 완료")
            
    except Exception as e:
        print(f"유튜브 앱 실행 중 오류 발생: {e}")
        # 오류 발생 시 상태 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("유튜브 앱 실행 실패")
        else:
            device_manager.update_device_action(deviceIds, "유튜브 앱 실행 실패")