from aiogram.utils.markdown import hlink


at_the_market = [
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
    {"hint": "wahtever"}),
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
    {"hint": "purchase"}),
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





headache = [
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
    {"hint": "to offer"}),
    ("Здравствуйте! Вы мерили ваше давление?",
    [
        "Hello! Did you measure your blood pressure?",
        "Good afternoon! Did you measure your blood pressure?",
        "Hello! Have you measured your blood pressure?",
        "Good afternoon! Have you measured your blood pressure?",
    ],
    {"hint": "blood pressure"}),
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
    {"hint": "a prescription, ibuprofen"}),
    ("Я раньше никогда не принимала его",
    [
        "I have never taken it",
        "I've never taken it"
    ],
    {"hint": "have, to take"}),
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
    {"hint": "medication, within"}),
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
    {"hint": "will"})
]





car_navigator = [
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
    {"hint": "route"}),
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
    {"hint": "the, lane"}),
    ("На кольце съезжайте на третьем съезде",
    [
        "At the roundabout move out at the third exit",
        "On the roundabout move out on the third exit",
        "On the roundabout move out at the third exit",
        "At the roundabout move out on the third exit",
    ],
    {"hint": "the, a roundabout, an exit"}),
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
    {"hint": "a crossroads"}),
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
    {"hint": "a locality"}),
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





