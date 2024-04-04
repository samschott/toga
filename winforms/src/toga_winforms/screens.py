from ctypes import byref, c_void_p, windll, wintypes

from System.Drawing import (
    Bitmap,
    Graphics,
    Imaging,
    Point,
    Size,
)
from System.IO import MemoryStream

from toga.screens import Screen as ScreenInterface

from .widgets.base import Scalable


class Screen(Scalable):
    _instances = {}

    def __new__(cls, native):
        if native in cls._instances:
            return cls._instances[native]
        else:
            instance = super().__new__(cls)
            instance.interface = ScreenInterface(_impl=instance)
            instance.native = native
            cls._instances[native] = instance
            return instance

    @property
    def dpi_scale(self):
        screen_rect = wintypes.RECT(
            self.native.Bounds.Left,
            self.native.Bounds.Top,
            self.native.Bounds.Right,
            self.native.Bounds.Bottom,
        )
        windll.user32.MonitorFromRect.restype = c_void_p
        windll.user32.MonitorFromRect.argtypes = [wintypes.RECT, wintypes.DWORD]
        # MONITOR_DEFAULTTONEAREST = 2
        hMonitor = windll.user32.MonitorFromRect(screen_rect, 2)
        pScale = wintypes.UINT()
        windll.shcore.GetScaleFactorForMonitor(c_void_p(hMonitor), byref(pScale))
        return pScale.value / 100

    def get_name(self):
        name = self.native.DeviceName
        # WinForms Display naming convention is "\\.\DISPLAY1". Remove the
        # non-text part to prevent any errors due to non-escaped characters.
        return name.split("\\")[-1]

    def get_origin(self):
        return (
            self.scale_out(self.native.Bounds.X),
            self.scale_out(self.native.Bounds.Y),
        )

    def get_size(self):
        return (
            self.scale_out(self.native.Bounds.Width),
            self.scale_out(self.native.Bounds.Height),
        )

    def get_image_data(self):
        bitmap = Bitmap(*map(self.scale_in, self.get_size()))
        graphics = Graphics.FromImage(bitmap)
        source_point = Point(*map(self.scale_in, self.get_origin()))
        destination_point = Point(0, 0)
        copy_size = Size(*map(self.scale_in, self.get_size()))
        graphics.CopyFromScreen(source_point, destination_point, copy_size)
        stream = MemoryStream()
        bitmap.Save(stream, Imaging.ImageFormat.Png)
        return bytes(stream.ToArray())
