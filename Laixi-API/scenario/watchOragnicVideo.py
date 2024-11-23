from module.utility.sleepDummy import sleepDummyMs
from module.utility.getAllDeviceInformation import sendAllDeviceList
from module.toastMsg import sendToastMsg
from module.utility.executeAutox import sendExecuteAutox
from scenario.randomSearch import randomSearch

def watchOragnicVideo(targetDevices, wsUrl, deviceManager):
    try:
        # 현재 상태를 "오거닉 영상 시청 중"으로 업데이트
        if targetDevices == "all":
            deviceManager.update_all_devices_action("오거닉 영상 시청 중")
        else:
            deviceManager.update_device_action(targetDevices, "오거닉 영상 시청 중")
        
        print("\n\033[92m더미 작업을 시작합니다.\033[0m\n")

        # 오거닉 키워드 검색
        print("\n\033[92m오거닉 키워드 검색을 시작합니다.\033[0m\n")
        randomSearch("all", wsUrl, deviceManager)
        sleepDummyMs(1500, 3000)

        # 텍스트 기반 쿼리 (영상 탐지)
        # print("\n\033[92m텍스트 기반 쿼리를 시작합니다.\033[0m\n")
        # sendExecuteAutox(targetDevices, "Scripts/queryTextAll.js", wsUrl)
        # sleepDummyMs(3500, 4500)

        # 오거닉 영상 시청
        print("\n\033[92m화면 기준 첫 번째 영상 클릭을 시작합니다.\033[0m\n")
        sendExecuteAutox(targetDevices, "Scripts/organicWatching.js", wsUrl)
        sleepDummyMs(1500, 2500)
        
        # 현재 상태를 "오거닉 영상 시청 완료"로 업데이트
        if targetDevices == "all":
            deviceManager.update_all_devices_action("오거닉 영상 시청 완료")
        else:
            deviceManager.update_device_action(targetDevices, "오거닉 영상 시청 완료")

    except Exception as e:
        print(f"오거닉 영상 시청 중 오류 발생: {e}")
        if targetDevices == "all":
            deviceManager.update_all_devices_action("오거닉 영상 시청 실패")
        else:
            deviceManager.update_device_action(targetDevices, "오거닉 영상 시청 실패")
