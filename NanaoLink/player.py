import wavelink
from typing import Optional
from .filters import *

class Nanao_Player(wavelink.Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._filters = self.create_filters()
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
        return self
    
    def loop(self):
        """
        ตั้งค่าให้เล่นเพลงปัจจุบันซ้ำ (Loop Current)

        ฟังก์ชันนี้จะเปลี่ยนโหมดการเล่นของผู้เล่น (player) ให้เล่นเพลงที่กำลังเล่นอยู่ในขณะนี้ซ้ำ
        โดยตั้งค่า `queue.mode` ให้เป็น `wavelink.QueueMode.loop` ซึ่งจะทำให้เพลงปัจจุบันในคิวเล่นซ้ำจนกว่าจะมีการหยุดหรือเปลี่ยนเพลงใหม่ (แต่ก่อนจะใช้ได้ต้องคิวเพลงไม่น้อยกว่า 2 เท่านั้น)

        Note:
            โหมดนี้ใช้สำหรับการเล่นเพลงเดิมที่กำลังเล่นอยู่ในคิวซ้ำโดยไม่ข้ามไปเพลงถัดไป
        """
        self.queue.mode = wavelink.QueueMode.loop

    def normal(self):
        """
        ตั้งค่าให้ไม่เล่นเพลงซ้ำ (Normal Mode)

        ฟังก์ชันนี้จะตั้งค่าโหมดการเล่นให้เป็นโหมดปกติ (ไม่เล่นซ้ำ) โดยการเปลี่ยนค่า `queue.mode` 
        ให้เป็น `wavelink.QueueMode.normal` ซึ่งหมายความว่าเมื่อเพลงปัจจุบันจบลง เพลงจะข้ามไปเล่นเพลงถัดไปในคิว
        โดยไม่ทำการเล่นซ้ำเพลงใด ๆ

        Note:
            โหมดนี้ใช้สำหรับการเล่นเพลงตามลำดับปกติในคิวโดยไม่ทำการลูป
        """
        self.queue.mode = wavelink.QueueMode.normal
    
    def loop_all(self):
        """
        ตั้งค่าให้เล่นทุกเพลงในคิวซ้ำ (Loop All)

        ฟังก์ชันนี้จะตั้งค่าโหมดการเล่นของเพลงให้เล่นทุกเพลงในคิวซ้ำ โดยการตั้งค่า `queue.mode`
        ให้เป็น `wavelink.QueueMode.loop_all` ซึ่งหมายความว่าเมื่อเพลงในคิวจบลง เพลงจะเริ่มเล่นเพลงแรกในคิวซ้ำ
        และจะเล่นซ้ำทุกเพลงในคิวไปเรื่อย ๆ จนกว่าจะมีการหยุดหรือเปลี่ยนโหมด

        Note:
            โหมดนี้ใช้สำหรับการลูปทั้งหมดในคิว โดยไม่ข้ามเพลงจนกว่าเราจะหยุดหรือเปลี่ยนโหมด
        """
        self.queue.mode = wavelink.QueueMode.loop_all

    @property
    def queue_mode(self):
        """ส่งคืนโหมดคิวปัจจุบันของโหมดคิวเพลง"""
        return self.queue.mode
    
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
        
        await self.play(track)
        await player.set_volume(volume)