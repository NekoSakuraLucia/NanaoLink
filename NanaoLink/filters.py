import wavelink

class Nightcore:
    """
    Class สำหรับจัดการฟิลเตอร์ Nightcore
    ซึ่งใช้เพื่อปรับความเร็วและเสียงของเพลง
    """
    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ Nightcore
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player
    
    async def set(self, speed=1.2, pitch=1.2, rate=1):
        """
        ตั้งค่าฟิลเตอร์ timescale สำหรับ Nightcore

        ฟังก์ชันนี้จะปรับความเร็วและเสียงของเพลงตามที่ระบุ
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ผู้เล่น

        Args:
            speed (float): ค่าความเร็วของเพลง (ค่าเริ่มต้น 1.2)
            pitch (float): ค่าพิชของเสียง (ค่าเริ่มต้น 1.2)
            rate (float): ค่าระดับการเปลี่ยนแปลง (ค่าเริ่มต้น 1)
        """
        filters: wavelink.Filters = self.player.filters
        filters.timescale.set(speed=speed, pitch=pitch, rate=rate)
        await self.player.set_filters(filters)