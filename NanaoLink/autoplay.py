import wavelink


class AutoplayMode:
    """
    คลาสนี้ใช้เพื่อจัดการโหมดการเล่นเพลงอัตโนมัติ (autoplay) ของผู้เล่นเพลง (player)
    """

    def __init__(self, player: wavelink.Player) -> None:
        """
        สร้างอ็อบเจ็กต์ AutoplayMode ที่เชื่อมโยงกับผู้เล่นเพลง (player)

        :param player: wavelink.Player เป็นอ็อบเจ็กต์ของผู้เล่นเพลงที่ต้องการจัดการโหมดการเล่นอัตโนมัติ
        """
        self.player = player

    def on(self):
        """
        เปิดใช้งานโหมด autoplay สำหรับผู้เล่น (player).
        จะทำให้ผู้เล่นเล่นเพลงถัดไปโดยอัตโนมัติเมื่อเพลงปัจจุบันจบ.
        """
        self.player.autoplay = wavelink.AutoPlayMode.enabled

    def off(self):
        """
        ปิดใช้งานโหมด autoplay สำหรับผู้เล่น (player).
        จะทำให้ผู้เล่นหยุดเล่นเพลงถัดไปหลังจากเพลงปัจจุบันจบ.
        """
        self.player.autoplay = wavelink.AutoPlayMode.disabled
