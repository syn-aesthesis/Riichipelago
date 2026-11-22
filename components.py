from worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    from .client.launch import launch_client

    launch(launch_client, name="Riichipelago Client", args=args)

components.append(
    Component(
        "Riichipelago Client",
        func=run_client,
        component_type=Type.CLIENT,
    )
)