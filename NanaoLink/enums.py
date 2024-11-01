from enum import Enum
import wavelink

class RepeatMode(Enum):
    """ใช้ระบุโหมดการเล่นซ้ำของเพลง"""
    CURRENT = wavelink.QueueMode.loop # เล่นเพลงปัจจุบันซ้ำ
    NORMAL = wavelink.QueueMode.normal # ไม่เล่นซ้ำ
    QUEUE = wavelink.QueueMode.loop_all # เล่นทุกเพลงในคิวซ้ำ