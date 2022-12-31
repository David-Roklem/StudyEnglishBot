from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Start button
sb = KeyboardButton("/start")
cb = KeyboardButton("/cancel")
kbsbcb = ReplyKeyboardMarkup(resize_keyboard=True)
kbsbcb.add(sb).add(cb)


# Check if the user really intends to cancel test
bt_yes = KeyboardButton("Выйти из теста")
bt_no = KeyboardButton("Продолжить тест")
kbyesno = ReplyKeyboardMarkup(resize_keyboard=True)
kbyesno.add(bt_yes, bt_no)


# Cancel_command_button
ccb = KeyboardButton("/cancel")
kccb = ReplyKeyboardMarkup(resize_keyboard=True)
kccb.add(ccb)


# A user chooses a level
bl0 = KeyboardButton("/cancel")
bl1 = KeyboardButton("/Низкий")
bl2 = KeyboardButton("/Средний")
bl3 = KeyboardButton("/Высокий")

kbl = ReplyKeyboardMarkup(resize_keyboard=True)

kbl.add(bl0).add(bl1, bl2, bl3)


# A user chooses a topic from easy themes
bt_e0 = KeyboardButton("/cancel")
all_bt_e = [
    "/topic_easy1",
    "/topic_easy2",
    "/topic_easy3",
    "/topic_easy4",
    "/topic_easy5",
    "/topic_easy6",
    "/topic_easy7",
    "/topic_easy8",
    "/topic_easy9",
    "/topic_easy10"
]

kbt_e = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

kbt_e.add(bt_e0).add(*all_bt_e)


# A user chooses a topic from medium themes
bt_m0 = KeyboardButton("/cancel")
all_bt_m = [
    "/topic_medium1",
    "/topic_medium2",
    "/topic_medium3",
    "/topic_medium4",
    "/topic_medium5",
    "/topic_medium6",
    "/topic_medium7",
    "/topic_medium8",
    "/topic_medium9",
    "/topic_medium10"
]

kbt_m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

kbt_m.add(bt_m0).add(*all_bt_m)


# A user chooses a topic from hard themes
bt_h0 = KeyboardButton("/cancel")
all_bt_h = [
    "/topic_hard1",
    "/topic_hard2",
    "/topic_hard3",
    "/topic_hard4",
    "/topic_hard5",
    "/topic_hard6",
    "/topic_hard7",
    "/topic_hard8",
    "/topic_hard9",
    "/topic_hard10"
]

kbt_h = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

kbt_h.add(bt_h0).add(*all_bt_h)


# A user decides to start learning
bt_start_learning = KeyboardButton("Начать заниматься")
kb_start_learning = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start_learning.add(bt_start_learning)
