import re
from aiogram import types, Dispatcher
from aiogram.filters import Command
from config import dp, router
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.types import ReplyKeyboardRemove
# from keyboards.keyboard import kbsbcb, kbl, kbt_e, kbt_m, kbt_h, kb_start_learning, kccb, kbyesno
# from FSMstates.states import States
from topics_all import list_of_topics
# import texts




# @router.message_handler(state='*', commands='cancel')
# @router.message_handler(Text(equals='cancel', ignore_case=True), state='*')
# async def cmd_cancel(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await message.answer('<b>Вы уверены, что хотите выйти из теста?</b>', reply_markup=kbyesno, parse_mode="HTML")
#     await message.delete()


# @dp.message_handler(Text(equals='Выйти из теста', ignore_case=False), state='*')
# async def cmd_cancel_exit(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.answer('<b>Вы вышли из теста</b>', reply_markup=kbsbcb, parse_mode="HTML")


# @dp.message_handler(Text(equals='Продолжить тест', ignore_case=False), state='*')
# async def cmd_cancel_stay(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await message.answer('<b>Тест продолжается. Впишите сюда⬇️ ваш ответ на последний вопрос</b>',
#     reply_markup=kccb, parse_mode="HTML")
#     await message.delete()


# # @dp.message_handler(commands=['низкий', 'средний', 'высокий'], state=States.level)
# async def cmd_choose_level(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_level'] = message.text
#     if data['user_level'] == '/Низкий':
#         await message.answer("<b>Теперь выберите топик:</b>", reply_markup=kbt_e, parse_mode="HTML")
#     elif data['user_level'] == '/Средний':
#         await message.answer("<b>Теперь выберите топик:</b>", reply_markup=kbt_m, parse_mode="HTML")
#     else:
#         await message.answer("<b>Теперь выберите топик:</b>", reply_markup=kbt_h, parse_mode="HTML")
#     await States.next()


# # @dp.message_handler(commands=list_of_topics, state=States.topic)
# async def determine_topic_and_show_first_question(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['user_topic'] = message.text
#     if data["user_level"] == '/Низкий':
#         async with state.proxy() as data:
#             data['path'] = 'texts.topics_easy' + '.' + data["user_topic"][1::]
#             data['module'] = eval(data['path'])
#     elif data["user_level"] == '/Средний':
#         async with state.proxy() as data:
#             data['path'] = 'texts.topics_medium' + '.' + data["user_topic"][1::]
#             data['module'] = eval(data['path'])
#     else:
#         async with state.proxy() as data:
#             data['path'] = 'texts.topics_hard' + '.' + data["user_topic"][1::]
#             data['module'] = eval(data['path'])
#     async with state.proxy() as data:
#         data['score'] = 0
#     await message.answer(f'''<i>Начнём. Вот весь текст для ознакомления.</i>
#     {data['module'][0]}''', reply_markup=kb_start_learning, parse_mode="HTML")
#     await States.next()


# # @dp.message_handler(Text(equals='Начать заниматься', ignore_case=True), state=States.show_whole_text)
# async def begin_learning(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 1
#         await message.answer(f"1️⃣ {data['module'][1][0]}", reply_markup=kccb)
#         if len(data['module'][1]) == 3:
#             if "hint" in data['module'][1][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][1][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][1][2].keys():
#                 await message.answer(data['module'][1][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_1)
# async def process_q_1(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 2
#         data['all_answers_lowered_q_1'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][1][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_1']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][1][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"2️⃣ {data['module'][2][0]}", reply_markup=kccb)
#         if len(data['module'][2]) == 3:
#             if "hint" in data['module'][2][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][2][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][2][2].keys():
#                 await message.answer(data['module'][2][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_2)
# async def process_q_2(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 3
#         data['all_answers_lowered_q_2'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][2][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_2']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][2][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"3️⃣ {data['module'][3][0]}", reply_markup=kccb)
#         if len(data['module'][3]) == 3:
#             if "hint" in data['module'][3][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][3][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][3][2].keys():
#                 await message.answer(data['module'][3][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_3)
# async def process_q_3(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 4
#         data['all_answers_lowered_q_3'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][3][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_3']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][3][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"4️⃣ {data['module'][4][0]}", reply_markup=kccb)
#         if len(data['module'][4]) == 3:
#             if "hint" in data['module'][4][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][4][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][4][2].keys():
#                 await message.answer(data['module'][4][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_4)
# async def process_q_4(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 5
#         data['all_answers_lowered_q_4'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][4][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_4']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][4][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"5️⃣ {data['module'][5][0]}", reply_markup=kccb)
#         if len(data['module'][5]) == 3:
#             if "hint" in data['module'][5][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][5][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][5][2].keys():
#                 await message.answer(data['module'][5][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_5)
# async def process_q_5(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 6
#         data['all_answers_lowered_q_5'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][5][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_5']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][5][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"6️⃣ {data['module'][6][0]}", reply_markup=kccb)
#         if len(data['module'][6]) == 3:
#             if "hint" in data['module'][6][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][6][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][6][2].keys():
#                 await message.answer(data['module'][6][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_6)
# async def process_q_6(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 7
#         data['all_answers_lowered_q_6'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][6][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_6']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][6][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"7️⃣ {data['module'][7][0]}", reply_markup=kccb)
#         if len(data['module'][7]) == 3:
#             if "hint" in data['module'][7][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][7][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][7][2].keys():
#                 await message.answer(data['module'][7][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_7)
# async def process_q_7(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 8
#         data['all_answers_lowered_q_7'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][7][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_7']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][7][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"8️⃣ {data['module'][8][0]}", reply_markup=kccb)
#         if len(data['module'][8]) == 3:
#             if "hint" in data['module'][8][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][8][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][8][2].keys():
#                 await message.answer(data['module'][8][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_8)
# async def process_q_8(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 9
#         data['all_answers_lowered_q_8'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][8][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_8']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][8][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"9️⃣ {data['module'][9][0]}", reply_markup=kccb)
#         if len(data['module'][9]) == 3:
#             if "hint" in data['module'][9][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][9][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][9][2].keys():
#                 await message.answer(data['module'][9][2].get('for_info'), reply_markup=kccb)
#     await States.next()
# # {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>to offer, farmer's pizza</u></b> |"}

