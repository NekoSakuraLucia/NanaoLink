import wavelink

class Karaoke:
    """
    Class สำหรับจัดการฟิลเตอร์ Karaoke
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ karaoke
    """
    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ Karaoke
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player

    async def set(self, level=2, mono_level=1, filter_band=220, filter_width=100):
        """
        ตั้งค่าฟิลเตอร์ karaoke สำหรับ Karaoke

        ฟังก์ชั่นนี้จะปรับค่าฟิลเตอร์ karaoke ตามที่ระบุ
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ผู้เล่น

        Args:
            level (int): ระดับของฟิลเตอร์ karaoke (ค่าเริ่มต้นคือ 2)
            mono_level (int): ระดับเสียงโมโน (ค่าเริ่มต้นคือ 1)
            filter_band (int): ความถี่ของฟิลเตอร์ (ค่าเริ่มต้นคือ 220)
            filter_width (int): ความกว้างของฟิลเตอร์ (ค่าเริ่มต้นคือ 100)
        """
        filters: wavelink.Filters = self.player.filters
        filters.karaoke.set(level=level, mono_level=mono_level, filter_band=filter_band, filter_width=filter_width)
        await self.player.set_filters(filters)

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

class LowPass:
    """
    Class สำหรับจัดการฟิลเตอร์ LowPass
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ LowPass
    """
    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ LowPass
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player

    async def set(self, smoothing=20):
        """
        ตั้งค่าฟิลเตอร์ low_pass สำหรับ LowPass

        ฟังก์ชันนี้จะปรับค่าฟิลเตอร์ LowPass ตามที่ระบุ
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ผู้เล่น

        Args:
            smooting (float): ค่าความสมูทของเพลง (ค่าเริ่มต้น 20)
        """
        filters: wavelink.Filters = self.player.filters
        filters.low_pass.set(smoothing=smoothing)
        await self.player.set_filters(filters)