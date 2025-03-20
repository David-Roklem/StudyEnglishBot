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
    MAIN = State()


class Exercise(StatesGroup):
    level = State()
    category = State()
    subcategory = State()


class ExactExercise(StatesGroup):
    MAIN = State()


class Usage(StatesGroup):
    MAIN = State()


class Book(StatesGroup):
    MAIN = State()


class Rating(StatesGroup):
    MAIN = State()


class LearnWords(StatesGroup):
    MAIN = State()


class Notifications(StatesGroup):
    MAIN = State()


class Feedback(StatesGroup):
    MAIN = State()
