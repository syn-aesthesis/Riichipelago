from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import RiichipelagoWorld

from .data import REGIONS, REGION_CONNECTIONS

def create_and_connect_regions(world: RiichipelagoWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: RiichipelagoWorld) -> None:
    regions: list[Region] = []
    for region_name in REGIONS:
        regions.append(Region(region_name, world.player, world.multiworld))

    world.multiworld.regions += regions

def connect_regions(world: RiichipelagoWorld) -> None:
    regions: dict[str, Region] = {}
    for region_name in REGIONS:
        regions[region_name] = world.get_region(region_name)

    # define Entrance connections between regions
    for src, dst in REGION_CONNECTIONS:
        regions[src].connect(regions[dst], f"{src} to {dst}")