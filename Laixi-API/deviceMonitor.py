import tkinter as tk
from tkinter import ttk
import threading
import time
from module.deviceORM.models import Device

class DeviceMonitor:
    def __init__(self, device_manager):
        self.device_manager = device_manager
        self.root = tk.Tk()
        self.root.title("Device Monitor")
        self.current_buffers = {}  # 현재 버퍼 값을 저장할 딕셔너리
        
        # 트리뷰 생성
        self.tree = ttk.Treeview(self.root, columns=(
            'Device ID', 
            'Name', 
            'Status', 
            'Current Action',
            'Buffer'  # 버퍼 컬럼 추가
        ), show='headings')
        
        # 컬럼 설정
        self.tree.heading('Device ID', text='Device ID')
        self.tree.heading('Name', text='이름')
        self.tree.heading('Status', text='상태')
        self.tree.heading('Current Action', text='현재 동작')
        self.tree.heading('Buffer', text='버퍼')  # 버퍼 헤딩 추가
        
        # 컬럼 너비 설정
        self.tree.column('Device ID', width=150)
        self.tree.column('Name', width=100)
        self.tree.column('Status', width=100)
        self.tree.column('Current Action', width=200)
        self.tree.column('Buffer', width=100)  # 버퍼 컬럼 너비 설정
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # 상태 레이블 추가
        self.status_label = tk.Label(self.root, text="", anchor="w")
        self.status_label.pack(fill=tk.X, padx=5, pady=5)
        
        # 업데이트 시작
        self.update_devices()
    
    def update_devices(self):
        try:
            devices = self.device_manager.get_all_devices()
            self.status_label.config(text=f"마지막 업데이트: {time.strftime('%Y-%m-%d %H:%M:%S')} - 디바이스 수: {len(devices)}")
            
            # 현재 표시된 항목들의 버퍼 값을 저장
            current_tree_items = {}
            for item in self.tree.get_children():
                values = self.tree.item(item)['values']
                device_id = values[0]
                buffer_value = values[4]
                if buffer_value:  # 버퍼 값이 있으면 저장
                    current_tree_items[device_id] = buffer_value
            
            # 트리뷰 초기화
            self.tree.delete(*self.tree.get_children())
            
            for device in devices:
                device_id = device.device_id
                
                # 버퍼 값 결정 로직
                buffer_value = device.buffer
                if not buffer_value:  # 새로운 버퍼 값이 비어있으면
                    # 1. 현재 트리뷰에 있던 값 확인
                    buffer_value = current_tree_items.get(device_id)
                    if not buffer_value:  # 2. 없으면 저장된 버퍼 값 확인
                        buffer_value = self.current_buffers.get(device_id, '')
                
                if buffer_value:  # 유효한 버퍼 값이 있으면 저장
                    self.current_buffers[device_id] = buffer_value
                    # DeviceManager에도 버퍼 값 유지
                    self.device_manager.update_device_info(
                        device_id=device_id,
                        buffer=buffer_value
                    )
                
                self.tree.insert('', tk.END, values=(
                    device_id,
                    device.name,
                    device.status,
                    device.current_action,
                    buffer_value or self.current_buffers.get(device_id, '')  # 저장된 값 사용
                ))
                
        except Exception as e:
            self.status_label.config(text=f"오류 발생: {str(e)}")
            print(f"업데이트 중 오류 발생: {e}")
        
        # 다음 업데이트 예약
        self.root.after(1000, self.update_devices)