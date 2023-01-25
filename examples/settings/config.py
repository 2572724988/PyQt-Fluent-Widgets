# coding:utf-8
from enum import Enum

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication, QFont
from qfluentwidgets import (qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator,
                            ColorConfigItem, OptionsValidator, RangeConfigItem, RangeValidator,
                            FolderListValidator, EnumSerializer, FolderValidator)


class SongQuality(Enum):
    """ Online song quality enumeration class """

    STANDARD = "Standard quality"
    HIGH = "High quality"
    SUPER = "Super quality"
    LOSSLESS = "Lossless quality"

    @staticmethod
    def values():
        return [q.value for q in SongQuality]


class MvQuality(Enum):
    """ MV quality enumeration class """

    FULL_HD = "Full HD"
    HD = "HD"
    SD = "SD"
    LD = "LD"

    @staticmethod
    def values():
        return [q.value for q in MvQuality]


class Config(QConfig):
    """ Config of application """

    # folders
    musicFolders = ConfigItem(
        "Folders", "LocalMusic", [], FolderListValidator())
    downloadFolder = ConfigItem(
        "Folders", "Download", "download", FolderValidator())

    # online
    onlineSongQuality = OptionsConfigItem(
        "Online", "SongQuality", SongQuality.STANDARD, OptionsValidator(SongQuality), EnumSerializer(SongQuality))
    onlinePageSize = RangeConfigItem(
        "Online", "PageSize", 30, RangeValidator(0, 50))
    onlineMvQuality = OptionsConfigItem(
        "Online", "MvQuality", MvQuality.FULL_HD, OptionsValidator(MvQuality), EnumSerializer(MvQuality))

    # main window
    enableAcrylicBackground = ConfigItem(
        "MainWindow", "EnableAcrylicBackground", False, BoolValidator())
    minimizeToTray = ConfigItem(
        "MainWindow", "MinimizeToTray", True, BoolValidator())
    playBarColor = ColorConfigItem("MainWindow", "PlayBarColor", "#225C7F")
    themeMode = OptionsConfigItem(
        "MainWindow", "ThemeMode", "Light", OptionsValidator(["Light", "Dark", "Auto"]), restart=True)
    recentPlaysNumber = RangeConfigItem(
        "MainWindow", "RecentPlayNumbers", 300, RangeValidator(10, 300))
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)

    # desktop lyric
    deskLyricHighlightColor = ColorConfigItem(
        "DesktopLyric", "HighlightColor", "#0099BC")
    deskLyricFontSize = RangeConfigItem(
        "DesktopLyric", "FontSize", 50, RangeValidator(15, 50))
    deskLyricStrokeSize = RangeConfigItem(
        "DesktopLyric", "StrokeSize", 5, RangeValidator(0, 20))
    deskLyricStrokeColor = ColorConfigItem(
        "DesktopLyric", "StrokeColor", Qt.black)
    deskLyricFontFamily = ConfigItem(
        "DesktopLyric", "FontFamily", "Microsoft YaHei")
    deskLyricAlignment = OptionsConfigItem(
        "DesktopLyric", "Alignment", "Center", OptionsValidator(["Center", "Left", "Right"]))

    # software update
    checkUpdateAtStartUp = ConfigItem(
        "Update", "CheckUpdateAtStartUp", True, BoolValidator())

    @property
    def desktopLyricFont(self):
        """ get the desktop lyric font """
        font = QFont(self.deskLyricFontFamily.value)
        font.setPixelSize(self.deskLyricFontSize.value)
        return font

    @desktopLyricFont.setter
    def desktopLyricFont(self, font: QFont):
        dpi = QGuiApplication.primaryScreen().logicalDotsPerInch()
        self.deskLyricFontFamily.value = font.family()
        self.deskLyricFontSize.value = max(15, int(font.pointSize()*dpi/72))
        self.save()


YEAR = 2023
AUTHOR = "zhiyiYo"
VERSION = "v0.0.1"
HELP_URL = "https://pyqt-fluent-widgets.readthedocs.io"
FEEDBACK_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/issues"
RELEASE_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/releases/latest"


cfg = Config()
qconfig.load('config/config.json', cfg)