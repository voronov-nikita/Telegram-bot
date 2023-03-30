import requests

# Задаем URL-адрес для отправки запроса на авторизацию
token = "?bo=%2Fsps%2Foauth%2Fae%3Fresponse_type%3Dcode%26access_type%3Doffline%26client_id%3Ddnevnik.mos.ru%26scope%3Dopenid%2Bprofile%2Bbirthday%2Bcontacts%2Bsnils%2Bblitz_user_rights%2Bblitz_change_password%26redirect_uri%3Dhttps%253A%252F%252Fschool.mos.ru%252Fv3%252Fauth%252Fsudir%252Fcallback"
url = f'https://login.mos.ru/sps/login/methods/password{token}'

# Задаем данные для отправки POST-запроса
payload = {'login': '', 'password': ''}

res = requests.get("https://dnevnik.mos.ru/diary/homeworks/homeworks")
print(res.text)
# Отправляем POST-запрос на авторизацию
r = requests.post(url, data=payload)
print(r.status_code)

# Проверяем статус-код ответа (200 означает успешный запрос)
if r.status_code == 200:
    print('Успешная авторизация!')
    # Выводим полученный токен
    res = requests.get("https://dnevnik.mos.ru/diary/homeworks/homeworks")
    # print(res.)
else:
    print('Ошибка авторизации')
