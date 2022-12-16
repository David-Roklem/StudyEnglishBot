from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Start button
sb = KeyboardButton("/start")
cb = KeyboardButton("/cancel")
kbsbcb = ReplyKeyboardMarkup(resize_keyboard=True)
kbsbcb.add(sb).add(cb)


# A user chooses a level
bl0 = KeyboardButton("/cancel")
bl1 = KeyboardButton("/Низкий")
bl2 = KeyboardButton("/Средний")
bl3 = KeyboardButton("/Высокий")

kbl = ReplyKeyboardMarkup(resize_keyboard=True)

kbl.add(bl0).add(bl1, bl2, bl3)


# A user chooses a topic from easy themes
bt_e0 = KeyboardButton("/cancel")
bt_e1 = KeyboardButton("/topic_easy1")
bt_e2 = KeyboardButton("/topic_easy2")
bt_e3 = KeyboardButton("/topic_easy3")

kbt_e = ReplyKeyboardMarkup(resize_keyboard=True)

kbt_e.add(bt_e0).add(bt_e1, bt_e2, bt_e3)


# A user chooses a topic from medium themes
bt_m0 = KeyboardButton("/cancel")
bt_m1 = KeyboardButton("/topic_medium1")
bt_m2 = KeyboardButton("/topic_medium2")
bt_m3 = KeyboardButton("/topic_medium3")

kbt_m = ReplyKeyboardMarkup(resize_keyboard=True)

kbt_m.add(bt_m0).add(bt_m1, bt_m2, bt_m3)


# A user chooses a topic from hard themes
bt_h0 = KeyboardButton("/cancel")
bt_h1 = KeyboardButton("/topic_hard1")
bt_h2 = KeyboardButton("/topic_hard2")
bt_h3 = KeyboardButton("/topic_hard3")

kbt_h = ReplyKeyboardMarkup(resize_keyboard=True)

kbt_h.add(bt_h0).add(bt_h1, bt_h2, bt_h3)


# A user decides to start learning
bt_start_learning = KeyboardButton("Начать заниматься")
kb_start_learning = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start_learning.add(bt_start_learning)
