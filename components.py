from worlds.LauncherComponents import Component, Type, components, launch, icon_paths

def run_client(*args: str) -> None:
    from .client.launch import launch_client

    launch(launch_client, name="Riichipelago Client", args=args)

icon_paths["riichipelago"] = f"ap:{__package__}/assets/icon-48px.png"

components.append(
    Component(
        "Riichipelago Client",
        func=run_client,
        component_type=Type.CLIENT,
        icon="riichipelago"
    )
)