in_New_York = [
    """
    - Посмотри на город, какой он красивый!
    - Мне не нравится. Здесь слишком много людей.
    - Это Тайм-Сквер, самая знаменитая улица. Естественно, здесь будет много людей.
    - Я помню эту улицу из американских фильмов. Такое чувство, что я здесь уже был.
    - Нам нужно посетить музей естествознания.
    - Это далеко от нашей квартиры?
    - Довольно далеко. Жилье в центре Нью-Йорка дорогое, поэтому пришлось забронировать квартиру подальше.
    - Нам нужно ехать на метро? Там так много людей!
    - Хватит жаловаться! Мы приехали смотреть большой город!
    - Ладно...
    """,
    ("Посмотри на город, какой он красивый!",
    [
        "Look at the city, it's so beautiful!",
        "Look at the city, it is so beautiful!",
        "Look at the city, that's so beautiful!",
        "Look at the city, that is so beautiful!",
        "Look at the city, it's so lovely!",
        "Look at the city, it is so lovely!",
        "Look at the city, that's so lovely!",
        "Look at the city, that is so lovely!"
    ]),
    ("Мне не нравится. Здесь слишком много людей",
    [
        "I do not like it. There are too many people",
        "I d'not like it. There are too many people",
        "I do not like this. There are too many people",
        "I d'not like this. There are too many people"
    ]),
    ("Это Таймс-Сквер, самая знаменитая улица. Естественно, здесь много людей",
    [
        "This is Times Square, the most famous street. Naturally, there are many people here",
        "This is Times Square, the most famous street. Naturally, there are lots of people here",
        "This is Times Square, the most famous street. Naturally, there are a lot of people here",
        "It is Times Square, the most famous street. Naturally, there are many people here",
        "It is Times Square, the most famous street. Naturally, there are lots of people here",
        "It is Times Square, the most famous street. Naturally, there are a lot of people here",
        "It's Times Square, the most famous street. Naturally, there are many people here",
        "It's Times Square, the most famous street. Naturally, there are lots of people here",
        "It's Times Square, the most famous street. Naturally, there are a lot of people here"
    ],
    {"hint": "Times Square, aturally"}),
    ("Я помню эту улицу из американских фильмов. Такое чувство, что я здесь уже был",
    [
        "I remember this street from American films. It feels like that I have been here",
        "I remember this street from American movies. It feels like that I have been here",
        "I remember this street from American films. It feels like that I have been here before",
        "I remember this street from American movies. It feels like that I have been here before",
        "I remember this street from American films. It feels like that I've been here",
        "I remember this street from American movies. It feels like that I've been here",
        "I remember this street from American films. It feels like that I've been here before",
        "I remember this street from American movies. It feels like that I've been here before",
        "I remember this street from American films. Feels like that I have been here",
        "I remember this street from American movies. Feels like that I have been here",
        "I remember this street from American films. Feels like that I have been here before",
        "I remember this street from American movies. Feels like that I have been here before",
        "I remember this street from American films. Feels like that I've been here",
        "I remember this street from American movies. Feels like that I've been here",
        "I remember this street from American films. Feels like that I've been here before",
        "I remember this street from American movies. Feels like that I've been here before",
        "I remember this street from American films. It feels like I have been here",
        "I remember this street from American movies. It feels like I have been here",
        "I remember this street from American films. It feels like I have been here before",
        "I remember this street from American movies. It feels like I have been here before",
        "I remember this street from American films. It feels like I've been here",
        "I remember this street from American movies. It feels like I've been here",
        "I remember this street from American films. It feels like I've been here before",
        "I remember this street from American movies. It feels like I've been here before",
        "I remember this street from American films. Feels like I have been here",
        "I remember this street from American movies. Feels like I have been here",
        "I remember this street from American films. Feels like I have been here before",
        "I remember this street from American movies. Feels like I have been here before",
        "I remember this street from American films. Feels like I've been here",
        "I remember this street from American movies. Feels like I've been here",
        "I remember this street from American films. Feels like I've been here before",
        "I remember this street from American movies. Feels like I've been here before",
    ]),
    ("Нам нужно посетить музей естествознания",
    [
        "We need to visit American Museum of Natural History",
        "We have to visit American Museum of Natural History",
        "We must visit American Museum of Natural History",
        "We have got to visit American Museum of Natural History",
        "We've got to visit American Museum of Natural History",
        "We need to attend American Museum of Natural History",
        "We have to attend American Museum of Natural History",
        "We must attend American Museum of Natural History",
        "We have got to attend American Museum of Natural History",
        "We've got to attend American Museum of Natural History",
    ],
    {"hint": "American Museum of Natural History"}),
    ("Это далеко от нашей квартиры?",
    [
        "Is it far from our flat?",
        "Is that far from our flat?",
        "Is it a long way from our flat?",
        "Is that a long way from our flat?",
    ],
    {"hint": "a flat"}),
    ("Довольно далеко. Жилье в центре Нью-Йорка дорогое, поэтому пришлось забронировать квартиру загородом",
    [
        "Quite far away. Housing in the center of New York is expensive so we had to rent a flat in the countryside",
        "Quite far away. Housing in the centre of New York is expensive so we had to rent a flat in the countryside",
        "Quite far. Housing in the center of New York is expensive so we had to rent a flat in the countryside",
        "Quite far. Housing in the centre of New York is expensive so we had to rent a flat in the countryside",
        "Pretty far away. Housing in the center of New York is expensive so we had to rent a flat in the countryside",
        "Pretty far away. Housing in the centre of New York is expensive so we had to rent a flat in the countryside",
        "Pretty far. Housing in the center of New York is expensive so we had to rent a flat in the countryside",
        "Pretty far. Housing in the centre of New York is expensive so we had to rent a flat in the countryside",
        "Quite far away. Housing in the center of New York is expensive, that is why we had to rent a flat in the countryside",
        "Quite far away. Housing in the centre of New York is expensive, that is why we had to rent a flat in the countryside",
        "Quite far. Housing in the center of New York is expensive, that is why we had to rent a flat in the countryside",
        "Quite far. Housing in the centre of New York is expensive, that is why we had to rent a flat in the countryside",
        "Pretty far away. Housing in the center of New York is expensive, that is why we had to rent a flat in the countryside",
        "Pretty far away. Housing in the centre of New York is expensive, that is why we had to rent a flat in the countryside",
        "Pretty far. Housing in the center of New York is expensive, that is why we had to rent a flat in the countryside",
        "Pretty far. Housing in the centre of New York is expensive, that is why we had to rent a flat in the countryside",
        "Quite far away. Housing in the center of New York is expensive, that's why we had to rent a flat in the countryside",
        "Quite far away. Housing in the centre of New York is expensive, that's why we had to rent a flat in the countryside",
        "Quite far. Housing in the center of New York is expensive, that's why we had to rent a flat in the countryside",
        "Quite far. Housing in the centre of New York is expensive, that's why we had to rent a flat in the countryside",
        "Pretty far away. Housing in the center of New York is expensive, that's why we had to rent a flat in the countryside",
        "Pretty far away. Housing in the centre of New York is expensive, that's why we had to rent a flat in the countryside",
        "Pretty far. Housing in the center of New York is expensive, that's why we had to rent a flat in the countryside",
        "Pretty far. Housing in the centre of New York is expensive, that's why we had to rent a flat in the countryside",
    ],
    {"hint": "housing, have to, in the countryside"}),
    ("Нам нужно ехать на метро? Там так много людей!",
    [
        "Do we need to go by subway? It is so crowded!",
        "Do we need to go by subway? It's so crowded!",
        "Do we have to go by subway? It is so crowded!",
        "Do we have to go by subway? It's so crowded!",
        "Must we go by subway? It is so crowded!",
        "Must we go by subway? It's so crowded!",
        "Should we go by subway? It is so crowded!",
        "Should we go by subway? It's so crowded!",
        "Do we need to go on subway? It is so crowded!",
        "Do we need to go on subway? It's so crowded!",
        "Do we have to go on subway? It is so crowded!",
        "Do we have to go on subway? It's so crowded!",
        "Must we go on subway? It is so crowded!",
        "Must we go on subway? It's so crowded!",
        "Should we go on subway? It is so crowded!",
        "Should we go on subway? It's so crowded!",
        "Do we need to go by the subway? It is so crowded!",
        "Do we need to go by the subway? It's so crowded!",
        "Do we have to go by the subway? It is so crowded!",
        "Do we have to go by the subway? It's so crowded!",
        "Must we go by the subway? It is so crowded!",
        "Must we go by the subway? It's so crowded!",
        "Should we go by the subway? It is so crowded!",
        "Should we go by the subway? It's so crowded!",
        "Do we need to go on the subway? It is so crowded!",
        "Do we need to go on the subway? It's so crowded!",
        "Do we have to go on the subway? It is so crowded!",
        "Do we have to go on the subway? It's so crowded!",
        "Must we go on the subway? It is so crowded!",
        "Must we go on the subway? It's so crowded!",
        "Should we go on the subway? It is so crowded!",
        "Should we go on the subway? It's so crowded!",
    ],
    {"hint": "subway, be crowded"}),
    ("Хватит жаловаться! Мы приехали смотреть большой город!",
    [
        "Stop complaining. We have come to see a big city!",
        "Stop complaining. We've come to see a big city!",
        "Stop complaining. We have come to see a large city!",
        "Stop complaining. We've come to see a large city!",
        "Stop complaining. We have come to see a great city!",
        "Stop complaining. We've come to see a great city!",
        "Cease complaining. We have come to see a big city!",
        "Cease complaining. We've come to see a big city!",
        "Cease complaining. We have come to see a large city!",
        "Cease complaining. We've come to see a large city!",
        "Cease complaining. We have come to see a great city!",
        "Cease complaining. We've come to see a great city!",
        "Finish complaining. We have come to see a big city!",
        "Finish complaining. We've come to see a big city!",
        "Finish complaining. We have come to see a large city!",
        "Finish complaining. We've come to see a large city!",
        "Finish complaining. We have come to see a great city!",
        "Finish complaining. We've come to see a great city!",
    ],
    {"for_info": hlink("Употребление глаголов после «stop»", "http://surl.li/effwq")}),
    ("Ладно",
    [
        "Alright",
        "All right",
        "OK",
        "Okay"
    ])
]





