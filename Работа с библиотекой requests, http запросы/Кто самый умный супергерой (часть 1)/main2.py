import requests


def get_the_smartest_superhero() -> str:
    base_url = "https://akabab.github.io/superhero-api/api"
    hulk = 332
    captain_america = 149
    thanos = 655
    max_intelligence = 0
    the_smartest_superhero = ''
    for superhero_id in (hulk, captain_america, thanos):
        url = base_url + f"/id/{superhero_id}.json"
        response = requests.get(url)
        info = response.json()
        intelligence = info['powerstats']['intelligence']
        if intelligence > max_intelligence:
            max_intelligence = intelligence
            the_smartest_superhero = info['name']
    print(the_smartest_superhero)
    return the_smartest_superhero


if __name__ == '__main__':
    assert get_the_smartest_superhero() == 'Thanos'