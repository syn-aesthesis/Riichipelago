from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
# from . import options as riichipelago_options
class RiichipelagoWorld(World):
    """
    Riichipelago is a single-player Japanese mahjong experience.
    Mahjong causes great damage to the human spirit without a single benefit.
    """

    game = "Riichipelago"

    web = web_world.RiichipelagoWebWorld()

    # options_dataclass = riichipelago_options.RiichipelagoOptions
    # options: riichipelago_options.RiichipelagoOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Start"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.RiichipelagoItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
            "test": True,
        }
        return slot_data