at_the_restaurant = [
    """
    - Здравствуйте! Меня зовут Мария, я ваша официантка.
    - Я могу вам помочь с заказом?
    - Приветствую, Мария! Какие напитки у вас есть?
    - У нас есть газировка, соки, а также фирменный клубничный лимонад.
    - Это любопытно! Можно нам графин вашего лимонада?
    - А какие салаты вы подаёте?
    - У нас есть отличный салат от шефа. В него входят орехи и сезонные овощи. 
    - Отлично! Тогда я буду еще этот салат.
    - А я бы хотела грибной суп и тарелку риса с курицей для моего племянника.
    - Спасибо за заказ! Лимонад я принесу сразу, а ваши блюда по готовности.
    """,
    ("Здравствуйте! Меня зовут Мария, я ваша официантка",
    [
        "Hello! My name is Maria, I am your waitress",
        "Hello! My name is Maria, I'm your waitress",
        "Hello! My name's Maria, I am your waitress",
        "Hello! My name's Maria, I'm your waitress",
    ]),
    ("Я могу вам помочь с заказом?",
    [
        "Can I help you with the order?",
        "Can I help you with your order?",
        "May I help you with the order?",
        "May I help you with your order?",
    ]),
    ("Приветствую, Мария! Какие напитки у вас есть?",
    [
        "Greetings, Maria! What beverages do you have?",
        "Greetings, Maria! What drinks do you have?",
        "Greetings, Maria! What beverages have you got?",
        "Greetings, Maria! What drinks have you got?",
    ],
    {"hint": "greetings"}),
    ("У нас есть газировка, соки, а также фирменный клубничный лимонад",
    [
        "We have soda, juices and also branded strawberry lemonade",
        "We have got soda, juices and also branded strawberry lemonade",
        "We've got soda, juices and also branded strawberry lemonade",
        "We have soda, juices as well as branded strawberry lemonade",
        "We have got soda, juices as well as branded strawberry lemonade",
        "We've got soda, juices as well as branded strawberry lemonade",
        "We have soda, juices and branded strawberry lemonade as well",
        "We have got soda, juices and branded strawberry lemonade as well",
        "We've got soda, juices and branded strawberry lemonade as well"
    ],
    {"hint": "soda, branded"}),
    ("Это любопытно! Можно нам графин вашего лимонада?",
    [
        "That is curious! Can we have a decanter of your lemonade?",
        "That's curious! Can we have a decanter of your lemonade?",
    ],
    {"hint": "curious, a decanter"}),
    ("А какие салаты вы подаёте?",
    [
        "And what salads do you serve?"
    ],
    {"hint": "to serve"}),
    ("У нас есть отличный салат от шефа. В него входят орехи и сезонные овощи",
    [
        "We have an excellent salad from the chef. It includes nuts and seasonal vegetables",
        "We have an excellent salad from the chef. It includes nuts and season vegetables",
        "We have got an excellent salad from the chef. It includes nuts and seasonal vegetables",
        "We have got an excellent salad from the chef. It includes nuts and season vegetables",
        "We have an excellent salad from the chef. It involves nuts and seasonal vegetables",
        "We have an excellent salad from the chef. It involves nuts and season vegetables",
        "We have got an excellent salad from the chef. It involves nuts and seasonal vegetables",
        "We have got an excellent salad from the chef. It involves nuts and season vegetables"
    ]),
    ("Отлично! Тогда я буду еще этот салат",
    [
        "Great! Then I will also have that salad",
        "Great! Then I'll also have that salad",
        "Awesome! Then I will also have that salad",
        "Awesome! Then I'll also have that salad",
        "Splendid! Then I will also have that salad",
        "Splendid! Then I'll also have that salad",
        "Great! Then I will have that salad as well",
        "Great! Then I'll have that salad as well",
        "Awesome! Then I will have that salad as well",
        "Awesome! Then I'll have that salad as well",
        "Splendid! Then I will have that salad as well",
        "Splendid! Then I'll have that salad as well",
    ]),
    ("А я бы хотела грибной суп и тарелку риса с курицей для моего племянника",
    [
        "And I would like a mushroom soup and a plate of rice with chicken for my nephew",
        "And Iэd like a mushroom soup and a plate of rice with chicken for my nephew",
        "And I would like a mushroom soup and a dish of rice with chicken for my nephew",
        "And Iэd like a mushroom soup and a dish of rice with chicken for my nephew",
    ]),
    ("Спасибо за заказ! Лимонад я принесу сразу, а ваши блюда по готовности",
    [
        "Thanks for the order! The lemonade I will bring at once and the dishes on readiness",
        "Thank you for the order! The lemonade I will bring at once and the dishes on readiness",
        "Thanks for the order! The lemonade I will bring right away and the dishes on readiness",
        "Thank you for the order! The lemonade I will bring right away and the dishes on readiness",
        "Thanks for the order! The lemonade I will bring straight away and the dishes on readiness",
        "Thank you for the order! The lemonade I will bring straight away and the dishes on readiness",
        "Thanks for the order! I will bring the lemonade at once and the dishes on readiness",
        "Thank you for the order! I will bring the lemonade at once and the dishes on readiness",
        "Thanks for the order! I will bring the lemonade right away and the dishes on readiness",
        "Thank you for the order! I will bring the lemonade right away and the dishes on readiness",
        "Thanks for the order! I will bring the lemonade straight away and the dishes on readiness",
        "Thank you for the order! I will bring the lemonade straight away and the dishes on readiness",
    ],
    {"hint": "the, on readiness"}),
]






