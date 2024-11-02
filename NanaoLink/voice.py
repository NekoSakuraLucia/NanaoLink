import discord.ext.commands
import discord
import wavelink
from typing import Union

import discord.ext

class Voice:
    """
    คลาสสำหรับจัดการการเชื่อมต่อเสียงของบอท

    คลาสนี้จะช่วยให้บอทสามารถเชื่อมต่อกับช่องเสียง 
    และจัดการฟังก์ชันที่เกี่ยวข้องกับเสียง เช่น การสร้าง player 
    และเชื่อมต่อกับช่องเสียงของผู้ใช้

    Attributes:
        player: อินสแตนซ์ของ player ที่ใช้ในการจัดการการเชื่อมต่อเสียง
    """
    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นสำหรับตัวจัดการเสียงด้วยอินสแตนซ์ของ player

        Args:
            player: อินสแตนซ์ของ player ที่จะใช้ในการจัดการการเชื่อมต่อเสียง
        """
        self.player = player
        self.voice_channel = None

    async def createPlayer(
        self,
        source: Union[discord.ext.commands.Context, discord.Interaction],
        cls=None,
        self_deaf=True,
        self_mute=False,
        reconnect=False
    ):
        """
        เชื่อมต่อบอทกับช่องเสียงของผู้ใช้

        ฟังก์ชันนี้จะตรวจสอบแหล่งที่มาของคำสั่ง (จาก prefix command หรือ slash command) 
        และพยายามเชื่อมต่อกับช่องเสียงที่เกี่ยวข้อง

        Args:
            source (Union[discord.ext.commands.Context, discord.Interaction]): 
                แหล่งที่มาของคำสั่ง อาจเป็น context จาก prefix command 
                หรือ interaction จาก slash command
            cls (type): คลาสของ player ที่จะสร้าง (ค่าเริ่มต้นคือ None) ควรใช้ wavelink.Player แทน
            self_deaf (bool): ว่าบอทควรจะปิดเสียงตัวเองหรือไม่ (ค่าเริ่มต้นคือ True)
            self_mute (bool): ว่าบอทควรจะทำให้ตัวเองเงียบหรือไม่ (ค่าเริ่มต้นคือ False)
            reconnect (bool): ว่าควรจะเชื่อมต่อใหม่ถ้ามีการเชื่อมต่ออยู่แล้วหรือไม่ (ค่าเริ่มต้นคือ False)

        Raises:
            TypeError: ถ้าประเภทของแหล่งที่มาไม่ถูกต้อง
            AttributeError: ถ้าผู้ใช้ไม่ได้เชื่อมต่อกับช่องเสียง
            RuntimeError: ถ้าการเชื่อมต่อกับช่องเสียงล้มเหลว

        Returns:
            player: อินสแตนซ์ของ player ที่เชื่อมต่อกับช่องเสียง
        """
        if isinstance(source, discord.ext.commands.Context):
            voice_channel = source.author.voice.channel if source.author.voice else None
        elif isinstance(source, discord.Interaction):
            voice_channel = source.user.voice.channel if source.user.voice else None
        else:
            raise TypeError("ประเภทแหล่งที่มาไม่ถูกต้อง คาดว่าเป็น Context หรือ Interaction.")
        
        if not voice_channel:
            raise AttributeError("ผู้ใช้ไม่ได้เชื่อมต่อกับช่องเสียง.")
        
        player: wavelink.Player | None = source.guild.voice_client
        if not player or not player.connected:
            try:
                player = await voice_channel.connect(
                    cls=cls,
                    self_deaf=self_deaf,
                    self_mute=self_mute,
                    reconnect=reconnect
                )
            except Exception as e:
                raise RuntimeError(f"เกิดข้อผิดพลาดในการเชื่อมต่อกับช่องเสียง: {str(e)}")
            
        return player