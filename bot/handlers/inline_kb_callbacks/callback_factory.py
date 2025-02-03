from enum import Enum
from aiogram.filters.callback_data import CallbackData


class Level(str, Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"


class LevelCallbackFactory(CallbackData, prefix="exercise"):
    lvl: Level
