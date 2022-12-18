# First element of the list is a whole text
topic_easy1 = [
    """
    Алина приехала в новый город. На улице было очень холодно.
    На улице идёт дождь, тебе следует взять зонт.
    У нас закончился хлеб, нам нужно найти магазин.
    Сегодня мы собираемся выйти погулять, потому что на улице тепло.
    В автобусах есть специальные сиденья для беременных женщин.
    В автобусах есть специальные сиденья для беременных женщин.
    Этот футбольный матч довольно скучный. Моей жене нужны новые брюки.
    Мне кажется, завтра будет плохая погода.
    """,
    ("Алина приехала в новый город",
    [
        "Alina came to a new city",
        "Alina have come to a new city",
        "Alina've come to a new city"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>come</u></b> |"}),
    ("На улице было очень холодно",
    [
        "It was very cold outside",
        "It was really cold outside"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>outside</u></b> |"}),
    ("На улице идёт дождь, тебе следует взять зонт",
    [
        "It's raining outside, you should take an umbrella",
        "It is raining outside, you should take an umbrella"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>should</u></b> |"}),
    ("У нас закончился хлеб, нам нужно найти магазин",
    [
        "We ran out of bread, we need to find a shop",
        "We've run out of bread, we need to find a shop",
        "We have run out of bread, we need to find a shop",
        "We ran out of bread, we need to find a store"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>run out of, need to</u></b> |"}),
    ("Сегодня мы собираемся выйти погулять, потому что на улице тепло",
    [
        "Today we are going to go out because it's warm outside",
        "Today we are planning to go out because it's warm outside",
        "Today we're going to go out because it's warm outside",
        "Today we're planning to go out because it's warm outside"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>go out</u></b> |"}),
    ("В автобусах есть специальные сиденья для беременных женщин",
    [
        "There are special seats for pregnant women in buses"
        "Buses have special seats for pregnant women",
        "There are special seats in buses for pregnant women",
    ]),
    ("Этот футбольный матч довольно скучный",
    [
        "This football match is pretty boring",
        "This football match is quite boring",
        "This football match is rather boring",
        "This football match is fairly boring",
        "This soccer match is pretty boring",
        "This soccer match is quite boring",
        "This soccer match is rather boring",
        "This soccer match is fairly boring",
        "This football game is pretty boring",
        "This football game is quite boring",
        "This football game is rather boring",
        "This football game is fairly boring",
        "This soccer game is pretty boring",
        "This soccer game is quite boring",
        "This soccer game is rather boring",
        "This soccer game is fairly boring"
    ]),
    ("Моей жене нужны новые брюки",
    [
        "My wife needs new pants",
        "My wife needs new trousers",
        "My wife requires new pants",
        "My wife requires new trousers"
    ]),
    ("Мне кажется, завтра будет плохая погода",
    [
        "It seems to me that tomorrow will be bad weather",
        "It seems to me tomorrow will be bad weather",
        "It seems tomorrow will be bad weather",
        "It seems that tomorrow will be bad weather"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>to seem</u></b> |"}),
    ("Дядя Федя очень высокий",
    [
        "Uncle Fediya is very tall",
        "Uncle Fediya is really tall",
        "Uncle Fediya's very tall",
        "Uncle Fediya's really tall"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>Fediya</u></b> |"}),
]


topic_easy2 = [
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
        "Good morning! Choose whichever you like, all my vegetables are fresh",
        "Good morning! Choose whichever you like, I have only fresh vegetables",
        "Good morning! Choose whichever you like, I've got only fresh vegetables",
        "Good morning! Choose whichever you like, I have got only fresh vegetables",
        "Good morning! Choose what you like, all my vegetables are fresh",
        "Good morning! Choose what you like, I have only fresh vegetables",
        "Good morning! Choose what you like, I've got only fresh vegetables",
        "Good morning! Choose what you like, I have got only fresh vegetables",
        "Good morning! Choose whatever you fancy, all my vegetables are fresh",
        "Good morning! Choose whatever you fancy, I have only fresh vegetables",
        "Good morning! Choose whatever you fancy, I've got only fresh vegetables",
        "Good morning! Choose whatever you fancy, I have got only fresh vegetables",
        "Good morning! Choose whichever you fancy, all my vegetables are fresh",
        "Good morning! Choose whichever you fancy, I have only fresh vegetables",
        "Good morning! Choose whichever you fancy, I've got only fresh vegetables",
        "Good morning! Choose whichever you fancy, I have got only fresh vegetables",
        "Good morning! Choose what you fancy, all my vegetables are fresh",
        "Good morning! Choose what you fancy, I have only fresh vegetables",
        "Good morning! Choose what you fancy, I've got only fresh vegetables",
        "Good morning! Choose what you fancy, I have got only fresh vegetables",
        "Good morning! Pick whatever you like, all my vegetables are fresh",
        "Good morning! Pick whatever you like, I have only fresh vegetables",
        "Good morning! Pick whatever you like, I've got only fresh vegetables",
        "Good morning! Pick whatever you like, I have got only fresh vegetables",
        "Good morning! Pick whichever you like, all my vegetables are fresh",
        "Good morning! Pick whichever you like, I have only fresh vegetables",
        "Good morning! Pick whichever you like, I've got only fresh vegetables",
        "Good morning! Pick whichever you like, I have got only fresh vegetables",
        "Good morning! Pick what you like, all my vegetables are fresh",
        "Good morning! Pick what you like, I have only fresh vegetables",
        "Good morning! Pick what you like, I've got only fresh vegetables",
        "Good morning! Pick what you like, I have got only fresh vegetables",
        "Good morning! Pick whatever you fancy, all my vegetables are fresh",
        "Good morning! Pick whatever you fancy, I have only fresh vegetables",
        "Good morning! Pick whatever you fancy, I've got only fresh vegetables",
        "Good morning! Pick whatever you fancy, I have got only fresh vegetables",
        "Good morning! Pick whichever you fancy, all my vegetables are fresh",
        "Good morning! Pick whichever you fancy, I have only fresh vegetables",
        "Good morning! Pick whichever you fancy, I've got only fresh vegetables",
        "Good morning! Pick whichever you fancy, I have got only fresh vegetables",
        "Good morning! Pick what you fancy, all my vegetables are fresh",
        "Good morning! Pick what you fancy, I have only fresh vegetables",
        "Good morning! Pick what you fancy, I've got only fresh vegetables",
        "Good morning! Pick what you fancy, I have got only fresh vegetables",
    ]),
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
        "alright, you convinced me, put also one carrot",
        "alright, you convinced me, put also a carrot",
        "Ok, you've convinced me, put also one carrot",
        "Ok, you've convinced me, put also a carrot",
        "alright, you've convinced me, put also one carrot",
        "alright, you've convinced me, put also a carrot",
        "Ok, you have convinced me, put also one carrot",
        "Ok, you have convinced me, put also a carrot",
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
    ("Где я могу купить яблоки?",
    [
        "Where can I buy apples?",
        "Where can I purchase apples?",
        "Where could I buy apples?",
        "Where could I purchase apples?"
    ]),
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
