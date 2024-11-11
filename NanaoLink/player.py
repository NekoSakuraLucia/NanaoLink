import wavelink
import re
from typing import Optional
from .filters import *
from .Repeat import RepeatMode
from .autoplay import AutoplayMode

class Nanao_Player(wavelink.Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._filters = self.create_filters()
        self._repeatMode = RepeatMode(self)
        self._autoplayMode = AutoplayMode(self)
        self._nightcore = Nightcore(self)
        self._karaoke = Karaoke(self)
        self._lowpass = LowPass(self)
        self._termolo = Termolo(self)
        self._slowdown = SlowDown(self)
        self._rotation = Rotation(self)
        self._distortion = Distortion(self)
        self._vibrato = Vibrato(self)
    
    @property
    def filters(self):
        """ 
        Property สำหรับเข้าถึงฟิลเตอร์ 
        และคืนค่าฟิลเตอร์ที่ถูกสร้างขึ้นใน _filters 
        """
        return self._filters

    @property
    def nightcore(self):
        """ 
        Property สำหรับสร้างอ็อบเจกต์ Nightcore 
        และคืนค่า Nightcore ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return self._nightcore
    
    @property
    def karaoke(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ Karaoke 
        และคืนค่า Kraoke ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return self._karaoke
    
    @property
    def low_pass(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ LowPass 
        และคืนค่า LowPass ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return self._lowpass
    
    @property
    def distortion(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ Distortion 
        และคืนค่า Distortion ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return self._distortion
    
    @property
    def termolo(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ Termolo 
        และคืนค่า Termolo ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return self._termolo
    
    @property
    def slow_down(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ SlowDown 
        และคืนค่า SlowDown ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return self._slowdown
    
    @property
    def rotation(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ Rotation 
        และคืนค่า Rotation ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return self._rotation
    
    @property
    def vibrato(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ Vibrato 
        และคืนค่า Vibrato ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return self._vibrato
    
    def create_filters(self):
        """ 
        ฟังก์ชันสำหรับสร้างฟิลเตอร์ใหม่ 
        และคืนค่าฟิลเตอร์ใหม่จาก wavelink.Filters

        โดยในที่นี้จะใช้ wavelink เป็นฐานในการสร้างฟิลเตอร์ใหม่
        """
        return wavelink.Filters()
    
    def _check_queue_length(self):
        """
        ตรวจสอบว่ามีเพลงในคิวเพียงพอในการตั้งค่าโหมดการเล่นซ้ำ

        Raises:
            RuntimeError: หากจำนวนเพลงคิววมีน้อยกว่า 2
        """
        if self.queue.count < 2:
            raise RuntimeError("ไม่สามารถตั้งค่าโหมดเล่นซ้ำได้ เพลงในคิวไม่เพียงพอ")
    
    @property
    def set_repeat(self):
        """คืนค่า object สำหรับการตั้งค่าโหมดการเล่นซ้ำ"""
        self._check_queue_length()
        return self._repeatMode

    @property
    def queue_mode(self):
        """ส่งคืนโหมดคิวปัจจุบันของโหมดคิวเพลง"""
        return self.queue.mode
    
    @property
    def auto_play(self):
        """
        ได้รับค่า autoplay mode ที่ถูกตั้งค่าไว้ใน player

        ค่า _autoplayMode ที่เก็บสถานะการเล่นอัตโนมัติ
        """
        return self._autoplayMode
    
    async def toggle(self, play: bool):
        """
        เปลี่ยนสถานะของเพลงให้เล่นหรือหยุดตามที่กำหนด\n
        การทำงานของ toggle นี้จะคล้ายกับ `player.pause(True หรือ False)`

        :param play: ค่าของ `True` หมายถึงต้องการให้เล่นเพลงต่อ\n
                     ค่าของ `False` หมายถึงต้องการให้หยุดเพลง
        :raises RuntimeError: หากเพลงอยู่ในสถานะที่ไม่สามารถทำการสลับสถานะได้\n
                               - ถ้าเพลงกำลังเล่นแล้วและพยายามเล่นอีกครั้ง\n
                               - ถ้าเพลงหยุดแล้วและพยายามหยุดอีกครั้ง
        """
        if play:
            if self.paused:
                await self.pause(False)
            else:
                raise RuntimeError("Already playing.")
        else:
            if not self.paused: 
                await self.pause(True)
            else:
                raise RuntimeError("Already paused.")
            
    async def seek_seconds(self, time_str: str):
        """
        แปลงเวลาในรูปแบบ 'นาที:วินาที' ให้เป็นหน่วยมิลลิวินาที และเรียกใช้ฟังก์ชัน seek() เพื่อเลื่อนไปยังตำแหน่งที่กำหนด

        Parameters:
            time_str (str): เวลาในรูปแบบ 'นาที:วินาที' เช่น '1:02' (1 นาที 2 วินาที)

        Raises:
            RuntimeError: หากรูปแบบเวลาไม่ถูกต้อง (ไม่ได้อยู่ในรูปแบบ 'นาที:วินาที')
        """
        match = re.match(r"(\d+):(\d+)", time_str)
        if not match:
            raise RuntimeError("รูปแบบเวลาไม่ถูกต้อง ควรใช้รูปแบบนาที:วินาที เช่น 1:02")
        
        minutes, seconds = int(match.group(1)), int(match.group(2))
        milliseconds = (minutes * 60 + seconds) * 1000
        await self.seek(milliseconds)
    
    async def TrackSearch(self, query: str):
        """
        ค้นหาแทร็กตามคำค้นหาที่กำหนด
        
        Args:
            query (str): คำค้นสำหรับการค้นหาแทร็ก

        Returns:
            track (Playable): อาจคืนค่าเป็นลิสต์ที่มีแทร็กแรกที่พบ หรือ Playlist ถ้ามีหลายแทร็กคืนค่า None ถ้าไม่พบแทร็กเลย
        """
        tracks: wavelink.Playable = await wavelink.Playable.search(query)
        if not tracks:
            return None
        
        if isinstance(tracks, wavelink.Playlist):
            await self.queue.put_wait(tracks)
            return tracks
        else:
            track: wavelink.Playable = tracks[0]
            await self.queue.put_wait(track)
            return [track]
        
    def QueueGet(self):
        """
        ดึงแทร็กถัดไปจากคิว

        Returns:
            QueueGet (Queue): แทร็กถัดไปจากคิว
        """
        return self.queue.get()

    async def playTrack(self, track: wavelink.Playable, volume: int = 60):
        """เล่นแทร็กที่กำหนดพร้อมระดับเสียงที่เลือกได้
        
        Args:
            track (wavelink.Playable): แทร็กที่ต้องการเล่น
            volume (int): ระดับเสียง (ค่าเริ่มต้นคือ 60)
        
        Raises:
            ValueError: ถ้าแทร็กเป็น None
            RuntimeError: ถ้าผู้เล่นไม่เชื่อมต่อกับช่องเสียง
        """
        if track is None:
            raise ValueError("Track cannot be None")
        
        player: Optional[wavelink.Player] = self.guild.voice_client 
        if player is None or not player.connected:
            raise RuntimeError("Player is not connected to a voice channel")
        
        await self.play(track, volume=volume)