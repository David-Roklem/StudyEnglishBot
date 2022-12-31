from aiogram.utils.markdown import hlink


topic_hard1 = [
    """
    Приготовить классический бисквит. Все продукты должны быть комнатной температуры.
    Ингредиенты: куриные яйца - 4 шт,  сахар - 150 грамм,
    ванильный сахар - чайная ложка, сливочное масло - 100 грамм, пшеничная мука - 150 грамм.
    Отделить белки от желтков и взбить до пены. Добавить сахар, а ванильный сахар - взбить.
    Затем добавить желтки и снова взбить. К получившейся массе добавить масло и муку, затем взбить.
    Форму смазать маслом и залить в него тесто. Отправить в духовку, разогретую до 180 градусов, на 20-25 минут.
    Не открывать духовку первые 15-20 минут.
    """,
    ("Приготовить классический бисквит",
    [
        "Cook classic sponge cake",
        "Cook classical sponge cake",
        "Prepare classic sponge cake",
        "Prepare classical sponge cake",
        "Make classic sponge cake",
        "Make classical sponge cake"
    ],
    {"hint": "sponge cake"}),
    ("Все продукты должны быть комнатной температуры",
    [
        "All the food must be of room temperature",
        "All the food must be at room temperature",
        "All the foods must be at room temperature",
        "All food must be at room temperature",
        "All foods must be at room temperature",
        "All the foods must be of room temperature",
        "All food must be of room temperature",
        "All foods must be of room temperature",
        "All the food should be at room temperature",
        "All the foods should be at room temperature",
        "All food should be at room temperature",
        "All foods should be at room temperature",
        "All the food should be of room temperature",
        "All the foods should be of room temperature",
        "All food should be of room temperature",
        "All foods should be of room temperature",
        "All the food have to be at room temperature",
        "All the foods have to be at room temperature",
        "All food have to be at room temperature",
        "All foods have to be at room temperature",
        "All the food have to be of room temperature",
        "All the foods have to be of room temperature",
        "All food have to be of room temperature",
        "All foods have to be of room temperature",
        "All the food ought to be at room temperature",
        "All the foods ought to be at room temperature",
        "All food ought to be at room temperature",
        "All foods ought to be at room temperature",
        "All the food ought to be of room temperature",
        "All the foods ought to be of room temperature",
        "All food ought to be of room temperature",
        "All foods ought to be of room temperature",
        "All the food have got to be at room temperature",
        "All the foods have got to be at room temperature",
        "All food have got to be at room temperature",
        "All foods have got to be at room temperature",
        "All the food have got to be of room temperature",
        "All the foods have got to be of room temperature",
        "All food have got to be of room temperature",
        "All foods have got to be of room temperature"
    ],
    {"hint": "food"}),
    (
    """
    Ингредиенты: куриные яйца - 4 шт,  сахар - 150 грамм,
    ванильный сахар - чайная ложка, сливочное масло - 100 грамм, пшеничная мука - 150 грамм
    """,
    [
        """
        Ingredients: chicken eggs - 4 pcs, sugar - 150 grams,
        vanilla sugar - a tea spoon, butter - 100 grams, wheat flour - 150 grams
        """,
        """
        Ingredients: chicken eggs - 4 pcs, sugar - 150 grams,
        vanilla sugar - one tea spoon, butter - 100 grams, wheat flour - 150 grams
        """
    ],
    {"hint": "pcs, wheat flour"}),
    ("Отделить белки от желтков и взбить до пены",
    [
        "Separate the egg whites from the yolks and beat until foamy",
        "Separate the egg whites from the yolks and whip until foamy",
        "Separate the egg whites from the yolks and beat up until foamy",
        "Separate the egg whites from the yolks and shake up until foamy",
        "Separate the egg whites from the yolks and shake until foamy",
        "Set apart the egg whites from the yolks and beat until foamy",
        "Set apart the egg whites from the yolks and whip until foamy",
        "Set apart the egg whites from the yolks and beat up until foamy",
        "Set apart the egg whites from the yolks and shake up until foamy",
        "Set apart the egg whites from the yolks and shake until foamy",
        "Detach the egg whites from the yolks and beat until foamy",
        "Detach the egg whites from the yolks and whip until foamy",
        "Detach the egg whites from the yolks and beat up until foamy",
        "Detach the egg whites from the yolks and shake up until foamy",
        "Detach the egg whites from the yolks and shake until foamy"
    ],
    {"hint": "the egg whites, the yolks"}),
    ("Добавить сахар, а ванильный сахар - взбить",
    [
        "Add sugar and whip the vanilla sugar",
        "Add sugar and beat the vanilla sugar",
        "Add sugar and shake the vanilla sugar",
        "Add sugar and shake up the vanilla sugar",
        "Add sugar and beat up the vanilla sugar"
    ],
    {"hint": "to add"}),
    ("Затем добавить желтки и снова взбить",
    [
        "Then add the yolks and whip again",
        "Then add the yolks and beat again",
        "Then add the yolks and shake again",
        "Then add the yolks and shake up again",
        "Then add the yolks and beat up again"
    ]),
    ("К получившейся массе добавить масло и муку, затем взбить",
    [
        "Add the butter and the flour to the resulting mass, then beat",
        "Add the butter and the flour to the resulting mass, then whip",
        "Add the butter and the flour to the resulting mass, then beat up",
        "Add the butter and the flour to the resulting mass, then shake",
        "Add the butter and the flour to the resulting mass, then shake up",
        "Add the butter and the flour to the resulting mass, then beat"
    ],
    {"hint": "the"}),
    ("Форму смазать маслом и залить в него тесто",
    [
        "Grease the form with oil and pour the dough into it",
        "Grease the form with oil and pour the dough inside it",
        "Grease the form with oil and pour the pastry into it",
        "Grease the form with oil and pour the pastry inside it"
    ],
    {"hint": "to grease"}),
    ("Отправить в духовку, разогретую до 180 градусов, на 20-25 минут",
    [
        "Send to the oven, preheated to 180 degrees, for 20-25 minutes",
        "Send to the oven, preheated up to 180 degrees, for 20-25 minutes"
    ],
    {"hint": "preheated"}),
    ("Не открывать духовку первые 15 минут",
    [
        "Do not open the oven for the first 15 minutes",
        "Don't open the oven for the first 15 minutes",
        "Do not open the oven for the initial 15 minutes",
        "Don't open the oven for the initial 15 minutes",
        "Do not open the oven for the primary 15 minutes",
        "Don't open the oven for the primary 15 minutes",
        "Do not open the oven for the primal 15 minutes",
        "Don't open the oven for the primal 15 minutes",
        "Do not open the oven during the first 15 minutes",
        "Don't open the oven during the first 15 minutes",
        "Do not open the oven during the initial 15 minutes",
        "Don't open the oven during the initial 15 minutes",
        "Do not open the oven during the primary 15 minutes",
        "Don't open the oven during the primary 15 minutes",
        "Do not open the oven during the primal 15 minutes",
        "Don't open the oven during the primal 15 minutes",
        "Do not open the oven within the first 15 minutes",
        "Don't open the oven within the first 15 minutes",
        "Do not open the oven within the initial 15 minutes",
        "Don't open the oven within the initial 15 minutes",
        "Do not open the oven within the primary 15 minutes",
        "Don't open the oven within the primary 15 minutes",
        "Do not open the oven within the primal 15 minutes",
        "Don't open the oven within the primal 15 minutes"
    ])
]
