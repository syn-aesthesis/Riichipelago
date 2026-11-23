# Riichipelago

An [Archipelago Multiworld](https://github.com/ArchipelagoMW/Archipelago) implementation for Japanese Mahjong

- **Status:** In development, not playable
- **Latest release:** None


## Client installation guide

1. Download the latest released apworld file.
2. Install the apworld by double-clicking on the apworld file, or by using the `Install APWorld` component in the Archipelago Launcher.
3. Open (or restart) the Archipelago Launcher. The `Riichipelago Client` should now be listed as a component.


## About this AP implementation

What abilities does the player start with?
- At game start, the player can only call `Riichi` and `Tsumo`
- At game start, the player can only win a hand if their hand contains one of the following yaku: `Riichi`, `Double Riichi`, `Menzen Tsumo`, `Tanyao`  

What "items" can you receive in this game?
- All other calls (`Ron`, `Chi`, `Pon`, `Kan`) and yaku (e.g. `Pinfu`, `Yakuhai`, `Toitoi`, `Honitsu`) will be unlockable through items received from the multiworld.

What count as "checks" in this game?
- Milestones such as winning a hand, finishing a hanchan, or finishing in 1st place will be implemented as checks.


## AI usage disclosure

- This implementation's apworld and client are hand-coded.
- This implementation does not contain any AI-generated media assets.
- I have used AI functionalities of IDEs for code completion, linting, and refactoring.
- I have used Claude Opus 5.5 to scaffold my learning of CommonClient and Kivy, and to aid in debugging.
- This implementation uses and partially reproduces the [MahjongCLI](https://github.com/YarrowRen/MahjongCLI) engine, which was written using Claude Opus 4.6. I have checked all components included here for desired and non-malicious functionality, and take full responsibility for its use in this implementation.


## Contributing

Bug reports, design suggestions, and other inputs related to this AP implementation are welcome in the Riichipelago thread on the Archipelago Discord server.


## Credits

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago) by the Archipelago team
- [Kivy](https://github.com/kivy/kivy) by the Kivy team
- [MahjongCLI](https://github.com/YarrowRen/MahjongCLI) by YarrowRen
- [Riichi Mahjong Tiles](https://github.com/FluffyStuff/riichi-mahjong-tiles/tree/master) by FluffyStuff
