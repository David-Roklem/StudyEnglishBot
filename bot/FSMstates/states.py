from aiogram.filters.state import State, StatesGroup


# class States(StatesGroup):
#     level = State()
#     topic = State()
#     show_whole_text = State()
#     q_1 = State()
#     q_2 = State()
#     q_3 = State()
#     q_4 = State()
#     q_5 = State()
#     q_6 = State()
#     q_7 = State()
#     q_8 = State()
#     q_9 = State()
#     q_10 = State()

class StartMenu(StatesGroup):
    START_MENU = State()


class Exercise(StatesGroup):
    START_MENU = State()
    A1 = State()
    A2 = State()
    B1 = State()
    B2 = State()
    C1 = State()
