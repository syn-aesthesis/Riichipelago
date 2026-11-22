from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import Has, CanReachLocation

if TYPE_CHECKING:
    from .world import RiichipelagoWorld

from .data import ITEMS, LOCATIONS, ENTRANCE_ITEMS, GOAL_LOCATION

def set_all_rules(world: RiichipelagoWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: RiichipelagoWorld) -> None:
    for entrance, item in ENTRANCE_ITEMS.items():
        world.set_rule(
            world.get_entrance(entrance),
            Has(ITEMS[item])
        )

def set_all_location_rules(world: RiichipelagoWorld) -> None:
    # set location rules for goal
    world.set_rule(
        world.get_location("Goal Condition"),
        CanReachLocation(LOCATIONS[GOAL_LOCATION])
    )

def set_completion_condition(world: RiichipelagoWorld) -> None:
    world.set_completion_rule(Has("Goal"))
