import asyncio
import colorama
from collections.abc import Sequence

import Utils
from CommonClient import get_base_parser, handle_url_arg

def launch_client(*args: Sequence[str]) -> None:
    from .context import main

    Utils.init_logging("RiichipelagoClient", exception_logger="Client")

    parser = get_base_parser()
    parser.add_argument("--name")
    parser.add_argument("url", nargs="?")

    launch_args = handle_url_arg(parser.parse_args(args))

    colorama.just_fix_windows_console()

    asyncio.run(main(launch_args))