from module.utility.executeAdb import executeAdbCommand

def killYoutube(deviceIds, ws_url, device_manager): 
    try:
        # 현재 상태를 "유튜브 앱 종료 중"으로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("유튜브 앱 종료 중")
        else:
            device_manager.update_device_action(deviceIds, "유튜브 앱 종료 중")
            
        # 유튜브 앱 강제 종료
        command = "am force-stop com.google.android.youtube"
        executeAdbCommand(command, deviceIds, ws_url)
        
        # 완료 상태를 "유튜브 앱 종료 완료"로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("유튜브 앱 종료 완료")
        else:
            device_manager.update_device_action(deviceIds, "유튜브 앱 종료 완료")
            
    except Exception as e:
        print(f"유튜브 앱 종료 중 오류 발생: {e}")
        # 오류 발생 시 상태 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("유튜브 앱 종료 실패")
        else:
            device_manager.update_device_action(deviceIds, "유튜브 앱 종료 실패")