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
        filters.karaoke.set(
            level=level,
            mono_level=mono_level,
            filter_band=filter_band,
            filter_width=filter_width,
        )
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

    async def set(
        self,
        sin_offset=0.05,
        sin_scale=0.2,
        cos_offset=0.05,
        cos_scale=0.2,
        tan_offset=0.0,
        tan_scale=0.1,
        offset=0.0,
        scale=0.5,
    ):
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
            scale=scale,
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


class Vibrato:
    """
    Class สำหรับจัดการฟิลเตอร์ Vibrato
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ Vibrato
    """

    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ Vibrato
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player

    async def set(self, frequency: float = 6.0, depth: float = 0.4):
        """
        ตั้งค่าฟิลเตอร์สำหรับการหมุนเสียง Vibrato

        ฟังก์ชันนี้จะปรับความถี่การหมุนของเสียงตามที่ระบุ
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ของผู้เล่น

        Args:
            frequency (float): ความถี่การสั่นของเสียง (ค่าเริ่มต้น 6.0)
            depth (float): ความลึกของการสั้น (ค่าเริ่มต้น 0.4)
        """
        filters: wavelink.Filters = self.player.filters
        filters.vibrato.set(frequency=frequency, depth=depth)
        await self.player.set_filters(filters)


class ChannelMix:
    """
    Class สำหรับจัดการฟิลเตอร์ ChannelMix
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ ChannelMix
    """

    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ ChannelMix
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player

    async def set(
        self,
        left_to_left: float = 0.7,
        left_to_right: float = 0.2,
        right_to_left: float = 0.2,
        right_to_right: float = 0.7,
    ):
        """
        ตั้งค่าฟิลเตอร์ ChannelMix สำหรับการผสมเสียงระหว่างช่องซ้ายและขวา

        ฟังก์ชันนี้จะปรับการผสมเสียงจากช่องซ้ายไปช่องขวาและจากช่องขวาไปช่องซ้าย\n
        โดยใช้ค่าที่ระบุในพารามิเตอร์ และเรียกใช้ฟังก์ชัน set_filters\n
        เพื่ออัปเดตฟิลเตอร์ของผู้เล่น

        Args:
            left_to_left (float): ค่าที่ผสมเสียงจากช่องซ้ายไปช่องซ้าย (ค่าเริ่มต้น 0.7)
            left_to_right (float): ค่าที่ผสมเสียงจากช่องซ้ายไปช่องขวา (ค่าเริ่มต้น 0.2)
            right_to_left (float): ค่าที่ผสมเสียงจากช่องขวาไปช่องซ้าย (ค่าเริ่มต้น 0.2)
            right_to_right (float): ค่าที่ผสมเสียงจากช่องขวาไปช่องขวา (ค่าเริ่มต้น 0.7)
        """
        filters: wavelink.Filters = self.player.filters
        filters.channel_mix.set(
            left_to_left=left_to_left,
            left_to_right=left_to_right,
            right_to_left=right_to_left,
            right_to_right=right_to_right,
        )
        await self.player.set_filters(filters)


class Equalizer:
    """
    Class สำหรับจัดการฟิลเตอร์ Equalizer
    ซึ่งใช้เพื่อปรับค่าฟิลเตอร์ Equalizer
    """

    def __init__(self, player: wavelink.Player) -> None:
        """
        กำหนดค่าเริ่มต้นให้กับ Equalizer
        Args:
            player (wavelink.Player): อ็อบเจกต์ผู้เล่นที่ต้องการใช้ฟิลเตอร์
        """
        self.player = player

    async def set(self, level: float = 0.5):
        """
        ตั้งค่าฟิลเตอร์ Equalizer สำหรับการเพิ่มเสียงเบส (Bass Boost) แบบพอดี

        ฟังก์ชันนี้จะปรับค่า Equalizer เพื่อเพิ่มเสียงเบสตามค่าระดับที่ระบุ\n
        และเรียกใช้ฟังก์ชัน set_filters เพื่ออัปเดตฟิลเตอร์ของผู้เล่น

        Args:
            level (float): ระดับของ Bass Boost (ค่าเริ่มต้น 0.5, สูงสุดที่ 1.0)
        """
        bands = [
            {"band": 0, "gain": level},  # Band 0 (เบส) เพิ่มค่าความแรงตาม level
            {"band": 1, "gain": level * 0.6},  # Band 1 (เบสต่ำ) เพิ่มค่าความแรงในระดับพอดี
            {"band": 2, "gain": level * 0.3},  # Band 2 (ต่ำ) เสริมเล็กน้อย
            {"band": 3, "gain": 0.0},  # Band 3, 4, 5 ไม่มีการปรับ
            {"band": 4, "gain": 0.0},
            {"band": 5, "gain": 0.0},
            {"band": 6, "gain": 0.0},
            {"band": 7, "gain": 0.0},
            {"band": 8, "gain": 0.0},
            {"band": 9, "gain": 0.0},
            {"band": 10, "gain": 0.0},
            {"band": 11, "gain": 0.0},
            {"band": 12, "gain": 0.0},
            {"band": 13, "gain": 0.0},
            {"band": 14, "gain": 0.0},
        ]
        filters: wavelink.Filters = self.player.filters
        filters.equalizer.set(bands=bands)
        await self.player.set_filters(filters)
