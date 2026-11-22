import asyncio
from argparse import Namespace
from CommonClient import CommonContext, server_loop

class RiichiContext(CommonContext):
    game = "Riichipelago"
    items_handling = 0b111
    want_slot_data = True

    def __init__(
        self,
        server_address: str | None = None,
        password: str | None = None
    ) -> None:
        super().__init__(server_address, password)

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game=self.game)


async def main(args: Namespace) -> None:
    ctx = RiichiContext(args.connect, args.password)
    ctx.auth = args.name
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()