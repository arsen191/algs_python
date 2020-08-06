"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib


class Sites:
    def __init__(self):
        self.sites = []
        self.salt = uuid4().hex

    def cash(self, site):
        hash_site = hashlib.sha256(
            self.salt.encode() + site.encode('utf-8')).hexdigest() + ':' + self.salt
        if hash_site in self.sites:
            return 'сайт в кэше'    # отладочный принт
        else:
            self.sites.append(hash_site)
            return 'сайт добавлен в кэш'    # для отладки

    def cash_fill(self):
        return self.sites

    def remove_cash(self):
        self.sites.clear()


Cash_site = Sites()
# при посещении новой страницы она складывается в кэш
print(Cash_site.cash('http://vk.com'))
print(Cash_site.cash('http://youtube.com'))
print(Cash_site.cash('http://apple.com'))

# проверяем хэши каких страниц у нас сложились в кэш
print(Cash_site.cash_fill())

# при повторном посещении сайта повторное значение не будет лететь в кэш
print(Cash_site.cash('http://vk.com'))

# очистка собранного кэша
Cash_site.remove_cash()

# еще раз проверяем заполненность кэша
print(Cash_site.cash_fill())
