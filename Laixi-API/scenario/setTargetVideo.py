from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scenario.updateTargetVideoInfo import updateTargetVideoInfo
from module.utility.sleepDummy import sleepDummyMs

def getTargetVideoInfo(link):
    try:
        # Chrome 옵션 설정
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 헤드리스 모드
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        
        # 영상 제목 가져오기
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#title h1 yt-formatted-string"))
        ).get_attribute('textContent')
        
        # 영상 길이 가져오기
        video_time = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ytp-time-duration"))
        ).text
        
        driver.quit()
        print(f"\n\033[92m{title} 영상 정보 가져오기 성공 - 길이: {video_time}\033[0m\n")
        return title, video_time
    
    except Exception as e:
        print(f"영상 정보 가져오기 실패: {e}")
        return None, None

def setTargetVideo(keyword, link, watchingTime, deviceIds, ws_url, device_manager):
    try:
        # 영상 정보 가져오기
        title, video_time = getTargetVideoInfo(link)
        if not title or not video_time:
            raise Exception("영상 정보를 가져올 수 없습니다")
        
        # video_time을 밀리초로 변환
        time_parts = video_time.split(':')
        total_seconds = sum(x * int(y) for x, y in zip([60, 1], time_parts))
        video_time_ms = total_seconds * 1000
        
        # createTargetVideoInfo.js 파일 업데이트
        updateTargetVideoInfo(keyword, title, video_time_ms, deviceIds, ws_url)
        sleepDummyMs(1500, 2500)

        # 현재 상태를 "타겟 영상 시청 완료"로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action(f"{title} 영상 정보 가져오기 완료")
        else:
            device_manager.update_device_action(deviceIds, f"{title} 영상 정보 가져오기 완료")
            
        return title, video_time
        
    except Exception as e:
        print(f"영상 정보 가져오기 중 오류 발생: {e}")
        if deviceIds == "all":
            device_manager.update_all_devices_action("영상 정보 가져오기 실패")
        else:
            device_manager.update_device_action(deviceIds, "영상 정보 가져오기 실패")
        return None, None

