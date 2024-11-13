import discord
from discord.ext import commands
from NanaoLink import NodesCreate, Nanao_Player
import wavelink
from typing import Optional

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(intents=intents, command_prefix="!")
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


# Note: เล่นเพลงทั่วไป (Normal Playing)


@bot.command(name="play")
async def music_play(ctx: commands.Context, query: str):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        player = await ctx.author.voice.channel.connect(
            cls=Nanao_Player, self_deaf=True
        )

    tracks = await player.TrackSearch(query=query)
    if not tracks:
        await ctx.send("ไม่พบแทร็กที่ค้นหา")

    if not player.playing:
        next_track = player.QueueGet()
        await player.playTrack(next_track, volume=85)


@bot.command(name="loop")
async def loop(ctx: commands.Context):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        return

    if not player:
        await ctx.send("ไม่สามารถสร้าง player ได้")
        return

    player.set_repeat.loop()
    await ctx.send(f"เปิดการใช้งาน {player.queue_mode.name} แล้ว")


@bot.command(name="pause")
async def autoplay(ctx: commands.Context):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        return

    if not player:
        await ctx.send("ไม่สามารถสร้าง player ได้")
        return

    await player.toggle(False)
    await ctx.send(f"เปิดการใช้งาน Pause แล้ว")


@bot.command(name="resumed")
async def resumed(ctx: commands.Context):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        return

    if not player:
        await ctx.send("ไม่สามารถสร้าง player ได้")
        return

    await player.toggle(True)
    await ctx.send(f"เปิดการใช้งาน Resumed แล้ว")


@bot.command(name="seek")
async def seek(ctx: commands.Context, time: str):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        return

    if not player:
        await ctx.send("ไม่สามารถสร้าง player ได้")
        return

    try:
        await player.seek_seconds(time)
        await ctx.send(f"เลื่อนไปยังตำแหน่ง {time} สำเร็จแล้ว!")
    except RuntimeError as e:
        await ctx.send(f"เกิดข้อผิดพลาด: {e}")
    except Exception as e:
        await ctx.send(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")


@bot.command(name="leave")
async def leave_voice(ctx: commands.Context):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        return

    if not player:
        await ctx.send("ไม่สามารถสร้าง player ได้")
        return

    await player.disconnect()
    await ctx.send(f"ออกจากห้องเสียงแล้ว")


# Note: เล่นเพลงในโหมดฟิลเตอร์ (Play music in filter mode)


@bot.command(name="nightcore")
async def nightcore(ctx: commands.Context):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        return

    if not player:
        await ctx.send("ไม่สามารถสร้าง player ได้")
        return

    await player.nightcore.set()
    await ctx.send(f"เปิดการใช้งาน Nightcore แล้ว")


@bot.command(name="equalizer")
async def equalizer(ctx: commands.Context):
    player: Optional[Nanao_Player] = ctx.voice_client
    if not player:
        return

    if not player:
        await ctx.send("ไม่สามารถสร้าง player ได้")
        return

    await player.equalizer.set()
    await ctx.send(f"เปิดการใช้งาน Equalizer แล้ว")


# Note: ในที่นี้เราจะยกตัวอย่างการใช้ฟิลเตอร์แค่สองตัวก่อน ยังมีอีกหลายฟิลเตอร์ที่คุณสามารถใช้ได้อีกหลายตัว
# Note: Here we will give an example of using just two filters first. There are many more filters you can use.

bot.run("Your/Token")
