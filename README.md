# ❤ NanaoLink

# Thai Ver:

แพ็กเกจ `client` สำหรับลาวาลิงก์ที่สืบทอดจาก `wavelink` ดั่งเดิมโค้ดและการใช้งานพื้นฐานยังคงเป็นของเขา
ส่วนที่เรานำมาปรับเปลี่ยนบางอย่างคือการ ปรับแต่งให้มีความใช้งานง่ายขึ้น ซึ่งปรับแต่งให้เหมือน `Erela.js` ทำให้การใช้งานง่ายและสดวกขึ้นงั้นเอง

โดยพื้นฐานที่มีในปัจจุบันมีดังนี้:

ตัวอย่างการสร้าง Player:
```js
player: Optional[Nanao_Player] = ctx.voice_client
```

| ของดั่งเดิม | เราเอานำมาปรับแต่ง |
|----------|----------|
| wavelink.Player | player.QueueGet() หรือ player.playTrack(track, volume=80) |
| wavelink.Playable | player.TrackSearch("เพลง") |
| wavelink.Filters | player.nightcore.set() หรือ player.karaoke.set() และอื่นๆ เลือกดูได้ |

โดยปัจจุบันยังมีแค่สามอย่างใน อนาคตอาจเพิ่มมาอีก อาจต้องรอก่อน

# Eng Ver:

The `client` package for lavalink inherited from the original `wavelink`. The code and basic usage are still his.
The part that we have changed some is to adjust it to be more user-friendly. Which is adjusted to be like `Erela.js`, making it easier and more convenient to use.

The basics that we have at present are as follows:

Example of creating a Player:
```js
player: Optional[Nanao_Player] = ctx.voice_client
```

| The original | We have adjusted it |
|----------|----------|
| wavelink.Player | player.QueueGet() or player.playTrack(track, volume=80) |
| wavelink.Playable | player.TrackSearch("song") |
| wavelink.Filters | player.nightcore.set() or player.karaoke.set() and others. You can choose to see |

Currently, there are only three things in the future. May add more. May have to wait.