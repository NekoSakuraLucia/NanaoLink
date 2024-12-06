import wavelink
from dataclasses import dataclass
from typing import Dict, Any, Union


@dataclass
class InfoTrack:
    """
    คลาสนี้เก็บข้อมูลเกี่ยวกับแทร็กเพลงที่มีคุณสมบัติที่จำเป็น\n
    ในการแสดงข้อมูลเพลง\n
    เช่น ชื่อเพลง, อัลบั้ม, ศิลปิน, ภาพปก,
    ผู้แต่ง และระยะเวลา, แหล่งที่มา, ลิงก์ของแทร็ก, ระยะเวลาเริ่มต้น

    Attributes:
        title (str): ชื่อของเพลง
        album (str): ชื่อของอัลบั้มที่เพลงนี้มาจาก
        artist (str): ชื่อของศิลปินที่แสดงเพลงนี้
        artwork (str): URL หรือข้อมูลของภาพปกเพลง
        author (str): ผู้แต่งเพลง หรือผู้เขียนเนื้อเพลง
        duration (int): ระยะเวลา (มิลลิวินาที) ของเพลง
        uri (str): ลิงก์ URL ของแทร็กปัจจุบัน
        sourceName (str): แหล่งที่มาปัจจุบันของแทร็ก
        position (int): ระยะเวลาเริ่มต้นของแทร็ก
    """

    title: str
    """ส่งชื่อ/ชื่อของแทร็กนี้"""
    album: str
    """ส่งอัลบั้มสำหรับแทร็กนี้"""
    artist: str
    """ส่งศิลปินสำหรับแทร็กนี้"""
    artwork: str
    """ส่ง URL หรือข้อมูลของภาพปกเพลง"""
    author: str
    """ส่งผู้แต่งเพลง หรือผู้เขียนเนื้อเพลง"""
    duration: int
    """ส่งระยะเวลาทั้งหมดของเพลง (มิลลิวินาที)"""
    uri: str
    """ส่งลิงก์ URL ของแทร็กปัจจุบัน"""
    sourceName: str
    """ส่งแหล่งที่มาปัจจุบันของแทร็กเช่น Youtube หรือ Spotify"""
    position: int
    """ส่งระยะเวลาของแทร็กปัจจุบัน (มิลลิวินาที)"""


