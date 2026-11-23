import asyncio
import logging
from argparse import Namespace
from typing import Any

import Utils
from CommonClient import CommonContext, ClientCommandProcessor, server_loop, logger
from NetUtils import ClientStatus
from MultiServer import mark_raw


game_logger = logging.getLogger("Riichipelago")

class RiichiCommandProcessor(ClientCommandProcessor):
    @mark_raw
    def _cmd_check(self, name: str = "") -> bool:
        """Send check from client"""
        from ..world import RiichipelagoWorld
        location_id = RiichipelagoWorld.location_name_to_id.get(name)
        if not name:
            self.output("Usage: /check <location name>")
            return False
        elif location_id is None:
            self.output(f"Unknown location: {name}")
            return False
        self.ctx.complete_location(location_id)
        return True

    def _cmd_goal(self) -> bool:
        """Send goal from client"""
        self.ctx.complete_goal()
        return True


class RiichiContext(CommonContext):
    game = "Riichipelago"
    items_handling = 0b111

    want_slot_data = True
    slot_data: dict[str, Any]

    items_processed_counter: int

    command_processor = RiichiCommandProcessor
    def __init__(
        self,
        server_address: str | None = None,
        password: str | None = None
    ) -> None:
        super().__init__(server_address, password)

        self.slot_data = {}
        self.items_processed_counter = 0
        self.received_item_names: list[str] = []

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict[str, Any]) -> None:
        logger.info(f"cmd: {cmd}")

        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            logger.info(f"slot_data: {self.slot_data}")
        elif cmd == "ReceivedItems":
            new_items = self.items_received[self.items_processed_counter:]
            for item in new_items:
                logger.info(f"{self.item_names.lookup_in_game(item.item)} from {self.player_names[item.player]}")
                self.received_item_names.append(self.item_names.lookup_in_game(item.item))
            self.items_processed_counter += len(new_items)
            self.refresh_ui()

    def refresh_ui(self) -> None:
        if self.ui is not None and hasattr(self.ui, "progress_view"):
            self.ui.progress_view.refresh(self.received_item_names)

    def reset_session_state(self) -> None:
        super().reset_session_state()
        self.slot_data = {}
        self.items_processed_counter = 0
        self.received_item_names = []

    def complete_location(self, location_id: int) -> None:
        self.locations_checked.add(location_id)
        Utils.async_start(self.check_locations({location_id}))

    def complete_goal(self) -> None:
        self.finished_game = True
        Utils.async_start(self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}]))

    def make_gui(self):
        from .gui import RiichiManager
        return RiichiManager


async def main(args: Namespace) -> None:
    ctx = RiichiContext(args.connect, args.password)
    ctx.auth = args.name
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    if Utils.gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()