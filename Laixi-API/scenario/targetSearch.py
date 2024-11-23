from module.utility.executeAutox import sendExecuteAutox
from module.clickText import clickText
from module.utility.sleepDummy import sleepDummyMs
from module.clickDesc import clickDesc
from module.inputText import inputText
from module.sendKeyEvent import sendKeyEvent

def targetSearch(keyword, deviceIds, ws_url, device_manager):
    try:
        # 현재 상태를 "타겟 키워드 검색 중"으로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action(keyword + " 키워드 검색 중")
        else:
            device_manager.update_device_action(deviceIds, keyword + " 키워드 검색 중")

        # 검색 버튼 클릭
        clickDesc("검색", deviceIds, ws_url)
        sleepDummyMs(500, 1000)

        # 각 디바이스에 타겟 키워드 저장 및 검색 실행
        if deviceIds == "all":
            devices = device_manager.get_all_devices()
            for device in devices:
                device_manager.update_device_info(
                    device_id=device.device_id,
                    buffer=keyword
                )
                # 각 디바이스별로 개별 검색 실행
                inputText(keyword, device.device_id, ws_url)
                sleepDummyMs(800, 1500)
        else:
            device_manager.update_device_info(
                device_id=deviceIds,
                buffer=keyword
            )
            # 단일 디바이스 검색어 입력
            inputText(keyword, deviceIds, ws_url)
            sleepDummyMs(7000, 9000)
        
        # 완료 상태를 "타겟 키워드 검색 완료"로 업데이트
        if deviceIds == "all":
            # 엔터 키 입력
            sendKeyEvent(66, deviceIds, ws_url)
            sleepDummyMs(2000, 3000)
            device_manager.update_all_devices_action(keyword + " 키워드 검색 완료")
        else:
            # 엔터 키 입력
            sendKeyEvent(66, deviceIds, ws_url)
            sleepDummyMs(2000, 3000)
            device_manager.update_device_action(deviceIds, keyword + " 키워드 검색 완료")

    except Exception as e:
        print(f"{keyword} 키워드 검색 중 오류 발생: {e}")
        # 오류 발생 시 상태 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action(keyword + " 키워드 검색 실패")
        else:
            device_manager.update_device_action(deviceIds, keyword + " 키워드 검색 실패")
