import pkgutil
import io

from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image

WORLD_PACKAGE = __package__.rpartition(".")[0]
cached_tile_names_to_textures = {}

tile_folder = "assets/tiles"  # relative to world
tile_names_to_files = {
    "1m": "Man1.png",
    "2m": "Man2.png",
    "3m": "Man3.png",
    "4m": "Man4.png",
    "5m": "Man5.png",
    "6m": "Man6.png",
    "7m": "Man7.png",
    "8m": "Man8.png",
    "9m": "Man9.png",
    "0m": "Man5-Dora.png",
    "1p": "Pin1.png",
    "2p": "Pin2.png",
    "3p": "Pin3.png",
    "4p": "Pin4.png",
    "5p": "Pin5.png",
    "6p": "Pin6.png",
    "7p": "Pin7.png",
    "8p": "Pin8.png",
    "9p": "Pin9.png",
    "0p": "Pin5-Dora.png",
    "1s": "Sou1.png",
    "2s": "Sou2.png",
    "3s": "Sou3.png",
    "4s": "Sou4.png",
    "5s": "Sou5.png",
    "6s": "Sou6.png",
    "7s": "Sou7.png",
    "8s": "Sou8.png",
    "9s": "Sou9.png",
    "0s": "Sou5-Dora.png",
    "1z": "Ton.png",
    "2z": "Nan.png",
    "3z": "Shaa.png",
    "4z": "Pei.png",
    "5z": "Haku.png",
    "6z": "Hatsu.png",
    "7z": "Chun.png"
}

def read_bytes(resource: str) -> bytes:
    data = pkgutil.get_data(WORLD_PACKAGE, resource)
    if data is None:
        raise FileNotFoundError(resource)
    return data

def tile_texture(name: str):
    if name not in cached_tile_names_to_textures:
        data = read_bytes(f"{tile_folder}/{tile_names_to_files[name]}")
        texture = CoreImage(io.BytesIO(data), ext="png").texture
        cached_tile_names_to_textures[name] = texture
    return cached_tile_names_to_textures[name]
