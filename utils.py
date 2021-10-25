import json, requests

def load_pokemons_list():
    '''Carrega lista de pokémons do arquivo .json'''
    file_path = './pokemon_list.json'
    f = open(file_path)
    pokemons = json.load(f)
    return pokemons


def download_gif(pokemon: str, suffix='ani'):
    '''Baixa arquivo .gif e retorna status de download'''
    base_url = 'https://play.pokemonshowdown.com/sprites/%s/'

    url_gif = base_url % suffix + pokemon
    # print(url_gif)

    try:
        response = requests.get(url_gif, allow_redirects=True)
        open(fr'./gifs/{ suffix }/{ pokemon }', 'wb').write(response.content)
        status = 'SUCCESS'
    except:
        status = 'ERRO'

    return status


def save_download_info(info: list, suffix: str):
    '''Salva informação de download'''
    with open(f'download_info_{ suffix }.json', 'w') as fp:
        json.dump(info, fp)
