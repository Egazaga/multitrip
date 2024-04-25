from itertools import chain

__bans_dict = {
    "jew_bans": [
        "Iran",
        "Lebanon",
        "Syria",
        "Yemen",
        "Palestinian Territories",
        "Iraq",
        "Afghanistan",
        "Somalia",
        "Sudan",
        "Libya",

        "Saudi Arabia",
        "Kuwait",
        "Pakistan",
        "Malaysia",
        "Brunei",
        "Bangladesh",
        "Algeria"
    ],

    "goida_bans": [
        "Poland",
        "Russian Federation",
        "Ukraine",
        "Türkiye"
    ],

    "other_bans": [
        "Albania"
    ]
}

banned_countries = set(chain(*__bans_dict.values()))
