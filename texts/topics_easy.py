from aiogram.utils.markdown import hlink


# First element of the list is a whole text
topic_easy1 = [
    """
    - Здравствуйте! Мне нужен номер на 1 ночь.
    - Добрый день! Вы бронировали заранее? - К сожалению, нет. У вас есть свободные номера?
    - Одну минуточку, пожалуйста. У нас есть номер superior. Цена за сутки 60$.
    - А что на счёт завтрака? - Вы можете оплатить его отдельно за 9$.
    - Хорошо, меня устраивает. Я забронирую этот номер и завтрак.
    - Как будете оплачивать, наличными или картой? - Дебетовой картой, пожалуйста.
    - Вот платежный терминал.
    """,
    ("Здравствуйте! Мне нужен номер на 1 ночь",
    [
        "Hello! I need a room for a night",
        "Hello! I require a room for a night",
        "Hello! I need a room for one night",
        "Hello! I require a room for one night",
    ]),
    ("Добрый день! Вы бронировали заранее?",
    [
        "Good day! Did you book in advance?",
        "Good afternoon! Did you book in advance?",
        "Good day! Have you booked in advance?",
        "Good afternoon! Have you booked in advance?",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>in advance</u></b> |"}),
    ("К сожалению, нет. У вас есть свободные номера?",
    [
        "Unfortunately, no. Do you have free rooms?",
        "Unfortunately, no. Have you got free rooms?",
        "No, unfortunately. Do you have free rooms?",
        "No, unfortunately. Have you got free rooms?",
    ]),
    ("Одну минуточку, пожалуйста. У нас есть номер superior. Цена за ночь 60$",
    [
        "One minute, please. We have a superior room. The price is 60$ per night",
        "One minute, please. We have got a superior room. The price is 60$ per night",
        "One minute, please. We have got a superior room. The price is 60$ for one night",
        "One minute, please. We have got a superior room. The price is 60$ for one night",
        "One minute, please. We have got a superior room. The price's 60$ per night",
        "One minute, please. We have got a superior room. The price's 60$ for a night",
        "One minute, please. We have got a superior room. The price's 60$ for one night",
        "One minute, please. We've got a superior room. The price is 60$ per night",
        "One minute, please. We've got a superior room. The price is 60$ per night",
        "One minute, please. We've got a superior room. The price is 60$ for one night",
        "One minute, please. We've got a superior room. The price is 60$ for one night",
        "One minute, please. We've got a superior room. The price's 60$ per night",
        "One minute, please. We've got a superior room. The price's 60$ for a night",
        "One minute, please. We've got a superior room. The price's 60$ for one night",
        "A minute, please. We have a superior room. The price is 60$ per night",
        "A minute, please. We have got a superior room. The price is 60$ per night",
        "A minute, please. We have got a superior room. The price is 60$ for one night",
        "A minute, please. We have got a superior room. The price is 60$ for one night",
        "A minute, please. We have got a superior room. The price's 60$ per night",
        "A minute, please. We have got a superior room. The price's 60$ for a night",
        "A minute, please. We have got a superior room. The price's 60$ for one night",
        "A minute, please. We've got a superior room. The price is 60$ per night",
        "A minute, please. We've got a superior room. The price is 60$ per night",
        "A minute, please. We've got a superior room. The price is 60$ for one night",
        "A minute, please. We've got a superior room. The price is 60$ for one night",
        "A minute, please. We've got a superior room. The price's 60$ per night",
        "A minute, please. We've got a superior room. The price's 60$ for a night",
        "A minute, please. We've got a superior room. The price's 60$ for one night",
        "A minute, please. We have a superior room. The price is 60$ per night",
    ]),
    ("А что на счёт завтрака?",
    [
        "And what about breakfast?"
    ]),
    ("Вы можете оплатить его отдельно за 9$",
    [
        "You can pay for it separately for 9$",
        "You may pay for it separately for 9$",
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>separately</u></b> |"}),
    ("Хорошо, меня устраивает. Я забронирую этот номер и завтрак",
    [
        "Good, it suits me. I will book this room and a breakfast",
        "Good, that suits me. I will book this room and a breakfast",
        "Good, I like it. I will book this room and a breakfast",
        "Fine, it suits me. I will book this room and a breakfast",
        "Fine, that suits me. I will book this room and a breakfast",
        "Fine, I like it. I will book this room and a breakfast",
        "Good, it suits me. I'll book this room and a breakfast",
        "Good, that suits me. I'll book this room and a breakfast",
        "Good, I like it. I'll book this room and a breakfast",
        "Fine, it suits me. I'll book this room and a breakfast",
        "Fine, that suits me. I'll book this room and a breakfast",
        "Fine, I like it. I'll book this room and a breakfast"
    ]),
    ("Как будете оплачивать, наличными или картой?",
    [
        "How will you pay, by cash or by card",
        "How will you pay, with cash or by card",
        "How will you pay, with cash or with card",
        "How will you pay, by cash or with card",
        "How are you goint to you pay, by cash or by card",
        "How are you goint to pay, with cash or by card",
        "How are you goint to pay, with cash or with card",
        "How are you gonna pay, by cash or by card",
        "How are you gonna pay, with cash or by card",
        "How are you gonna pay, with cash or with card",
        "How are you gonna pay, by cash or with card",
    ]),
    ("Дебетовой картой, пожалуйста",
    [
        "By debit card, please",
        "Withy debit card, please",
        "Debit card, please"
    ]),
    ("Вот платежный терминал",
    [
        "Here is the payment terminal",
        "Here's the payment terminal"
    ])
]





topic_easy2 = [
    """
    Я очень устала, но так хочу есть! 
    Давай закажем пиццу прямо в отель.
    Хорошая идея! Я хочу, чтобы она была с грибами, а еще много сыра.
    Здравствуйте! Можно заказать пиццу в отель?
    Добрый день! Скажите, пожалуйста, ваш адрес, я проверю, доставляем ли мы туда. - Ул. Зеленая, д. 11.
    Да, мы сможем осуществить доставку за 30 минут. Какую пиццу вы бы хотели?
    Я бы хотела в ней побольше сыра и грибов.
    Я могу вам предложить пиццу «фермерская». В ней будут, курица, грибы, томаты и сыр пармезан.
    Отлично! Нам подходит!
    Ожидайте пиццу через полчаса. Приятного аппетита!
    """,
    ("Я очень устала, но так хочу есть!",
    [
        "I'm exhausted but I want to eat so much!",
        "I am exhausted but I want to eat so much!",
        "I'm exhausted but I want to eat very much!",
        "I'm exhausted but I want to eat so much!",
        "I'm exhausted but I wanna eat so much!",
        "I am exhausted but I wanna eat so much!",
        "I'm exhausted but I wanna eat very much!",
        "I'm exhausted but I wanna eat so much!",
        "I'm exhausted but I want to eat so much!",
        "I am exhausted but I want to eat so much!",
        "I'm exhausted but I want to eat very much!",
        "I'm exhausted but I want to eat so much!",
        "I'm exhausted but I wanna eat so much!",
        "I am exhausted but I wanna eat so much!",
        "I'm exhausted but I wanna eat very much!",
        "I'm exhausted but I wanna eat so much!"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>be exhausted</u></b> |"}),
    ("Давай закажем пиццу прямо в отель",
    [
        "Let's order a pizza right into the hotel",
        "Let's order a pizza right into the hotel",
        "Let's order a pizza right into the hotel",
        "Let's order a pizza right into the hotel",
        "Let's order a pizza right into the hotel",
        "Let's order a pizza right into the hotel",
        "Let's order a pizza right into the hotel",
        "Let's order a pizza right into the hotel",
        "Let us order a pizza right into the hotel",
        "Let us order a pizza right into the hotel",
        "Let us order a pizza right into the hotel",
        "Let us order a pizza right into the hotel",
        "Let us order a pizza right into the hotel",
        "Let us order a pizza right into the hotel",
        "Let us order a pizza right into the hotel",
        "Let us order a pizza right into the hotel"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>right into</u></b> |"}),
    ("Хорошая идея! Я хочу, чтобы она была с грибами, а еще много сыра",
    [
        "Nice/good idea. I want it to be with with mushrooms and also with a lot of (much) cheese",
        "Good idea! I wish it to be with mushrooms and also with a lot of cheese",
        "Nice idea! I wish it to be with mushrooms and also with a lot of cheese",
        "Good idea! I wish it to be with mushrooms and also with lots cheese",
        "Nice idea! I wish it to be with mushrooms and also with lots cheese",
        "Good idea! I wish it to be with mushrooms and also with much cheese",
        "Nice idea! I wish it to be with mushrooms and also with much cheese",
        "Good idea! I wish it to be with mushrooms and with a lot of cheese as well",
        "Nice idea! I wish it to be with mushrooms and with a lot of cheese as well",
        "Good idea! I wish it to be with mushrooms and with lots cheese as well",
        "Nice idea! I wish it to be with mushrooms and with lots cheese as well",
        "Good idea! I wish it to be with mushrooms and with much cheese as well",
        "Nice idea! I wish it to be with mushrooms and with much cheese as well"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>to wish</u></b> |"}),
    ("Здравствуйте! Можно заказать пиццу в отель?",
    [
        "Hello! Can I order a pizza to a hotel?",
        "Hello! Can I order a pizza into a hotel?"
    ]),
    ("Добрый день! Скажите, пожалуйста, ваш адрес, я проверю, доставляем ли мы туда. - Ул. Зеленая, д. 11",
    [
        "Good day! Tell me, please, your address, I'll check if we deliver there. - Green street, 11",
        "Good afternoon! Tell me, please, your address, I'll check if we deliver there. - Green street, 11",
        "Good day! Tell me, please, your address, I will check if we deliver there. - Green street, 11",
        "Good afternoon! Tell me, please, your address, I will check if we deliver there. - Green street, 11",
        "Good day! Tell me, please, your address, I'll check if we deliver there. - Green street, 11",
        "Good afternoon! Tell me, please, your address, I'll check if we deliver there. - Green street, 11",
        "Good day! Tell me, please, your address, I will check if we deliver there. - Green street, 11",
        "Good afternoon! Tell me, please, your address, I will check if we deliver there. - Green street, 11"
    ]),
    ("Да, мы сможем осуществить доставку за 30 минут. Какую пиццу вы бы хотели?",
    [
        "Yes, we (will be able to) can deliver in 30 minutes. What kind/type of pizza would you like?",
        "Yes, we can deliver in 30 minutes. What kind of pizza would you like?",
        "Yes, we will be able to deliver in 30 minutes. What kind of pizza would you like?",
        "Yes, we'll be able to deliver in 30 minutes. What kind of pizza would you like?",
        "Yes, we can deliver in 30 minutes. What type of pizza would you like?",
        "Yes, we will be able to deliver in 30 minutes. What type of pizza would you like?",
        "Yes, we'll be able to deliver in 30 minutes. What type of pizza would you like?"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>would</u></b> |"}),
    ("Я бы хотела в ней побольше сыра и грибов",
    [
        "I would like it to have more cheese and mushrooms",
        "I'd like it to have more cheese and mushrooms",
        "I would like more cheese and mushrooms in it",
        "I'd like more cheese and mushrooms in it"
    ]),
    ("Я могу вам предложить пиццу «фермерская». В ней будут, курица, грибы, томаты и сыр пармезан",
    [
        "I can offer you farmer's pizza. It will have chicken, mushrooms, tomatoes and parmesan cheese",
        "I can offer you farmer's pizza. It will have chicken, mushrooms, tomatoes and parmesan cheese in it"
    ],
    {"hint":"| <i>Подсказка</i>☝️: используйте <b><u>to offer, farmer's pizza</u></b> |"}),
    ("Отлично! Нам подходит!",
    [
        "Great! It suits us!",
        "Fine! It suits us!",
        "Splendid! It suits us!"
    ]),
    ("Ожидайте пиццу через полчаса. Приятного аппетита!",
    [
        "Expect pizza in half an hour. Have a nice meal(enjoy your meal/food)!",
        "Expect pizza in 30 minutes. Enjoy your meal!",
        "Expect pizza in half an hour. Have a nice meal!",
        "Expect pizza in 30 minutes. Have a nice meal!",
        "Expect pizza in 30 minutes. Enjoy your food!",
        "Expect pizza in half an hour. Enjoy your food!",
    ])
]





topic_easy3 = [
    """
    - Добрый день! У меня с утра болит голова. Что вы можете мне предложить?
    - Здравствуйте! Вы мерили ваше давление? - Нет, у меня нет возможности.
    - Вы можете это сделать у нас в аптеке. - Пожалуйста, присядьте здесь и протяните мне правую руку.
    - Ваше давление в норме. Без рецепта врача могу вам предложить «ибупрофен».
    - Я раньше никогда не принимала его. - Это хорошее лекарство и оно поможет вам в течение 15 минут.
    - Можно мне еще бутылку воды. - Конечно! Все вместе вышло на сумму 2 доллара 80
    - Вот, возьмите. - Вот ваше лекарство. Не болейте!
    """,
    ("Добрый день! У меня с утра болит голова. Что вы можете мне предложить?",
    [
        "Good afternoon! I have a headache from the morning. What can you offer?",
        "Good afternoon! I have got a headache from the morning. What can you offer?",
        "Good afternoon! I've got a headache from the morning. What can you offer?",
        "Good afternoon! I have a headache since the morning. What can you offer?",
        "Good afternoon! I have got a headache since the morning. What can you offer?",
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
        "Hello! Did you measure your blood pressure",
        "Good afternoon! Did you measure your blood pressure",
        "Hello! Have you measured your blood pressure",
        "Good afternoon! Have you measured your blood pressure",
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
    {"hint": hlink("Разница между hand и arm", "http://surl.li/eeamc")}),
    ("А",
    [
        "A"
    ]),
    ("б",
    [
        "b"
    ]),
    ("Л",
    [
        "l"
    ]),
    ("о",
    [
        "o"
    ]),
    ("ф",
    [
        "f"
    ])
]