from pygame import load

def load_sprite(name, with_alpha=True):
    path = f'assets/sprites/{name}.ping'
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()

    return loaded_sprite.convert()