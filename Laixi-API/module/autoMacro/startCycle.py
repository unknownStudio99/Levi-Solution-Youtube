from module.utility.executeAutox import sendExecuteAutox

def startCycle(targetDevices, wsUrl, deviceManager):
    try:
        # 현재 상태를 "사이클 진행 중"으로 업데이트
        if targetDevices == "all":
            deviceManager.update_all_devices_action("사이클 진행 중")
        else:
            deviceManager.update_device_action(targetDevices, "사이클 진행 중")

        print("\n\033[92m사이클을 시작합니다.\033[0m\n")

        sendExecuteAutox(targetDevices, "Scripts/organicWatching.js", wsUrl)

    except Exception as e:
        print(f"\033[91m사이클 시작 중 오류 발생: {e}\033[0m")
        if targetDevices == "all":
            deviceManager.update_all_devices_action("사이클 시작 실패")
        else:
            deviceManager.update_device_action(targetDevices, "사이클 시작 실패")