class InfoTrack_Class(wavelink.Playable):
    """
    คลาสสำหรับจัดการข้อมูลแทร็กเพลงที่ได้รับจาก Playable\n
    ซึ่งจะเก็บข้อมูลต่างๆ ที่เกี่ยวข้องกับแทร็กเพลง\n
    เช่น ชื่อแทร็ก, อัลบั้ม, ศิลปิน, ภาพปก, เวลาแทร็ก, แหล่งที่มา, ลิงก์ของแทร็ก, ระยะเวลาเริ่มต้น และข้อมูลดิบ
    """

    def __init__(
        self,
        title: str,
        album: str,
        artwork: str,
        author: str,
        duration: int,
        uri: str,
        sourceName: str,
        position: int,
        data: Union[Dict, Any],
    ):
        """
        กำหนดค่าเริ่มต้นสำหรับข้อมูลแทร็กเพลง

        Args:
            title (str): ชื่อของแทร็กเพลง
            album (str): ชื่ออัลบั้มของแทร็ก
            artwork (str): URL ของภาพหน้าปก
            author (str): ชื่อผู้แต่งหรือศิลปิน
            data (Union[Dict, Any]): ข้อมูลดิบที่มาจาก Wavelink ซึ่งอาจจะเป็น dict หรือประเภทอื่น
            duration (int): เวลาปัจจุบันของแทร็ก
            uri (str): ลิงก์ของแทร็กปัจจุบัน
            source (str): แหล่งที่มาปัจจุบันของแทร็ก
            position (int): ระยะเวลาเริ่มต้นของแทร็ก
        """
        super().__init__(data)
        self._title = title
        self._album = album
        self._artwork = artwork
        self._author = author
        self._duration = duration
        self._uri = uri
        self._source = sourceName
        self._position = position
        self.data = data
        self._info = None

    @property
    def title(self):
        """
        รับค่าชื่อของแทร็ก

        คืนค่าชื่อแทร็กจากตัวแปร _title ซึ่งถูกกำหนดใน constructor

        Returns:
            str: ชื่อของแทร็ก
        """
        return self._title

    @title.setter
    def title(self, value: str):
        """
        ตั้งค่าชื่อของแทร็ก

        กำหนดค่าชื่อแทร็กใหม่ให้กับตัวแปร _title

        Args:
            value (str): ชื่อของแทร็กที่ต้องการตั้งค่าใหม่
        """
        self._title = value

    @property
    def album(self):
        """
        รับค่าอัลบัมของแทร็ก

        คืนค่าชื่ออัลบัมจากตัวแปร _album ซึ่งถูกกำหนดใน constructor

        Returns:
            str: ชื่อของอัลบัม
        """
        return self._album

    @album.setter
    def album(self, value: str):
        """
        ตั้งค่าอัลบัมของแทร็ก

        กำหนดค่าอัลบัมใหม่ให้กับตัวแปร _album

        Args:
            value (str): ชื่อของอัลบัมที่ต้องการตั้งค่าใหม่
        """
        self._album = value

    @property
    def artwork(self):
        """
        รับค่า artwork ของแทร็ก

        คืนค่าภาพปกอัลบัมหรือ artwork ของแทร็กจากตัวแปร _artwork

        Returns:
            str: ลิงก์ไปยังภาพ artwork ของแทร็ก
        """
        return self._artwork

    @artwork.setter
    def artwork(self, value: str):
        """
        ตั้งค่า artwork ของแทร็ก

        กำหนดค่า artwork ใหม่ให้กับตัวแปร _artwork

        Args:
            value (str): ลิงก์ของ artwork ที่ต้องการตั้งค่าใหม่
        """
        self._artwork = value

    @property
    def author(self):
        """
        รับค่าผู้แต่ง (author) ของแทร็ก

        คืนค่าชื่อผู้แต่งจากตัวแปร _author ซึ่งถูกกำหนดใน constructor

        Returns:
            str: ชื่อผู้แต่งของแทร็ก
        """
        return self._author

    @author.setter
    def author(self, value: str):
        """
        ตั้งค่าผู้แต่ง (author) ของแทร็ก

        กำหนดชื่อผู้แต่งใหม่ให้กับตัวแปร _author

        Args:
            value (str): ชื่อของผู้แต่งที่ต้องการตั้งค่าใหม่
        """
        self._author = value

    @property
    def duration(self):
        """
        รับค่าเวลา (duration) ของแทร็ก

        คืนค่าเวลาจากตัวแปร _duration ซึ่งถูกกำหนดใน constructor

        Returns:
            int: เวลาปัจจุบันของแทร็ก
        """
        return self._duration

    @duration.setter
    def duration(self, value: int):
        """
        ตั้งค่าให้กับเวลา (duration) ของแทร็ก

        กำหนดชื่อเวลาใหม่ให้กับตัวแปร _duration

        Args:
            value (int): เวลาของเพลงที่ต้องการตั้งค่าใหม่
        """
        self._duration = value

    @property
    def sourceName(self):
        """
        รับค่าแหล่งที่มา (sourceName) ของแทร็ก

        คืนค่าแหล่งที่มาจากตัวแปร _source ซึ่งถูกกำหนดใน constructor

        Returns:
            str: แหล่งที่มาของปัจจุบันของแทร็ก
        """
        return self._source

    @sourceName.setter
    def sourceName(self, value: str):
        """
        ตั้งค่าให้กับแหล่งที่มา (sourceName) ของแทร็ก

        กำหนดชื่อแหล่งที่มาใหม่ให้กับตัวแปร _source

        Args:
            value (str): แหล่งที่มาของปัจจุบันของแทร็ก
        """
        self._source = value

    @property
    def uri(self):
        """
        รับค่าลิงก์ล่าสุด (uri) ของแทร็ก

        คืนค่าลิงก์แทร็กจากตัวแปร _uri ซึ่งถูกกำหนดใน constructor

        Returns:
            str: ลิงก์ล่าสุดของแทร็ก
        """
        return self._uri

    @uri.setter
    def uri(self, value: str):
        """
        ตั้งค่าให้กับลิงก์ล่าสุด (uri) ของแทร็ก

        กำหนดชื่อลิงก์ล่าสุดใหม่ให้กับตัวแปร _uri

        Args:
            value (str): ลิงก์ล่าสุดของแทร็ก
        """
        self._uri = value

    @property
    def position(self):
        """
        รับค่าเวลาเริ่มต้น (position) ของแทร็ก

        คืนค่าระยะเวลาเริ่มต้นจากตัวแปร _position ซึ่งถูกกำหนดใน constructor

        Returns:
            int: ระยะเวลาปัจจุบันที่เพลงกำลังเล่น
        """
        return self._position

    @position.setter
    def position(self, value: int):
        """
        ตั้งค่าให้กับเวลาปัจจุบัน (position) ของแทร็ก

        กำหนดระยะเวลาเริ่มต้นให้กับตัวแปร _position

        Args:
            value (int): ระยะเวลาปัจจุบันที่เพลงกำลังเล่น
        """
        self._position = value

    @property
    def info(self) -> InfoTrack:
        """
        คืนค่าข้อมูลทั้งหมดของแทร็กในรูปแบบ InfoTrack

        ถ้าข้อมูล info ยังไม่ถูกตั้งค่า จะทำการสร้าง InfoTrack ใหม่และเก็บไว้ใน _info
        ข้อมูลที่คืนมาจะรวมถึงชื่อแทร็ก, อัลบัม, ผู้แต่ง, artwork, ลิงก์ของแทร็ก, แหล่งที่มา, ระยะเวลาเริ่มต้น และข้อมูลอื่นๆ ที่เกี่ยวข้อง

        Returns:
            InfoTrack: ข้อมูลของแทร็กในรูปแบบ InfoTrack

        Note:
            ถ้าไม่มีการตั้งค่าข้อมูลของแทร็ก อาจทำให้เกิดข้อผิดพลาด
        """
        if not self._info:
            self._info = InfoTrack(
                title=self._title,
                album=self._album,
                artist=self._author,  # ใช้ author หรือ artist ขึ้นอยู่กับความต้องการ
                artwork=self._artwork,
                author=self._author,
                duration=self._duration,
                uri=self._uri,
                sourceName=self._source,
                position=self._position,
            )
        return self._info
