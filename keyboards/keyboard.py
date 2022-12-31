from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Start button
sb = KeyboardButton("/start")
kbsbcb = ReplyKeyboardMarkup(resize_keyboard=True)
kbsbcb.add(sb)


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
bl1 = KeyboardButton("/Низкий")
bl2 = KeyboardButton("/Средний")
bl3 = KeyboardButton("/Высокий")

kbl = ReplyKeyboardMarkup(resize_keyboard=True)

kbl.add(bl1, bl2, bl3)


# A user chooses a topic from easy themes
all_bt_e = [
    "/a_room_for_one_night",
    "/ordering_pizza_into_a_hotel",
    "/decoration_of_a_Christmas_tree",
    "/coming_to_a_new_city",
    "/topic_easy5",
    "/topic_easy6",
    "/topic_easy7",
    "/topic_easy8",
    "/topic_easy9",
    "/topic_easy10"
]

kbt_e = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

kbt_e.add(*all_bt_e)


# A user chooses a topic from medium themes
all_bt_m = [
    "/at_the_market",
    "/headache",
    "/car_navigator",
    "/in_New_York",
    "/at_the_restaurant",
    "/topic_medium6",
    "/topic_medium7",
    "/topic_medium8",
    "/topic_medium9",
    "/topic_medium10"
]

kbt_m = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

kbt_m.add(*all_bt_m)


# A user chooses a topic from hard themes
all_bt_h = [
    "/cooking_a_sponge_cake",
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

kbt_h.add(*all_bt_h)


# A user decides to start learning
bt_start_learning = KeyboardButton("Начать заниматься")
kb_start_learning = ReplyKeyboardMarkup(resize_keyboard=True)
kb_start_learning.add(bt_start_learning)
