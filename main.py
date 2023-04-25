import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://meow.senither.com/v1/random'
API_FOX_URL: str = 'https://randomfox.ca/floof/'
BOT_TOKEN: str = ''
TEXT: str = ' это конечно хорошо, но как на счет лисички?'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
MAX_COUNTER: int = 1000

offset: int = -2
counter: int = 0
chat_id: int
first_name: str


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            Update_TEXT = result['message']['text']
            first_name = result['message']['from']['first_name']
            cat_response = requests.get(API_FOX_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['image']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={first_name}, "{Update_TEXT}"{TEXT}')
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
