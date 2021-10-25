from tqdm import tqdm

from utils import (
    download_gif,
    load_pokemons_list,
    save_download_info
)

pokemons = load_pokemons_list()
info_normal = {}
info_shiny = {}

pbar = tqdm(pokemons)
for pokemon in pbar:
    pbar.set_description(pokemon)

    status_normal = download_gif(pokemon)
    info_normal[pokemon] = status_normal

    status_shiny = download_gif(pokemon, 'ani-shiny')
    info_shiny[pokemon] = status_shiny

save_download_info(info_normal, 'normal')
save_download_info(info_shiny, 'shiny')