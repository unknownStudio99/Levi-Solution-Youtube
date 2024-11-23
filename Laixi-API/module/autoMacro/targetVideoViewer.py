from module.utility.sleepDummy import sleepDummyMs
from module.utility.getAllDeviceInformation import sendAllDeviceList
from module.toastMsg import sendToastMsg
from scenario.targetSearch import targetSearch

def watchTargetVideo(targetKeyword, videoUrl, durationPercent, targetDevices, wsUrl, deviceManager):
    """
    지정된 유튜브 영상을 시청하는 함수
    
    Args:
        video_url (str): 시청할 유튜브 영상 URL
        duration_minutes (int): 시청 시간 (분)
        target_devices (str): 대상 디바이스 ("all" 또는 특정 디바이스 ID)
        ws_url (str): WebSocket URL
        device_manager (DeviceManager): 디바이스 매니저 인스턴스
    """
    try:
        # 타겟 키워드 검색
        targetSearch(targetKeyword, targetDevices, wsUrl, deviceManager)
        sleepDummyMs(2000, 3500)
        
        # 영상 시청
        watchTargetVideo(videoUrl, durationPercent, targetDevices, wsUrl, deviceManager)
        
    except Exception as e:
        print(f"타겟 영상 시청 중 오류 발생: {e}")
        sendToastMsg("타겟 영상 시청 실패", targetDevices, wsUrl)