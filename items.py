from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
if TYPE_CHECKING:
    from .world import RiichipelagoWorld

from .data import ITEMS, ITEM_NAME_TO_ID

class RiichipelagoItem(Item):
    game = "Riichipelago"

def get_random_filler_item_name(world: RiichipelagoWorld) -> str:
    # if world.random.randint(0, 99) < world.options.trap_chance:
    #     return "Trap"
    return "Filler"

def create_item_with_correct_classification(world: RiichipelagoWorld, name: str) -> RiichipelagoItem:
    if name == "Trap":
        classification = ItemClassification.trap
    elif name == "Filler":
        classification = ItemClassification.filler
    else:
        classification = ItemClassification.progression

    return RiichipelagoItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: RiichipelagoWorld) -> None:
    itempool: list[Item] = [
        world.create_item(item) for item in ITEMS.values()
    ]

    num_items = len(itempool)
    num_unfilled = len(world.multiworld.get_unfilled_locations(world.player))
    num_filler_items = num_unfilled - num_items

    itempool += [world.create_filler() for _ in range(num_filler_items)]

    world.multiworld.itempool += itempool


