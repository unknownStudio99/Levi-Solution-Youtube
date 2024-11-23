from module.utility.sleepDummy import sleepDummyMs
from module.utility.executeAutox import sendExecuteAutox

def updateTargetVideoInfo(newKeyword, newTitle, newVideoTime, targetDevices, wsUrl):
    file_path = r"C:\Program Files\Laixi\Scripts\createTargetVideoInfo.js"
    
    try:
        # 파일 전체 내용 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 첫 두 줄 수정
        lines[0] = f'let keyword = "{newKeyword}";\n'
        lines[1] = f'let title = "{newTitle}";\n'
        lines[2] = f'let videoTime = {newVideoTime};\n'
        
        # 수정된 내용 파일에 쓰기
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        sleepDummyMs(1500, 2500)
        result = sendExecuteAutox(targetDevices, "Scripts/createTargetVideoInfo.js", wsUrl)
        
        if not result:
            print(f"[ERROR] AutoX 실행 실패: {targetDevices}")
            return False
            
        return True

    except FileNotFoundError:
        print(f"[ERROR] 파일을 찾을 수 없음: {file_path}")
        return False
    except Exception as e:
        print(f"[ERROR] 비디오 정보 업데이트 중 오류 발생: {str(e)}")
        return False
