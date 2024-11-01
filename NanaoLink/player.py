import discord.ext.commands
import wavelink
import discord
from typing import Optional
from .filters import Nightcore, Karaoke, LowPass, Distortion, Termolo, SlowDown, Rotation
from .voice import Voice

import discord.ext

class Nanao_Player(wavelink.Player):
    def __init__(self, *args, guild: discord.Guild, **kwargs):
        super().__init__(*args, **kwargs)
        self._guild = guild
        self.voice_channel = None
        self._filters = self.create_filters()
        self._nightcore = Nightcore(self)

    @property
    def guild(self):
        """
        Property สำหรับการเข้าถึงข้อมูล guild
        และค่าค่าข้อมูล guild ที่ถูกเก็บไว้ใน _guild
        """
        return self._guild
    
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
        return Karaoke(self)
    
    @property
    def low_pass(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ LowPass 
        และคืนค่า LowPass ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return LowPass(self)
    
    @property
    def distortion(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ Distortion 
        และคืนค่า Distortion ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return Distortion(self)
    
    @property
    def termolo(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ Termolo 
        และคืนค่า Termolo ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return Termolo(self)
    
    @property
    def slow_down(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ SlowDown 
        และคืนค่า SlowDown ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return SlowDown(self)
    
    @property
    def rotation(self):
        """
        Property สำหรับสร้างอ็อบเจกต์ Rotation 
        และคืนค่า Rotation ที่ถูกสร้างจากผู้เล่นนี้ 
        """
        return Rotation(self)
    
    async def clearFilters(self):
        await self.filters.reset()
        self._nightcore._enabled = False
    
    def create_filters(self):
        """ 
        ฟังก์ชันสำหรับสร้างฟิลเตอร์ใหม่ 
        และคืนค่าฟิลเตอร์ใหม่จาก wavelink.Filters

        โดยในที่นี้จะใช้ wavelink เป็นฐานในการสร้างฟิลเตอร์ใหม่
        """
        return wavelink.Filters()
    
    @property
    def voice(self):
        """
        Property สำหรับการสร้าง player เกี่ยวกับช่องเสียง
        """
        return Voice(self)
    
    async def TrackSearch(self, query: str):
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
        track = self.queue.get()
        return track if track else None

    async def playTrack(self, track: wavelink.Playable, volume: int = 60):
        if track is None:
            raise ValueError("Track cannot be None")
        
        player: Optional[wavelink.Player] = self.guild.voice_client 
        if player is None or not player.connected:
            raise RuntimeError("Player is not connected to a voice channel")
        
        await self.play(track)
        await player.set_volume(volume)