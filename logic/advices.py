import json, requests
from pprint import pprint
from translate import Translator

api_url = 'https://api.adviceslip.com/advice'
def get_en_advice(api):
    response = requests.get(api)
    advice = json.loads(response.text)
    return advice['slip']['advice']

def get_ptbr_advice(api=api_url):
    translator = Translator(to_lang='pt-br')
    advice = get_en_advice(api)
    return translator.translate(advice)


if __name__ == '__main__':
    pprint(get_ptbr_advice(api_url))