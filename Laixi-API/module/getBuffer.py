import json
import traceback
import time
from websocket import create_connection

class BufferWebSocket:
    def __init__(self, ws_url):
        self.ws_url = ws_url
        self.ws = None
        self.is_in_use = False
        self.last_used = 0
        self.connect()

    def connect(self):
        try:
            if self.ws is None or not self.ws.connected:
                self.ws = create_connection(self.ws_url)
                print(f"웹소켓 연결 성공 (ID: {id(self)})")
                return True
            return True
        except Exception as e:
            print(f"웹소켓 연결 실패: {e}")
            self.ws = None
            return False

    def get_buffer(self, device_id):
        try:
            if not self.connect():
                return None

            start_time = time.time()
            self.last_used = start_time
            
            message = json.dumps({
                "action": "getclipboard",
                "comm": {
                    "deviceIds": device_id
                }
            })
            
            self.ws.send(message)
            send_time = time.time() - start_time
            
            result = self.ws.recv()
            total_time = time.time() - start_time
            
            if total_time > 7.0:
                print(f"⚠️  느린 응답 감지 - 기기: {device_id}, 소요시간: {total_time:.3f}초")
            else:
                print(f"기기 {device_id} 버퍼 요청 완료: {total_time:.3f}초")
            
            return result
            
        except Exception as e:
            print(f"버퍼 가져오기 실패 ({device_id}): {e}")
            self.ws = None
            return None
        finally:
            self.is_in_use = False

    def is_healthy(self):
        return self.ws is not None and self.ws.connected

    def is_idle(self):
        current_time = time.time()
        return (not self.is_in_use and 
                current_time - self.last_used > 0.1)

    def close(self):
        if self.ws:
            try:
                self.ws.close()
            except Exception as e:
                print(f"연결 종료 중 오류: {e}")
            finally:
                self.ws = None
                self.is_in_use = False
