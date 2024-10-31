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
    
    async def set(self, speed=1.2, pitch=1.2, rate: float = 1):
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

class Distortion:
    """
    Class สำหรับจัดการฟิลเตอร์ Distortion
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ Distortion
    """
    def __init__(self, player: wavelink.Player):
        """
        กำหนดค่าเริ่มต้นให้กับ Distortion
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player
    
    async def set(self, sin_offset=0.05, sin_scale=0.2, cos_offset=0.05, cos_scale=0.2, tan_offset=0.0, tan_scale=0.1, offset=0.0, scale=0.5):
        """
        ตั้งค่าฟิลเตอร์ Distortion สำหรับเสียง

        ฟังก์ชันนี้จะปรับค่าฟิลเตอร์ Distortion ตามที่ระบุ
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ในผู้เล่น

        Args:
            sin_offset (float): ค่าการปรับ sin offset (ค่าเริ่มต้น 0.05)
            sin_scale (float): ค่าการปรับ sin scale (ค่าเริ่มต้น 0.2)
            cos_offset (float): ค่าการปรับ cos offset (ค่าเริ่มต้น 0.05)
            cos_scale (float): ค่าการปรับ cos scale (ค่าเริ่มต้น 0.2)
            tan_offset (float): ค่าการปรับ tan offset (ค่าเริ่มต้น 0.0)
            tan_scale (float): ค่าการปรับ tan scale (ค่าเริ่มต้น 0.1)
            offset (float): ค่าการปรับ offset (ค่าเริ่มต้น 0.0)
            scale (float): ค่าการปรับ scale (ค่าเริ่มต้น 0.5)
        """
        filters: wavelink.Filters = self.player.filters
        filters.distortion.set(
            sin_offset=sin_offset,
            sin_scale=sin_scale,
            cos_offset=cos_offset,
            cos_scale=cos_scale,
            tan_offset=tan_offset,
            tan_scale=tan_scale,
            offset=offset,
            scale=scale
        )
        await self.player.set_filters(filters)

class Termolo:
    """
    Class สำหรับจัดการฟิลเตอร์ Termolo
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ Termolo
    """
    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ Termolo
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player

    async def set(self, frequency=5.0, depth=0.7):
        """
        ตั้งค่าฟิลเตอร์ Tremolo สำหรับเสียง

        ฟังก์ชันนี้จะปรับค่าฟิลเตอร์ Tremolo ตามที่ระบุ
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ในผู้เล่น

        Args:
            frequency (float): ความถี่ของ tremolo (ค่าเริ่มต้น 5.0 Hz)
            depth (float): ความลึกของ tremolo (ค่าเริ่มต้น 0.7)
        """
        filters: wavelink.Filters = self.player.filters
        filters.tremolo.set(frequency=frequency, depth=depth)
        await self.player.set_filters(filters)

class SlowDown:
    """
    Class สำหรับจัดการฟิลเตอร์ SlowDown
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ SlowDown
    """
    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ SlowDown
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player
    
    async def set(self, speed=0.8, pitch=0.9, rate: float = 1):
        """
        ตั้งค่าฟิลเตอร์ timescale สำหรับ SlowDown

        ฟังก์ชันนี้จะปรับความเร็วและเสียงของเพลงตามที่ระบุ
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ผู้เล่น

        Args:
            speed (float): ค่าความเร็วของเพลง (ค่าเริ่มต้น 0.8)
            pitch (float): ค่าพิชของเสียง (ค่าเริ่มต้น 0.9)
            rate (float): ค่าระดับการเปลี่ยนแปลง (ค่าเริ่มต้น 1)
        """
        filters: wavelink.Filters = self.player.filters
        filters.timescale.set(speed=speed, pitch=pitch, rate=rate)
        await self.player.set_filters(filters)

class Rotation:
    """
    Class สำหรับจัดการฟิลเตอร์ Rotation
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ Rotation
    """
    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ Rotation
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player

    async def set(self, rotation_hz=0.2):
        """
        ตั้งค่าฟิลเตอร์สำหรับการหมุนเสียง Rotation

        ฟังก์ชันนี้จะปรับความถี่การหมุนของเสียงตามที่ระบุ
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ของผู้เล่น

        Args:
            rotation_hz (float): ความถี่การหมุนของเสียง (ค่าเริ่มต้น 0.2)
        """
        filters: wavelink.Filters = self.player.filters
        filters.rotation.set(rotation_hz=rotation_hz)
        await self.player.set_filters(filters)