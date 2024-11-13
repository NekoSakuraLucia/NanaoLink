# ❤ NanaoLink

### ตัว client นี้ทำมาใช้กับ Nekoriku เพื่อให้ใช้งานได้ง่ายขึ้น

แพ็กเกจ `client` สำหรับลาวาลิงก์ที่สืบทอดจาก `wavelink` ดั่งเดิมโค้ดและการใช้งานพื้นฐานยังคงเป็นของเขา
ส่วนที่เรานำมาปรับเปลี่ยนบางอย่างคือการ ปรับแต่งให้มีความใช้งานง่ายขึ้น

ตัวอย่างการสร้าง Player:
```js
player: Optional[Nanao_Player] = ctx.voice_client
```

#### การใช้งานเบื้องต้น (Example Bot)
```py
import discord
from discord.ext import commands
from NanaoLink import NodesCreate, Nanao_Player
import wavelink
from typing import Optional

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(intents=intents, command_prefix="!>")
nodes = NodesCreate(
    identifier="NanaoLink/v0.1.1",
    uri="http://localhost:2333",
    password="yourpassword",
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await nodes.connect(client=bot, cache_capacity=100)

@bot.event
async def on_wavelink_node_ready(payload: wavelink.NodeReadyEventPayload):
    print(f"Wavelink Node connected: {payload.node}")

@bot.command(name="play")
async def music_play(ctx: commands.Context, query: str):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        player = await ctx.author.voice.channel.connect(cls=Nanao_Player, self_deaf=True)
    
    tracks = await player.TrackSearch(query=query)
    if not tracks:
        await ctx.send("ไม่พบแทร็กที่ค้นหา")
    
    if not player.playing:
        next_track = player.QueueGet()
        await player.playTrack(next_track, volume=85)

bot.run("Your/TOKEN")
```