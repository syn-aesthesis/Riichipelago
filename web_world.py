from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class RiichipelagoWebWorld(WebWorld):
    game = "Riichipelago"

    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Riichipelago for Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["synaesthesis"]
    )

    tutorials = [setup_en]