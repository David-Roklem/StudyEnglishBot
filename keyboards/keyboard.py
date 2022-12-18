from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Start button
sb = KeyboardButton("/start")
cb = KeyboardButton("/cancel")
kbsbcb = ReplyKeyboardMarkup(resize_keyboard=True)
kbsbcb.add(sb).add(cb)


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
bt_e1 = KeyboardButton("/topic_easy1")
bt_e2 = KeyboardButton("/topic_easy2")
bt_e3 = KeyboardButton("/topic_easy3")
bt_e4 = KeyboardButton("/topic_easy4 djjdjsl lsll ")
bt_e5 = KeyboardButton("/topic_easy5skkks kskkls")
bt_e6 = KeyboardButton("/topic_easy6")
bt_e7 = KeyboardButton("/topic_easy7")
bt_e8 = KeyboardButton("/topic_easy8")
bt_e9 = KeyboardButton("/topic_easy9 slslo 12 slls")
bt_e10 = KeyboardButton("/topic_easy10")
bt_e11 = KeyboardButton("/topic_easy11")
bt_e12 = KeyboardButton("/topic_easy12")
bt_e13 = KeyboardButton("/topic_easy13")
bt_e14 = KeyboardButton("/topic_easy14")
bt_e15 = KeyboardButton("/topic_easy15")
bt_e16 = KeyboardButton("/topic_easy16")
bt_e17 = KeyboardButton("/topic_easy17")


kbt_e = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

kbt_e.add(bt_e0).add(bt_e1, bt_e2, bt_e3, bt_e4, bt_e5, bt_e6, bt_e7, bt_e8,\
                    bt_e9, bt_e10, bt_e11, bt_e12, bt_e13, bt_e14, bt_e15, bt_e16, bt_e17)


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
bt_cancel_command = KeyboardButton("/cancel")
kb_start_learning = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start_learning.add(bt_start_learning).add(bt_cancel_command)
