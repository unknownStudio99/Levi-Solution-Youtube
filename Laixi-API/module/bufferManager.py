import json
import time
import concurrent.futures
from collections import defaultdict
from queue import Queue
from threading import Lock
from module.getBuffer import BufferWebSocket

class BufferManager:
    def __init__(self, ws_url, device_manager):
        self.device_manager = device_manager
        self.ws_url = ws_url
        self.device_buffers = {}
        self.connection_pool = []
        self.pool_size = 10  # 웹소켓 연결 풀 크기 (커스터마이징 가능)
        self.max_workers = 20  # 동시 실행할 최대 스레드 수 (커스터마이징 가능)
        self.batch_size = 50   # 한 번에 처리할 디바이스 수 (커스터마이징 가능)
        self.connection_lock = Lock()
        self._initialize_connection_pool()

    def _initialize_connection_pool(self):
        """웹소켓 연결 풀 초기화"""
        for _ in range(self.pool_size):
            ws_client = BufferWebSocket(self.ws_url)
            self.connection_pool.append(ws_client)

    def _get_connection(self):
        """연결 풀에서 사용 가능한 웹소켓 연결 가져오기"""
        with self.connection_lock:
            for ws in self.connection_pool:
                if not ws.is_in_use:
                    ws.is_in_use = True
                    return ws
            # 모든 연결이 사용 중이면 새로운 연결 생성
            ws_client = BufferWebSocket(self.ws_url)
            ws_client.is_in_use = True
            self.connection_pool.append(ws_client)
            return ws_client

    def _release_connection(self, ws):
        """웹소켓 연결을 풀에 반환"""
        with self.connection_lock:
            ws.is_in_use = False

    def _update_single_device(self, device):
        if not device.is_online:
            return

        ws_client = None
        try:
            ws_client = self._get_connection()
            buffer_response = ws_client.get_buffer(device.device_id)
            if buffer_response:
                response_data = json.loads(buffer_response)
                if response_data.get('StatusCode') == 200:
                    new_buffer = response_data.get('result', '').strip()
                    current_buffer = self.device_buffers.get(device.device_id, '')
                    
                    if new_buffer and new_buffer != current_buffer:
                        print(f"버퍼 업데이트 - 기기: {device.device_id}, 새값: {new_buffer}")
                        self.device_manager.update_device_info(
                            device_id=device.device_id,
                            buffer=new_buffer
                        )
                        self.device_buffers[device.device_id] = new_buffer
                    
        except Exception as e:
            print(f"기기 {device.device_id} 버퍼 업데이트 실패: {str(e)}")
        finally:
            if ws_client:
                self._release_connection(ws_client)

    def _process_batch(self, devices):
        """디바이스 배치 처리"""
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self._update_single_device, device) 
                      for device in devices]
            concurrent.futures.wait(futures)

    def update_buffer_status(self):
        try:
            devices = self.device_manager.get_all_devices()
            total_devices = len(devices)
            
            # 디바이스를 배치로 나누어 처리
            for i in range(0, total_devices, self.batch_size):
                batch = devices[i:i + self.batch_size]
                self._process_batch(batch)
                
        except Exception as e:
            print(f"전체 버퍼 업데이트 실패: {str(e)}")

    def __del__(self):
        for ws in self.connection_pool:
            ws.close()