Hawaii = [
    """
    Гавайские острова очень красивые. Это пятидесятый по счету штат в США. 
    Мауна-Кеа — самая высокий среди вулканов на Гавайский островах.
    Еще на Гавайях зародился серфинг. На Гавайях нет змей.
    Ежегодно Гавайи посещают более 6 миллионов туристов.
    В среднем туристы тратят на Гавайях около 11 миллиардов долларов каждый год.
    Самый древний остров Гавайского архипелага — Кауаи, ему более 6 миллионов лет.
    Средняя температура на островах 25 градусов. Приезжайте на отдых на Гавайи.
    """,
    ("Гавайские острова очень красивые",
    [
        "The Hawaiian Islands are very beautiful",
        "The Hawaiian Islands are really beautiful",
        "The Hawaiian Islands are very nice",
        "The Hawaiian Islands are really nice",
    ],
    {"hint": "The Hawaiian Islands"}),
    ("Это пятидесятый по счету штат в США",
    [
        "It is the fiftieth state in the US",
        "It's the fiftieth state in the US"
    ]),
    ("Мауна-Кеа — самая высокий среди вулканов на Гавайский островах",
    [
        "Mauna Kea is the highest among volcanoes on the Hawaiian Islands",
        "Mauna Kea's the highest among volcanoes on the Hawaiian Islands",
        "Mauna Kea is the highest amongst volcanoes on the Hawaiian Islands",
        "Mauna Kea's the highest amongst volcanoes on the Hawaiian Islands",
        "Mauna Kea is the highest volcano on the Hawaiian Islands",
        "Mauna Kea's the highest volcano on the Hawaiian Islands"
    ],
    {"hint": "Mauna Kea, on"},
    {"for_info": hlink("Разница между tall и high", "http://surl.li/efzyo")}),
    ("Еще на Гавайях зародился серфинг",
    [
        "Also surfing originated in Hawaii",
        "Surfing also originated in Hawaii"
    ],
    {"hint": "originate in"}),
    ("На Гавайях нет змей",
    [
        "There are no snakes in Hawaii",
        "There are not any snakes in Hawaii",
        "There aren't any snakes in Hawaii",
        "Hawaii does not have snakes",
        "Hawaii doesn't have snakes",
        "Hawaii has not got snakes",
        "Hawaii hasn't got snakes",
    ],
    {"hint": "in"}),
    ("Ежегодно Гавайи посещают более 6 миллионов туристов",
    [
        "More than 6 million tourists visit Hawaii annually",
        "More than 6 million tourists annually visit Hawaii",
    ],
    {"hint": "annually"}),
    ("В среднем туристы тратят на Гавайях около 11 миллиардов долларов каждый год",
    [
        "On average, tourists spend about 11 billion dollars in Hawaii each year",
        "Tourists spend about 11 billion dollars on average in Hawaii each year",
        "On average, tourists spend about 11 billion dollars in Hawaii every year",
        "Tourists spend about 11 billion dollars on average in Hawaii every year",
    ],
    {"hint": "on average, each"},
    {"for_info": hlink("Разница между each и every", "http://surl.li/egafa")}),
    ("Самый древний остров Гавайского архипелага — Кауаи, ему более 6 миллионов лет",
    [
        "Kauai, the oldest island in the Hawaiian archipelago, is over 6 million years old",
        "Kauai, the most ancient island in the Hawaiian archipelago, is over 6 million years old",
        "The oldest island in the Hawaiian archipelago is Kauai , it is over 6 million years old",
        "The most ancient island in the Hawaiian archipelago is Kauai , it's over 6 million years old"
    ],
    {"hint": "the Hawaiian archipelago, over, old"}),
    ("Средняя температура на островах 25 градусов",
    [
        "The average temperature on the islands is 25 degrees"
    ],
    {"hint": "the"}),
    ("Приезжайте на отдых на Гавайи",
    [
        "Come to rest to Hawaii",
        "Come to the rest to Hawaii",
        "Come for the rest to Hawaii",
        "Come for rest to Hawaii"
        "Come on vacation to Hawaii",
        "Visit Hawaii on your vacation",
        "Come to visit Hawaii on your vacation",
        "Come on holidays to Hawaii",
        "Visit Hawaii on your holidays",
        "Come to visit Hawaii on your holidays",
        "Come on holiday to Hawaii",
        "Visit Hawaii on your holiday",
        "Come to visit Hawaii on your holiday",
    ])
]