# @dp.message_handler(state=States.q_9)
# async def process_q_9(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 10
#         data['all_answers_lowered_q_9'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][9][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in  data['all_answers_lowered_q_9']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][9][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"🔟 {data['module'][10][0]}", reply_markup=kccb)
#         if len(data['module'][10]) == 3:
#             if "hint" in data['module'][10][2].keys():
#                 await message.answer(
#                     f'| <i>Подсказка</i>☝️: используйте <b><u>{data["module"][10][2].get("hint")}</u></b> |',
#                     reply_markup=kccb, parse_mode="HTML")
#             if "for_info" in data['module'][10][2].keys():
#                 await message.answer(data['module'][10][2].get('for_info'), reply_markup=kccb)
#     await States.next()


# @dp.message_handler(state=States.q_10)
# async def process_q_10(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['current_question_number'] = 10
#         data['all_answers_lowered_q_10'] = list((re.sub("[^A-Za-z0-9]", "", i.lower()) for i in data['module'][10][1]))
#         if re.sub("[^A-Za-z0-9]", "", message.text.lower()) in data['all_answers_lowered_q_10']:
#             await message.reply("Правильно! 😃🥳")
#             data['score'] += 1
#         else:
#             await message.reply(f"К сожалению, ответ неверный...😔 Один из возможных вариантов: <b>{data['module'][10][1][0]}</b>",
#             parse_mode="HTML")
#         await message.answer(f"Ваш результат: <b>{data['score']} из {len(data['module']) - 1}</b>", 
#         parse_mode="HTML", reply_markup=kbsbcb)
#     await state.finish()


# def register_all_handlers(dp: Dispatcher):
#     dp.register_message_handler(cmd_start, commands='start', state=None)
#     # dp.register_message_handler(cmd_cancel, state='*', commands=['cancel'])
#     # dp.register_message_handler(cmd_cancel, Text(equals='cancel', ignore_case=True), state='*')
#     # dp.register_message_handler(cmd_cancel_exit, Text(equals='Выйти из теста', ignore_case=False), state='*')
#     # dp.register_message_handler(cmd_cancel_stay, Text(equals='Продолжить тест', ignore_case=False), state='*')
#     dp.register_message_handler(cmd_choose_level, commands=['низкий', 'средний', 'высокий'], state=States.level)
#     dp.register_message_handler(determine_topic_and_show_first_question, commands=list_of_topics, state=States.topic)
#     dp.register_message_handler(begin_learning, Text(
#         equals='Начать заниматься', ignore_case=True), state=States.show_whole_text)
#     dp.register_message_handler(process_q_1, state=States.q_1)
#     dp.register_message_handler(process_q_2, state=States.q_2)
#     dp.register_message_handler(process_q_3, state=States.q_3)
#     dp.register_message_handler(process_q_4, state=States.q_4)
#     dp.register_message_handler(process_q_5, state=States.q_5)
#     dp.register_message_handler(process_q_6, state=States.q_6)
#     dp.register_message_handler(process_q_7, state=States.q_7)
#     dp.register_message_handler(process_q_8, state=States.q_8)
#     dp.register_message_handler(process_q_9, state=States.q_9)
#     dp.register_message_handler(process_q_10, state=States.q_10)