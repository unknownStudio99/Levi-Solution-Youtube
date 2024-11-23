import random

from module.utility.executeAutox import sendExecuteAutox
from module.clickText import clickText
from module.utility.sleepDummy import sleepDummyMs
from module.clickDesc import clickDesc
from module.inputText import inputText
from module.sendKeyEvent import sendKeyEvent

def randomSearch(deviceIds, ws_url, device_manager):
    try:
        # 현재 상태를 "더미 키워드 검색 중"으로 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("더미 키워드 검색 중")
        else:
            device_manager.update_device_action(deviceIds, "더미 키워드 검색 중")

        organicKeyword = [
                 '축구', '야구', '농구', '발로란트', '포트나이트', '리그 오브 레전드', '카트라이더', 
                 '배틀그라운드', '오버워치', '방탄소년단', '블랙핑크', '아이브', '스트레이 키즈', 
                 '트레저', '세븐틴', '지금, 우리 학교는', '오징어게임', '불가살', '킹덤', '펜트하우스', 
                 '이상한 변호사 우영우', '홈트', '요가', '피트니스', '헬스', '다이어트', '자전거 운동', 
                 '아이폰 15', '삼성 갤럭시', '가상 현실', '인공지능', '드론', '자율주행차', '치킨', '피자', 
                 '분식', '라면', '디저트', '간식 만들기', '스트리트 패션', '메이크업', '뷰티 유튜버', 
                 '헤어 스타일', '스킨케어', '패션 하울', '여행 브이로그', '동남아 여행', '유럽 여행', 
                 '국내 여행지', '해외 여행 팁', '여행 준비물', '자동차 리뷰', '전기차', '운전법', 
                 '차량 관리', '드라이브 코스', '스마트폰', 'AI 기술', '소셜 미디어', '인플루언서', 
                 '디지털 노마드', 'IT 뉴스', '테크 유튜버', '4K 카메라', '리얼리티 쇼', '패션 아이템', 
                 '시즌별 스타일', '트렌디한 의상', '패션 쇼', '스마트 워치', '가전제품', '홈 인테리어', 
                 '셀프 인테리어', '디지털 아트', '사진 촬영 팁', '뮤직 비디오', '일본 애니메이션', 
                 '중국 드라마', '영화 예고편', '넷플릭스 추천', '디즈니 플러스', '비디오 편집', 
                 '브이로그 장비', '보드게임', '레고', '피규어', '미니어처', '게임 스트리밍', 
                 '스포츠 중계', 'NFL', 'NBA', 'MLB', 'EPL', '배구', '탁구', '격투기', '레슬링', 
                 '자동차 리뷰', '모터쇼', '주식 투자', '경제 뉴스', '암호화폐', '비트코인', '블록체인', 
                 'ETF', '부동산 투자', '온라인 쇼핑몰', '리셀링', '중고 거래', '스마트 홈', '스마트 조명', 
                 '홈 오피스', '자기계발', '마인드셋', '책 추천', '명상', '심리학', '생산성 향상', 
                 '자기 개발', '멘탈 관리', '리더십', '개인 브랜딩', '경영 전략', '스타트업', '사회적 기업', 
                 '환경 보호', '기후 변화', '친환경 제품', '제로 웨이스트', '업사이클링', '비건', '유기농', 
                 '동물 보호', '채식', '여성 건강', '남성 건강', '육아', '부모 교육', '청소년 교육', 
                 '스마트 학습', '자녀 교육', '외국어 학습', '온라인 강의', '대학 진학', '취업 준비', 
                 '이력서 작성', '면접 준비', '창업 아이디어', '마케팅 전략', '브랜드 마케팅', 
                 '디지털 마케팅', 'SEO', 'SNS 광고', '콘텐츠 마케팅', '커뮤니티 관리', '스타일링', 
                 '뷰티 팁', '메이크업 튜토리얼', '피부 관리', '피부 타입', '탈모', '헤어 트렌드', 
                 '스킨케어', '네일 아트', '디지털 드로잉', '애니메이션', '게임 음악', '피아노', 
                 '기타', '디제이', '라이브 콘서트', '음악 페스티벌', '미술 전시회', '세계 명화', 
                 '공예', 'DIY 프로젝트', '핸드메이드', '패턴 디자인', '3D 프린팅', '메이커 운동', 
                 '프로토타입 제작', '스타트업 생태계', '창의력', '혁신적인 아이디어', '디자인 사고', 
                 '마케팅 캠페인', '디지털 아트워크', '모바일 게임'
                ]

        # 검색 버튼 클릭
        clickDesc("검색", deviceIds, ws_url)
        sleepDummyMs(500, 1000)

        # 각 디바이스별로 다른 랜덤 키워드 선택 및 저장
        if deviceIds == "all":
            devices = device_manager.get_all_devices()
            for device in devices:
                device_keyword = random.choice(organicKeyword)
                device_manager.update_device_info(
                    device_id=device.device_id,
                    buffer=device_keyword
                )
                # 각 디바이스별로 개별 검색 실행
                inputText(device_keyword, device.device_id, ws_url)
                sleepDummyMs(800, 1500)
        else:
            device_keyword = random.choice(organicKeyword)
            device_manager.update_device_info(
                device_id=deviceIds,
                buffer=device_keyword
            )
            # 단일 디바이스 검색어 입력
            inputText(device_keyword, deviceIds, ws_url)
            sleepDummyMs(7000, 9000)
        
        # 완료 상태를 "더미 키워드 검색 완료"로 업데이트
        if deviceIds == "all":
            # 엔터 키 입력
            sendKeyEvent(66, deviceIds, ws_url)
            sleepDummyMs(2000, 3000)
            device_manager.update_all_devices_action("더미 키워드 검색 완료")
        else:
            # 엔터 키 입력
            sendKeyEvent(66, deviceIds, ws_url)
            sleepDummyMs(2000, 3000)
            device_manager.update_device_action(deviceIds, "더미 키워드 검색 완료") 

    except Exception as e:
        print(f"더미 키워드 검색 중 오류 발생: {e}")
        # 오류 발생 시 상태 업데이트
        if deviceIds == "all":
            device_manager.update_all_devices_action("더미 키워드 검색 실패")
        else:
            device_manager.update_device_action(deviceIds, "더미 키워드 검색 실패")

