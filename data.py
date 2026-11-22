REGIONS = [
    "Start",
    "Ron"
]

REGION_CONNECTIONS = [
    ("Start", "Ron"),
]

ITEMS = {
    1001: "Ron",
    1002: "Chi",
    1003: "Pon",
    1004: "Kan",
}
FILLER = {
    101: "Filler",
}
ITEM_NAME_TO_ID = {name: i for i, name in (ITEMS | FILLER).items()}

LOCATIONS = {
    10001: "Win a hand with Tsumo",
    10002: "Win a hand with Ron",
    20001: "Place 3rd or higher",
    20002: "Place 2nd or higher",
    20003: "Place 1st",
}
LOCATION_NAME_TO_ID = {name: i for i, name in LOCATIONS.items()}

REGION_LOCATIONS = {
    "Start":    [10001, 20001, 20002, 20003],
    "Ron":      [10002],
}

ENTRANCE_ITEMS = {
    "Start to Ron": 1001,
}

GOAL_LOCATION = 20003
