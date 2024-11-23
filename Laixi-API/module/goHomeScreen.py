from module.utility.executeAdb import executeAdbCommand

def goHomeScreen(deviceIds, ws_url, device_manager):
    try:
        # 현재 상태를 "홈 화면 이동 중"으로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("홈 화면 이동 중")
        else:
            device_manager.update_device_action(deviceIds, "홈 화면 이동 중")
        
        # 홈 버튼 누르기 명령 실행
        command = "input keyevent 3"
        executeAdbCommand(command, deviceIds, ws_url)
        
        # 완료 상태를 "홈 화면 이동 완료"로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("홈 화면 이동 완료")
        else:
            device_manager.update_device_action(deviceIds, "홈 화면 이동 완료")
            
    except Exception as e:
        print(f"홈 스크린 이동 중 오류 발생: {e}")
        # 오류 발생 시 상태 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("홈 화면 이동 실패")
        else:
            device_manager.update_device_action(deviceIds, "홈 화면 이동 실패")