import requests
import time

def find_uk_city(coordinates:list) -> str:
    url = 'https://geocode.maps.co/reverse'
    cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    for lat, lon in coordinates:
        param = {'lat': lat, 'lon': lon}
        result = requests.get(url, params=param).json()
        time.sleep(11)
        if result['address']['city'] in cities:
            print(result['address']['city'])
            return result['address']['city']
    return 'no_city'

if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'
