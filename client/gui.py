from kvui import GameManager

from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.image import Image

import logging
from .assets import read_bytes, tile_texture

class ProgressView(MDScrollView):
    def refresh(self, lines: list[str]) -> None:
        rows = self.ids.rows
        rows.clear_widgets()
        for line in lines:
            rows.add_widget(MDLabel(text=line, size_hint_y=None, height=28))


Builder.load_string(read_bytes("assets/riichi.kv").decode("utf-8"))


class RiichiManager(GameManager):
    base_title = "Riichipelago Client"
    logging_pairs = GameManager.logging_pairs + [
        ("Riichipelago", "Game Log")
    ]
    progress_view: ProgressView

    def build(self):
        container = super().build()

        # logging.getLogger("Riichipelago").info(f"Man1.png: {len(read_bytes("assets/tiles/Man1.png"))}")
        # tiles = MDBoxLayout(orientation="horizontal")
        # for name in [f"{i}m" for i in range(1, 10)]:
        #     tiles.add_widget(
        #         Image(texture=tile_texture(name),
        #         size_hint=(None, None),
        #         size=(60, 80),
        #         fit_mode="contain")
        #     )
        # self.add_client_tab("Tiles", tiles)

        self.progress_view = ProgressView()
        self.add_client_tab("Progress", self.progress_view)
        self.ctx.refresh_ui()

        return container