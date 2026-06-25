import random

WORDS = {
    "Programming": {
        "Easy": [
            "python",
            "string",
            "loop",
            "array",
            "class"
        ],
        "Medium": [
            "algorithm",
            "function",
            "database",
            "debugging",
            "variable"
        ],
        "Hard": [
            "polymorphism",
            "encapsulation",
            "multithreading",
            "inheritance",
            "serialization"
        ]
    },

    "Countries": {
        "Easy": [
            "india",
            "japan",
            "china",
            "spain",
            "italy"
        ],
        "Medium": [
            "australia",
            "singapore",
            "thailand",
            "argentina",
            "indonesia"
        ],
        "Hard": [
            "kazakhstan",
            "madagascar",
            "switzerland",
            "mozambique",
            "liechtenstein"
        ]
    },

    "Animals": {
        "Easy": [
            "tiger",
            "zebra",
            "panda",
            "horse",
            "camel"
        ],
        "Medium": [
            "kangaroo",
            "elephant",
            "dolphin",
            "penguin",
            "alligator"
        ],
        "Hard": [
            "chimpanzee",
            "hippopotamus",
            "orangutan",
            "rhinoceros",
            "crocodile"
        ]
    },

    "Movies": {
        "Easy": [
            "avatar",
            "frozen",
            "jaws",
            "shrek",
            "rocky"
        ],
        "Medium": [
            "inception",
            "interstellar",
            "gladiator",
            "parasite",
            "whiplash"
        ],
        "Hard": [
            "oppenheimer",
            "casablanca",
            "goodfellas",
            "memento",
            "amelie"
        ]
    },

    "Sports": {
        "Easy": [
            "cricket",
            "tennis",
            "soccer",
            "boxing",
            "hockey"
        ],
        "Medium": [
            "badminton",
            "baseball",
            "wrestling",
            "swimming",
            "gymnastics"
        ],
        "Hard": [
            "powerlifting",
            "equestrian",
            "triathlon",
            "snowboarding",
            "synchronized"
        ]
    }
}


def get_categories():

    return list(WORDS.keys())


def get_difficulties():

    return ["Easy", "Medium", "Hard"]


def get_random_word(category, difficulty):

    return random.choice(
        WORDS[category][difficulty]
    ).upper()