import json
import time
import threading

# 모듈 임포트
from module.toastMsg import sendToastMsg
from module.utility.getAllDeviceInformation import sendAllDeviceList
from module.utility.sleepDummy import sleepDummyMs
from module.goHomeScreen import goHomeScreen
from module.deviceORM.deviceManager import DeviceManager
from deviceMonitor import DeviceMonitor
from module.bufferManager import BufferManager

# 시나리오 임포트
from scenario.killYoutube import killYoutube
from scenario.openYoutube import openYoutube
from scenario.randomSearch import randomSearch
from scenario.targetSearch import targetSearch
from scenario.setTargetVideo import setTargetVideo
from scenario.watchOragnicVideo import watchOragnicVideo
from module.autoMacro.startCycle import startCycle

# laixi API 주소
ws_url = "ws://127.0.0.1:22221"

# 기기 매니저 인스턴스 생성
device_manager = DeviceManager()

def update_device_status():
    while True:
        try:
            devices_info = sendAllDeviceList(ws_url)
            if devices_info:
                response = json.loads(json.loads(devices_info)['result'])
                for device in response:
                    update_info = {
                        'device_id': device['deviceId'],
                        'name': device.get('name', ''),
                        'model': device.get('name', ''),
                        'status': 'connected',
                        'is_online': True,
                        'is_otg': device.get('isOtg', False),
                        'is_cloud': device.get('isCloud', False),
                        'device_no': device.get('no')
                    }
                    if device.get('buffer'):
                        update_info['buffer'] = device['buffer']
                    device_manager.update_device_info(**update_info)
                
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{current_time}] 디바이스 상태 업데이트 완료: {len(response)}개 기기")
            time.sleep(3)
        except Exception as e:
            print(f"업데이트 중 오류 발생: {e}")
            time.sleep(3)

def update_buffer_status():
    buffer_manager = BufferManager(ws_url, device_manager)
    while True:
        try:
            buffer_manager.update_buffer_status()
            time.sleep(1)
        except Exception as e:
            print(f"버퍼 업데이트 중 오류 발생: {e}")
            time.sleep(1)

def main():
    try:
        # GUI 모니터 생성
        monitor = DeviceMonitor(device_manager)
        
        def start_main_tasks():
            try:
                print("메인 작업 시작")
                # 시작 토스트 메시지
                sendToastMsg("프로그램 연동 완료", "all", ws_url)
                
                # 타겟 영상 설정
                setTargetVideo("Charlie Puth", "https://www.youtube.com/watch?v=WFsAon_TWPQ", 10, "all", ws_url, device_manager)
                print("\n\033[93m타겟 영상 설정 중입니다..\033[0m\n")

                # 홈 화면으로 이동
                goHomeScreen("all", ws_url, device_manager)
                sleepDummyMs(800,1500)
                
                # 유튜브 앱 종료
                killYoutube("all", ws_url, device_manager)
                sleepDummyMs(800,1500)
                
                # 유튜브 앱 실행
                openYoutube("all", ws_url, device_manager)
                sleepDummyMs(3000,5000)

                # 사이클 시작
                startCycle("all", ws_url, device_manager)
                
            except Exception as e:
                print(f"작업 실행 중 오류 발생: {e}")

        # 디바이스 상태 업데이트 스레드 시작
        update_thread = threading.Thread(target=update_device_status, daemon=True)
        update_thread.start()

        # 버퍼 상태 업데이트 스레드 시작
        buffer_thread = threading.Thread(target=update_buffer_status, daemon=True)
        buffer_thread.start()

        # 메인 작업 스레드 시작
        main_thread = threading.Thread(target=start_main_tasks, daemon=True)
        main_thread.start()
        
        # GUI 메인 루프 실행
        monitor.root.mainloop()
        
    except Exception as e:
        print(f"메인 함수 실행 중 오류 발생: {e}")
        raise

if __name__ == "__main__":
    main()
