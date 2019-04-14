import requests
from random import randint as r

API_ID = '6786b5ca'
API_KEY = '466703f5de7e193922f8f308719ade96'
LANG = 'en'
URL = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + LANG + '/registers=Rare;'

'''
    OxfordRequest retrieves a list of words from the Oxford Dictionary API.
    Allows the user to get a random word from that particular word list.
    @author Pedro Luis Rivera Gomez
    @date April 13, 2019
'''

class OxfordRequest:
    def __init__(self):
        self.dictionary = requests.get(URL, headers = {'app_id': API_ID, 'app_key': API_KEY})
        self.dictionary =self.dictionary.json()
        self.total_words = len(self.dictionary["results"])

    def get_random_word(self):
        random = r(0, self.total_words - 1)
        return self.dictionary["results"][random]["word"]

if __name__ == "__main__":
    request = OxfordRequest()
    print(request.get_random_word())