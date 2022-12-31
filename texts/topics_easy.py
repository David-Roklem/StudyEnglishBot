from aiogram.utils.markdown import hlink


# First element of the list is a whole text
a_room_for_one_night = [
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
    {"hint": "in advance"}),
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
    {"hint": "separately"}),
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
        "With debit card, please",
        "Debit card, please"
    ]),
    ("Вот платежный терминал",
    [
        "Here is the payment terminal",
        "Here's the payment terminal"
    ])
]





ordering_pizza_into_a_hotel = [
    """
    - Я очень устала, но так хочу есть! 
    - Давай закажем пиццу прямо в отель.
    - Хорошая идея! Я хочу, чтобы она была с грибами, а еще много сыра.
    - Здравствуйте! Можно заказать пиццу в отель?
    - Добрый день! Скажите, пожалуйста, ваш адрес, я проверю, доставляем ли мы туда.
    - Да, мы сможем осуществить доставку за 30 минут. Какую пиццу вы бы хотели?
    - Я бы хотела в ней побольше сыра и грибов.
    - Я могу вам предложить пиццу «фермерская». В ней будут, курица, грибы, томаты и сыр пармезан.
    - Отлично! Нам подходит!
    - Ожидайте пиццу через полчаса. Приятного аппетита!
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
    {"hint": "be exhausted"}),
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
    {"hint": "right into"}),
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
    {"hint": "to wish"}),
    ("Здравствуйте! Можно заказать пиццу в отель?",
    [
        "Hello! Can I order a pizza to a hotel?",
        "Hello! Can I order a pizza into a hotel?"
    ]),
    ("Добрый день! Скажите, пожалуйста, ваш адрес, я проверю, доставляем ли мы туда.",
    [
        "Good day! Tell me, please, your address, I'll check if we deliver there.",
        "Good afternoon! Tell me, please, your address, I'll check if we deliver there.",
        "Good day! Tell me, please, your address, I will check if we deliver there.",
        "Good afternoon! Tell me, please, your address, I will check if we deliver there.",
        "Good day! Tell me, please, your address, I'll check if we deliver there.",
        "Good afternoon! Tell me, please, your address, I'll check if we deliver there.",
        "Good day! Tell me, please, your address, I will check if we deliver there.",
        "Good afternoon! Tell me, please, your address, I will check if we deliver there."
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
    {"hint": "would"}),
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
    {"hint": "to offer, farmer's pizza"}),
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





decoration_of_a_Christmas_tree = [
    """
    - Анна, ты уже нарядила свою ёлку? - Нет. Я в этом году лечу к родителям. Меня не будет целый месяц.
    - Однако они об этом не знают. Я готовлю сюрприз. - Здорово! Расскажи поподробнее об этом.
    - Я переоденусь в Деда Мороза и приду с подарками. - Что ты им купила?
    - Маме и сестре я везу перчатки, а папе - шарф. - Где они проживают?
    - Они живут в Сочи. Но я планирую снять домик в горах для всей семьи.
    - Здорово! Я желаю вам хорошего отдыха и счастливого Рождества!
    """,
    ("Анна, ты уже нарядила свою ёлку?",
    [
        "Anna, did you decorate your Christmas tree?",
        "Anna, have you decorated your Christmas tree?",
        "Anna, did you dress uo your Christmas tree?",
        "Anna, have you dressed up your Christmas tree?"
    ],
    {"hint": "Christmas tree"}),
    ("Нет. Я в этом году лечу к родителям. Меня не будет целый месяц",
    [
        "No. I am flying to my parents this year. I am going to be away for a whole month",
        "No. I'm flying to my parents this year. I am going to be away for a whole month",
        "No. I'm flying to my parents this year. I'm going to be away for a whole month",
        "No. I am flying to my parents this year. I'm going to be away for a whole month",
        "No. I am flying to my parents this year. I will be gone for a whole month",
        "No. I'm flying to my parents this year. I'll be gone for a whole month",
        "No. I'm flying to my parents this year. I will be gone for a whole month",
        "No. This year I am flying to my parents. I am going to be away for a whole month",
        "No. This year I am flying to my parents. I'll be gone for a whole month",
        "No. This year I'm flying to my parents. I am going to be away for a whole month",
        "No. This year I'm flying to my parents. I'm going to be away for a whole month",
        "No. This year I am flying to my parents. I'm going to be away for a whole month",
        "No. This year I am flying to my parents. I will be gone for a whole month",
        "No. This year I'm flying to my parents. I'll be gone for a whole month",
        "No. This year I'm flying to my parents. I will be gone for a whole month",
        "No. This year I am flying to my parents. I'll be gone for a whole month",
    ]),
    ("Однако они об этом не знают. Я готовлю сюрприз",
    [
        "However they do not know about that. I am preparing a surprise",
        "However they don't know about that. I am preparing a surprise",
        "However they don't know about that. I'm preparing a surprise",
        "However they do not know about that. I'm preparing a surprise",
        "However they do not know about it. I am preparing a surprise",
        "However they don't know about it. I am preparing a surprise",
        "However they don't know about it. I'm preparing a surprise",
        "However they do not know about it. I'm preparing a surprise",
    ],
    {"hint": "However"}),
    ("Здорово! Расскажи поподробнее об этом",
    [
        "Awesome. Tell me more about it"
    ],
    {"hint": "awesome"}),
    ("Я переоденусь в Деда Мороза и приду с подарками",
    [
        "I will dress up as Father Christmas and come with presents",
        "I will dress up as Father Christmas and come with gifts",
        "I'll dress up as Father Christmas and come with presents",
        "I'll dress up as Father Christmas and come with gifts",
        "I will dress up as Father Christmas and will come with presents",
        "I will dress up as Father Christmas and will come with gifts",
        "I'll dress up as Father Christmas and will come with presents",
        "I'll dress up as Father Christmas and will come with gifts",
    ],
    {"hint": "will, to dress up as, Father Christmas"}),
    ("Что ты им купила?",
    [
        "What did you buy for them?",
        "What did you buy them?",
        "What have you bought for them?",
        "What have you bought them?",
        "What've you bought for them?",
        "What've you bought them?",
    ]),
    ("Маме и сестре я везу перчатки, а папе - шарф",
    [
        "I am bringing gloves to my mom and sister, and a scarf to dad",
        "I am bringing gloves to my mother and sister, and a scarf to father",
        "I'm bringing gloves to my mom and sister, and a scarf to dad",
        "I'm bringing gloves to my mother and sister, and a scarf to father",
        "I am bringing gloves for my mom and sister, and a scarf to dad",
        "I am bringing gloves for my mother and sister, and a scarf to father",
        "I'm bringing gloves for my mom and sister, and a scarf to dad",
        "I'm bringing gloves for my mother and sister, and a scarf to father",
        "I am bringing gloves to mom and sister, and a scarf to dad",
        "I am bringing gloves to mother and sister, and a scarf to father",
        "I'm bringing gloves to mom and sister, and a scarf to dad",
        "I'm bringing gloves to mother and sister, and a scarf to father",
        "I am bringing gloves for mom and sister, and a scarf to dad",
        "I am bringing gloves for mother and sister, and a scarf to father",
        "I'm bringing gloves for mom and sister, and a scarf to dad",
        "I'm bringing gloves for mother and sister, and a scarf to father",
    ]),
    ("Где они проживают?",
    [
        "Where do they reside?",
    ],
    {"hint": "to reside"}),
    ("Они живут в Сочи. Но я планирую снять домик в горах для всей семьи",
    [
        "They live in Sochi. But I am planning to rent a lodge in the montains for the whole family",
        "They reside in Sochi. But I am planning to rent a lodge in the montains for the whole family",
        "They live in Sochi city. But I am planning to rent a lodge in the montains for the whole family",
        "They reside in Sochi city. But I am planning to rent a lodge in the montains for the whole family",
        "They live in Sochi. But I'm planning to rent a lodge in the montains for the whole family",
        "They reside in Sochi. But I'm planning to rent a lodge in the montains for the whole family",
        "They live in Sochi city. But I'm planning to rent a lodge in the montains for the whole family",
        "They reside in Sochi city. But I'm planning to rent a lodge in the montains for the whole family",
    ],
    {"hint": "to be planning to, a lodge"}),
    ("Здорово! Я желаю вам хорошего отдыха и счастливого Рождества!",
    [
        "Great! I wish you good rest and Merry Christmas!",
        "Cool! I wish you good rest and Merry Christmas!",
    ],
    {"hint": "to wish, Merry Christmas"})
]





coming_to_a_new_city = [
    """
    Сегодня я приехал в новый город. Тут холоднее, чем в моём городе.
    Мой друг встретил меня в аэропорту. У моего друга хорошая машина. 
    Прямо сейчас мы едем домой к моему другу. У него очень большая и дружелюбная семья.
    Они живут в центре города. Их квартира находится на девятом этаже.
    Я буду жить в маленькой комнате рядом с кухней. Я очень рад своему отпуску.
    """,
    ("Сегодня я приехал в новый город",
    [
        "Today I have come to a new city",
        "Today I've come to a new city",
        "Today I came to a new city",
        "Today I have come to a new town",
        "Today I've come to a new town",
        "Today I came to a new town"
    ]),
    ("Тут холоднее, чем в моём городе",
    [
        "It is colder here than in my city",
        "It's colder here than in my city",
        "It is colder here than in my town",
        "It's colder here than in my town",
        "Here it is colder than in my city",
        "Here it's colder than in my city",
        "Here it is colder than in my town",
        "Here it's colder than in my town"
    ]),
    ("Мой друг встретил меня в аэропорту",
    [
        "My friend met me at the airport",
    ],
    {"hint": "at"}),
    ("У моего друга хорошая машина",
    [
        "My friend has a good car",
        "My friend has got a good car",
        "My friend's got a good car",
        "My friend has a fine car",
        "My friend has got a fine car",
        "My friend's got a fine car",
        "My friend has a nice car",
        "My friend has got a nice car",
        "My friend's got a nice car",
    ]),
    ("Прямо сейчас мы едем домой к моему другу",
    [
        "Right now we are going to my friend's house",
        "Right now we're going to my friend's house",
        "Right now we are driving to my friend's house",
        "Right now we're driving to my friend's house",
        "Right now we are going to my friend's home",
        "Right now we're going to my friend's home",
        "Right now we are driving to my friend's home",
        "Right now we're driving to my friend's home"
    ],
    {"hint": "friend's"}),
    ("У него очень большая и дружелюбная семья",
    [
        "He has a very big and friendly family",
        "He has got a very big and friendly family",
        "He's got a very big and friendly family",
        "He has a really big and friendly family",
        "He has got a really big and friendly family",
        "He's got a really big and friendly family"
    ]),
    ("Они живут в центре города",
    [
        "They live in the city center",
    ],
    {"hint": "the city center"}),
    ("Их квартира находится на девятом этаже",
    [
        "Their apartment is on the nineth floor",
        "Their flat is on the nineth floor",
        "Their apartment is on the nineth storey",
        "Their flat is on the nineth storey"
    ]),
    ("Я буду жить в маленькой комнате рядом с кухней",
    [
        "I will live in a small room near the kitchen",
        "I will live in a little room near the kitchen",
        "I will live in a small room close to the kitchen",
        "I will live in a little room close to the kitchen",
        "I will live in a small room next door to the kitchen",
        "I will live in a little room next door to the kitchen",
        "I will live in a small room by the kitchen",
        "I will live in a little room by the kitchen",
        "I'll live in a small room near the kitchen",
        "I'll live in a little room near the kitchen",
        "I'll live in a small room close to the kitchen",
        "I'll live in a little room close to the kitchen",
        "I'll live in a small room next door to the kitchen",
        "I'll live in a little room next door to the kitchen",
        "I'll live in a small room by the kitchen",
        "I'll live in a little room by the kitchen",
        "I am going to live in a small room near the kitchen",
        "I am going to live in a little room near the kitchen",
        "I am going to live in a small room close to the kitchen",
        "I am going to live in a little room close to the kitchen",
        "I am going to live in a small room next door to the kitchen",
        "I am going to live in a little room next door to the kitchen",
        "I am going to live in a small room by the kitchen",
        "I am going to live in a little room by the kitchen",
        "I am going to live in a small room near the kitchen",
        "I am going to live in a little room near the kitchen",
        "I am going to live in a small room close to the kitchen",
        "I am going to live in a little room close to the kitchen",
        "I am going to live in a small room next door to the kitchen",
        "I am going to live in a little room next door to the kitchen",
        "I am going to live in a small room by the kitchen",
        "I am going to live in a little room by the kitchen",
        "I'm going to live in a small room near the kitchen",
        "I'm going to live in a little room near the kitchen",
        "I'm going to live in a small room close to the kitchen",
        "I'm going to live in a little room close to the kitchen",
        "I'm going to live in a small room next door to the kitchen",
        "I'm going to live in a little room next door to the kitchen",
        "I'm going to live in a small room by the kitchen",
        "I'm going to live in a little room by the kitchen",
        "I'm going to live in a small room near the kitchen",
        "I'm going to live in a little room near the kitchen",
        "I'm going to live in a small room close to the kitchen",
        "I'm going to live in a little room close to the kitchen",
        "I'm going to live in a small room next door to the kitchen",
        "I'm going to live in a little room next door to the kitchen",
        "I'm going to live in a small room by the kitchen",
        "I'm going to live in a little room by the kitchen",
        "I'm gonna to live in a small room near the kitchen",
        "I'm gonna to live in a little room near the kitchen",
        "I'm gonna to live in a small room close to the kitchen",
        "I'm gonna to live in a little room close to the kitchen",
        "I'm gonna to live in a small room next door to the kitchen",
        "I'm gonna to live in a little room next door to the kitchen",
        "I'm gonna to live in a small room by the kitchen",
        "I'm gonna to live in a little room by the kitchen",
        "I'm gonna to live in a small room near the kitchen",
        "I'm gonna to live in a little room near the kitchen",
        "I'm gonna to live in a small room close to the kitchen",
        "I'm gonna to live in a little room close to the kitchen",
        "I'm gonna to live in a small room next door to the kitchen",
        "I'm gonna to live in a little room next door to the kitchen",
        "I'm gonna to live in a small room by the kitchen",
        "I'm gonna to live in a little room by the kitchen"
    ]),
    ("Я очень рад своему отпуску",
    [
        "I am very happy about my vacation",
        "I'm very happy about my vacation",
        "I am really happy about my vacation",
        "I'm really happy about my vacation",
        "I am very happy about my holiday",
        "I'm very happy about my holiday",
        "I am really happy about my holiday",
        "I'm really happy about my holiday"
    ],
    {"hint": "be happy about"})
]
