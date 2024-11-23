from datetime import datetime
from .database import DatabaseManager
from .models import Device

class DeviceManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.device_buffers = {}  # 버퍼 값을 메모리에 저장
    
    def update_device_info(self, device_id, **kwargs):
        session = self.db_manager.get_session()
        try:
            device = session.query(Device).filter_by(device_id=device_id).first()
            if device:
                # 버퍼 값이 있으면 메모리에 저장
                if 'buffer' in kwargs:
                    self.device_buffers[device_id] = kwargs['buffer']
                elif device_id in self.device_buffers:
                    # 버퍼 값이 없으면 메모리에 저장된 값 사용
                    kwargs['buffer'] = self.device_buffers[device_id]
                
                for key, value in kwargs.items():
                    setattr(device, key, value)
                device.last_seen = datetime.utcnow()
            else:
                if 'buffer' in kwargs:
                    self.device_buffers[device_id] = kwargs['buffer']
                device = Device(device_id=device_id, **kwargs)
                session.add(device)
            session.commit()
        finally:
            session.close()
    
    def update_device_action(self, device_id, action):
        session = self.db_manager.get_session()
        try:
            device = session.query(Device).filter_by(device_id=device_id).first()
            if device:
                device.current_action = action
                device.last_seen = datetime.utcnow()
                session.commit()
        finally:
            session.close()
    
    def update_all_devices_action(self, action):
        session = self.db_manager.get_session()
        try:
            devices = session.query(Device).all()
            for device in devices:
                device.current_action = action
                device.last_seen = datetime.utcnow()
            session.commit()
        finally:
            session.close()
    
    def get_all_devices(self):
        session = self.db_manager.get_session()
        try:
            return session.query(Device).all()
        finally:
            session.close()