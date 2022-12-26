from aiogram.utils.markdown import hlink


topic_medium1 = [
    """
    Доброе утро! Мне нужны свежие овощи.
    Доброе утро! Выбирайте, что понравится, все овощи у меня свежие.
    Тогда я возьму 2 килограмма помидоров и 2 киллограмма огурцов, и 3 перца.
    Возьмите еще морковь, она очень сладкая. Хорошо, вы уговорили меня, положите еще одну морковь.
    С вас 8 долларов. Где я могу купить яблоки?
    Пройдите прямо, а затем поверните направо после лавки с зеленью, там будут фрукты.
    Спасибо огромное! Хорошего дня! Спасибо!
    """,
    ("Доброе утро! Мне нужны свежие овощи",
    [
        "Good morning! I need fresh vegetables",
        "Good morning! I require fresh vegetables"
    ]),
    ("Доброе утро! Выбирайте, что понравится, все овощи у меня свежие",
    [
        "Good morning! Choose whatever you like, all my vegetables are fresh",
        "Good morning! Choose whatever you like, I have only fresh vegetables",
        "Good morning! Choose whatever you like, I've got only fresh vegetables",
        "Good morning! Choose whatever you like, I have got only fresh vegetables",
        "Good morning! Pick whatever you like, all my vegetables are fresh",
        "Good morning! Pick whatever you like, I have only fresh vegetables",
        "Good morning! Pick whatever you like, I've got only fresh vegetables",
        "Good morning! Pick whatever you like, I have got only fresh vegetables",
        "Good morning! Pick whatever you fancy, all my vegetables are fresh",
        "Good morning! Pick whatever you fancy, I have only fresh vegetables",
        "Good morning! Pick whatever you fancy, I've got only fresh vegetables",
        "Good morning! Pick whatever you fancy, I have got only fresh vegetables"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>wahtever</u></b> |"}),
    ("Тогда я возьму 2 килограмма помидоров и 2 киллограмма огурцов, и 3 перца",
    [
        "In that case I'll take 2 kilograms of tomatoes and 2 kilograms of cucumbers and 3 peppers",
        "In this case I'll take 2 kilograms of tomatoes and 2 kilograms of cucumbers and 3 peppers",
        "In that case I will take 2 kilograms of tomatoes and 2 kilograms of cucumbers and 3 peppers",
        "In this case I will take 2 kilograms of tomatoes and 2 kilograms of cucumbers and 3 peppers",
        "Then I'll take 2 kilograms of tomatoes and 2 kilograms of cucumbers and 3 peppers",
        "Then I'll take 2 kilograms of tomatoes and 2 kilograms of cucumbers and 3 peppers",
        "Then I will take 2 kilograms of tomatoes and 2 kilograms of cucumbers and 3 peppers",
        "Then I will take 2 kilograms of tomatoes and 2 kilograms of cucumbers and 3 peppers"
    ]),
    ("Возьмите еще морковь, она очень сладкая",
    [
        "Take carrot as well, it is very sweet",
        "Take carrot as well, it's very sweet",
        "Take carrot as well, it is really sweet",
        "Take carrot as well, it's really sweet",
        "Take also carrot, it is very sweet",
        "Take also carrot, it's very sweet",
        "Take also carrot, it is really sweet",
        "Take also carrot, it's really sweet",
    ]),
    ("Хорошо, вы уговорили меня, положите еще одну морковь",
    [
        "Ok, you convinced me, put also one carrot",
        "Ok, you convinced me, put also a carrot",
        "Ok, you've convinced me, put also one carrot",
        "Ok, you've convinced me, put also a carrot",
        "Ok, you have convinced me, put also one carrot",
        "Ok, you have convinced me, put also a carrot",
        "fine, you convinced me, put also one carrot",
        "fine, you convinced me, put also a carrot",
        "fine, you've convinced me, put also one carrot",
        "fine, you've convinced me, put also a carrot",
        "fine, you have convinced me, put also one carrot",
        "fine, you have convinced me, put also a carrot",
        "alright, you convinced me, put also one carrot",
        "alright, you convinced me, put also a carrot",
        "alright, you've convinced me, put also one carrot",
        "alright, you've convinced me, put also a carrot",
        "alright, you have convinced me, put also one carrot",
        "alright, you have convinced me, put also a carrot",
    ]),
    ("С вас 8 долларов",
    [
        "That'll be 8 dollars from you",
        "That will be 8 dollars from you"
        "That'll be 8 dollars",
        "That will be 8 dollars",
        "It'll be 8 dollars from you",
        "It will be 8 dollars from you"
        "It'll be 8 dollars",
        "It will be 8 dollars",
    ]),
    ("Где я могу приобрести яблоки?",
    [
        "Where can I purchase apples?",
        "Where could I purchase apples?"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>purchase</u></b> |"}),
    ("Пройдите прямо, а затем поверните направо после лавки с зеленью, там будут фрукты",
    [
        "Go straight and then turn right after a greenery stall, there'll be fruit",
        "Go ahead and then turn right after a greenery stall, there'll be fruit",
        "Go straight ahead and then turn right after a greenery stall, there'll be fruit",
        "Go forward and then turn right after a greenery stall, there'll be fruit",
        "Go straight forward and then turn right after a greenery stall, there'll be fruit",
        "Go straight and then turn right beyond a greenery stall, there'll be fruit",
        "Go ahead and then turn right beyond a greenery stall, there'll be fruit",
        "Go straight ahead and then turn right beyond a greenery stall, there'll be fruit",
        "Go forward and then turn right beyond a greenery stall, there'll be fruit",
        "Go straight forward and then turn right beyond a greenery stall, there'll be fruit",
        "Go straight and then turn right after a greenery stall, there'll be fruits",
        "Go ahead and then turn right after a greenery stall, there'll be fruits",
        "Go straight ahead and then turn right after a greenery stall, there'll be fruits",
        "Go forward and then turn right after a greenery stall, there'll be fruits",
        "Go straight forward and then turn right after a greenery stall, there'll be fruits",
        "Go straight and then turn right beyond a greenery stall, there'll be fruist",
        "Go ahead and then turn right beyond a greenery stall, there'll be fruits",
        "Go straight ahead and then turn right beyond a greenery stall, there'll be fruits",
        "Go forward and then turn right beyond a greenery stall, there'll be fruits",
        "Go straight forward and then turn right beyond a greenery stall, there'll be fruits",
        "Go straight and then turn right after a greenery stall, there will be fruit",
        "Go ahead and then turn right after a greenery stall, there will be fruit",
        "Go straight ahead and then turn right after a greenery stall, there will be fruit",
        "Go forward and then turn right after a greenery stall, there will be fruit",
        "Go straight forward and then turn right after a greenery stall, there will be fruit",
        "Go straight and then turn right beyond a greenery stall, there will be fruit",
        "Go ahead and then turn right beyond a greenery stall, there will be fruit",
        "Go straight ahead and then turn right beyond a greenery stall, there will be fruit",
        "Go forward and then turn right beyond a greenery stall, there will be fruit",
        "Go straight forward and then turn right beyond a greenery stall, there will be fruit",
        "Go straight and then turn right after a greenery stall, there will be fruits",
        "Go ahead and then turn right after a greenery stall, there will be fruits",
        "Go straight ahead and then turn right after a greenery stall, there will be fruits",
        "Go forward and then turn right after a greenery stall, there will be fruits",
        "Go straight forward and then turn right after a greenery stall, there will be fruits",
        "Go straight and then turn right beyond a greenery stall, there will be fruist",
        "Go ahead and then turn right beyond a greenery stall, there will be fruits",
        "Go straight ahead and then turn right beyond a greenery stall, there will be fruits",
        "Go forward and then turn right beyond a greenery stall, there will be fruits",
        "Go straight forward and then turn right beyond a greenery stall, there will be fruits",
        "Go straight and then turn right after a greenery shop, there'll be fruit",
        "Go ahead and then turn right after a greenery shop, there'll be fruit",
        "Go straight ahead and then turn right after a greenery shop, there'll be fruit",
        "Go forward and then turn right after a greenery shop, there'll be fruit",
        "Go straight forward and then turn right after a greenery shop, there'll be fruit",
        "Go straight and then turn right beyond a greenery shop, there'll be fruit",
        "Go ahead and then turn right beyond a greenery shop, there'll be fruit",
        "Go straight ahead and then turn right beyond a greenery shop, there'll be fruit",
        "Go forward and then turn right beyond a greenery shop, there'll be fruit",
        "Go straight forward and then turn right beyond a greenery shop, there'll be fruit",
        "Go straight and then turn right after a greenery shop, there'll be fruits",
        "Go ahead and then turn right after a greenery shop, there'll be fruits",
        "Go straight ahead and then turn right after a greenery shop, there'll be fruits",
        "Go forward and then turn right after a greenery shop, there'll be fruits",
        "Go straight forward and then turn right after a greenery shop, there'll be fruits",
        "Go straight and then turn right beyond a greenery shop, there'll be fruist",
        "Go ahead and then turn right beyond a greenery shop, there'll be fruits",
        "Go straight ahead and then turn right beyond a greenery shop, there'll be fruits",
        "Go forward and then turn right beyond a greenery shop, there'll be fruits",
        "Go straight forward and then turn right beyond a greenery shop, there'll be fruits",
        "Go straight and then turn right after a greenery shop, there will be fruit",
        "Go ahead and then turn right after a greenery shop, there will be fruit",
        "Go straight ahead and then turn right after a greenery shop, there will be fruit",
        "Go forward and then turn right after a greenery shop, there will be fruit",
        "Go straight forward and then turn right after a greenery shop, there will be fruit",
        "Go straight and then turn right beyond a greenery shop, there will be fruit",
        "Go ahead and then turn right beyond a greenery shop, there will be fruit",
        "Go straight ahead and then turn right beyond a greenery shop, there will be fruit",
        "Go forward and then turn right beyond a greenery shop, there will be fruit",
        "Go straight forward and then turn right beyond a greenery shop, there will be fruit",
        "Go straight and then turn right after a greenery shop, there will be fruits",
        "Go ahead and then turn right after a greenery shop, there will be fruits",
        "Go straight ahead and then turn right after a greenery shop, there will be fruits",
        "Go forward and then turn right after a greenery shop, there will be fruits",
        "Go straight forward and then turn right after a greenery shop, there will be fruits",
        "Go straight and then turn right beyond a greenery shop, there will be fruist",
        "Go ahead and then turn right beyond a greenery shop, there will be fruits",
        "Go straight ahead and then turn right beyond a greenery shop, there will be fruits",
        "Go forward and then turn right beyond a greenery shop, there will be fruits",
        "Go straight forward and then turn right beyond a greenery shop, there will be fruits",
    ]),
    ("Спасибо огромное! Хорошего дня!",
    [
        "Thanks a lot! Have a nice day!",
        "Thank you so much! Have a nice day!",
        "Thank you very much! Have a nice day!"
    ]),
    ("Спасибо!",
    [
        "Thanks!",
        "Thank you!"
    ])
]





topic_medium2 = [
    """
    - Добрый день! У меня с утра болит голова. Что вы можете мне предложить?
    - Здравствуйте! Вы мерили ваше давление? - Нет, у меня нет возможности.
    - Вы можете это сделать у нас в аптеке. - Пожалуйста, присядьте здесь и протяните мне правую руку.
    - Ваше давление в норме. Без рецепта я могу вам предложить «ибупрофен».
    - Я раньше никогда не принимала его. - Это хорошее лекарство и оно поможет вам в течение 15 минут.
    - Можно мне еще бутылку воды. - Конечно! С вас 2 доллара 80 центов.
    """,
    ("Добрый день! У меня с утра болит голова. Что вы можете мне предложить?",
    [
        "Good afternoon! I have got a headache since the morning. What can you offer?",
        "Good afternoon! I have a headache from the morning. What can you offer?",
        "Good afternoon! I have got a headache from the morning. What can you offer?",
        "Good afternoon! I've got a headache from the morning. What can you offer?",
        "Good afternoon! I have a headache since the morning. What can you offer?",
        "Good afternoon! I've got a headache since the morning. What can you offer?",
        "Good afternoon! I have a headache since morning. What can you offer?",
        "Good afternoon! I have got a headache since morning. What can you offer?",
        "Good afternoon! I've got a headache since morning. What can you offer?",
        "Good day! I have a headache from the morning. What can you offer?",
        "Good day! I have got a headache from the morning. What can you offer?",
        "Good day! I've got a headache from the morning. What can you offer?",
        "Good day! I have a headache since the morning. What can you offer?",
        "Good day! I have got a headache since the morning. What can you offer?",
        "Good day! I've got a headache since the morning. What can you offer?",
        "Good day! I have a headache since morning. What can you offer?",
        "Good day! I have got a headache since morning. What can you offer?",
        "Good day! I've got a headache since morning. What can you offer?",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>to offer</u></b> |"}),
    ("Здравствуйте! Вы мерили ваше давление?",
    [
        "Hello! Did you measure your blood pressure?",
        "Good afternoon! Did you measure your blood pressure?",
        "Hello! Have you measured your blood pressure?",
        "Good afternoon! Have you measured your blood pressure?",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>blood pressure</u></b> |"}),
    ("Нет, у меня нет возможности",
    [
        "No, I don't have an opportunity",
        "No, I do not have an opportunity",
        "No, I have no opportunity"
    ]),
    ("Вы можете это сделать у нас в аптеке",
    [
        "You can do it here at our pharmacy",
        "You can do it here in our pharmacy",
        "You may do it here at our pharmacy",
        "You may do it here in our pharmacy",
        "You can do it here at our drugstore",
        "You can do it here in our drugstore",
        "You may do it here at our drugstore",
        "You may do it here in our drugstore",
        "You can do it here at our apothecary",
        "You can do it here in our apothecary",
        "You may do it here at our apothecary",
        "You may do it here in our apothecary",
        "You can do it here at our chemist's shop",
        "You can do it here in our chemist's shop",
        "You may do it here at our chemist's shop",
        "You may do it here in our chemist's shop",
    ]),
    ("Пожалуйста, присядьте здесь и протяните мне правую руку",
    [
        "Please, sit down here and give me your right arm",
        "Please, sit here and give me your right arm",
        "Please, sit over here and give me your right arm",
        "Please, sit down here and give me the right arm",
        "Please, sit here and give me the right arm",
        "Please, sit over here and give me the right arm",
    ],
    {"for_info": hlink("Разница между hand и arm", "http://surl.li/eeamc")}),
    ("Ваше давление в норме. Без рецепта я могу вам предложить «ибупрофен»",
    [
        "Your blood pressure is normal. Without a prescription I can offer you «ibuprofen»",
        "Your blood pressure's normal. Without a prescription I can offer you «ibuprofen»",
        "Your blood pressure is in the norm. Without a prescription I can offer you «ibuprofen»",
        "Your blood pressure's in the norm. Without a prescription I can offer you «ibuprofen»"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>a prescription, «ibuprofen»</u></b> |"}),
    ("Я раньше никогда не принимала его",
    [
        "I have never taken it",
        "I've never taken it"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>have, to take</u></b> |"}),
    ("Это хорошее лекарство и оно поможет вам в течение 15 минут",
    [
        "It is good medication and it will help you within 15 minutes",
        "It is good medication and it is going to help you within 15 minutes",
        "It's good medication and it will help you within 15 minutes",
        "It's good medication and it is going to help you within 15 minutes",
        "It's good medication and it's going to help you within 15 minutes",
        "It's good medication and it's gonna help you within 15 minutes",
        "It is good medication and it's gonna help you within 15 minutes",
        "It's good medication and it'll help you within 15 minutes",
        "It is good medication and it'll help you within 15 minutes",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>medication, within</u></b> |"}),
    ("Можно мне еще бутылку воды?",
    [
        "Can I also have a bottle of water?",
        "Can I have a bottle of water as well?",
        "May I also have a bottle of water?",
        "May I have a bottle of water as well?",
    ]),
    ("Конечно! С вас 2 доллара 80 центов",
    [
        "Of course! That will be 2 dollars 80 cents",
        "Of course! That'll be 2 dollars 80 cents",
        "Of course! It will be 2 dollars 80 cents",
        "Of course! It'll be 2 dollars 80 cents",
        "Cartainly! That will be 2 dollars 80 cents",
        "Cartainly! That'll be 2 dollars 80 cents",
        "Cartainly! It will be 2 dollars 80 cents",
        "Cartainly! It'll be 2 dollars 80 cents",
        "Surely! That will be 2 dollars 80 cents",
        "Surely! That'll be 2 dollars 80 cents",
        "Surely! It will be 2 dollars 80 cents",
        "Surely! It'll be 2 dollars 80 cents",
        "Sure! That will be 2 dollars 80 cents",
        "Sure! That'll be 2 dollars 80 cents",
        "Sure! It will be 2 dollars 80 cents",
        "Sure! It'll be 2 dollars 80 cents",
        "Assuredly! That will be 2 dollars 80 cents",
        "Assuredly! That'll be 2 dollars 80 cents",
        "Assuredly! It will be 2 dollars 80 cents",
        "Assuredly! It'll be 2 dollars 80 cents",
        "Absolutely! That will be 2 dollars 80 cents",
        "Absolutely! That'll be 2 dollars 80 cents",
        "Absolutely! It will be 2 dollars 80 cents",
        "Absolutely! It'll be 2 dollars 80 cents",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>will</u></b> |"})
]





topic_medium3 = [
    """
    Ваш маршрут построен. Через 300 метров поверните направо. Двигайтесь прямо пятьсот метров.
    Держитесь левой полосы. На кольце съезжайте на третьем съезде. Езжайте прямо до первого перекрёстка. 
    На перекрёстке развернитесь. Под мостом есть камера наблюдения за скоростным режимом. 
    Вы въезжаете в населённый пункт. Вы приехали, счастливо оставаться
    """,
    ("Ваш маршрут построен",
    [
        "Your route is set",
        "Your route's set",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>route</u></b> |"}),
    ("Через триста метров поверните направо",
    [
        "In three hundred meters turn right",
        "Turn right in three hundred meters",
        "After three hundred meters turn right",
        "Turn right after three hundred meters"
    ]),
    ("Двигайтесь прямо пятьсот метров",
    [
        "Move straight ahead for five hundred meters",
        "Move ahead for five hundred meters",
        "Move straight for five hundred meters",
        "Move forward for five hundred meters",
        "Move directly ahead for five hundred meters",
        "Move directly for five hundred meters",
    ]),
    ("Держитесь левой полосы",
    [
        "Keep to the left lane",
        "Hold to the left lane",
        "Stick to the left lane",
        "Follow on the left lane",
        "Follow on to the left lane",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>the, lane</u></b> |"}),
    ("На кольце съезжайте на третьем съезде",
    [
        "On the roundabout move out on the third exit",
        "On the roundabout move out on the third exit",
        "At the roundabout move out on the third exit",
        "At the roundabout move out on the third exit",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>the, a roundabout, an exit</u></b> |"}),
    ("Езжайте прямо до первого перекрёстка",
    [
        "Drive straight ahead until first crossroads",
        "Drive ahead until first crossroads",
        "Drive straight until first crossroads",
        "Drive forward until first crossroads",
        "Drive directly ahead until first crossroads",
        "Drive directly until first crossroads",
        "Go straight ahead until first crossroads",
        "Go ahead until first crossroads",
        "Go straight until first crossroads",
        "Go forward until first crossroads",
        "Go directly ahead until first crossroads",
        "Go directly until first crossroads"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>crossroads</u></b> |"}),
    ("На перекрёстке развернитесь",
    [
        "Turn around on the crossroads",
        "On the crossroads turn around",
        "Turn around at the crossroads",
        "At the crossroads turn around"
    ]),
    ("Под мостом есть камера наблюдения за скоростным режимом",
    [
        "There is a speed camera under the bridge",
        "There's a speed camera under the bridge",
        "Under the bridge there is a speed camera",
        "Under the bridge there's a speed camera"
    ]),
    ("Вы въезжаете в населённый пункт",
    [
        "You are entering a locality",
        "You're entering a locality",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>a locality</u></b> |"}),
    ("Вы приехали, счастливо оставаться",
    [
        "You have arrived, have a nice stay",
        "You have come, have a nice stay",
        "You've come, have a nice stay",
        "You have come, have a good stay",
        "You've come, have a good stay",
        "You have come, have a fine stay",
        "You've come, have a fine stay",
        "You've arrived, have a nice stay",
        "You have arrived, have a good stay",
        "You've arrived, have a good stay",
        "You have arrived, have a fine stay",
        "You've arrived, have a fine stay",
    ])
]