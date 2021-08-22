import time

from django.contrib.auth import login, logout
from django.utils.deprecation import MiddlewareMixin


class FakeUser:
    # определите у пользователя аттрибуты auth

    def __init__(self, user):
        self.auth = user.auth


# Необходимо изменить поведение указанных методов.
# Помните про __call__()
class MyMiddleware(MiddlewareMixin):

    def __init__(self, get_response):

        super().__init__(get_response)
        self.get_response = get_response

    def __call__(self, request):

        request.runtime = None

        begin_timestamp = time.time()*1000
        print(f"Время до выполнения запроса: {begin_timestamp}")

        # response = self.get_response(request)

        end_timestamp = time.time()*1000
        request.runtime = (end_timestamp - begin_timestamp)*1000
        print(f"Время после выполнения запроса: {end_timestamp}")
        print(f"Время выполнения запроса: {request.runtime}")

        response = self.get_response(request.runtime)
        # if request.runtime <= 0:
        #     raise ValueError('Время выполнения запроса не может быть отрицательным')

        # if request.auth == "VALID_TOKEN":
        #     self.auth = True
        # elif request.auth == 'INVALID_TOKEN':
        #     self.auth = False

        return response

    def process_request(self, request):

        return self.get_response(request)

    def process_response(self, request, response, user):

        if request.auth == "VALID_TOKEN":
            user.auth = True
            login(user)
        elif request.auth == 'INVALID_TOKEN':
            user.auth = False
            logout(user)


        return response


"""
SessionMiddleware - включает поддержку механизма сессий в Django-проекте. 
То есть по Session ID, который передаётся в Cookies, находит данные сессии в бекенде для хранения сессий.
(управляет состоянием сеанса для пользователя)

CsrfViewMiddleware - проверяет запросы с данными от клиента на наличие CSRF-токена, дабы предотвратить подделку запроса
(гарантирует, что токен CSRF присутствует и действителен при отправке формы)

AuthenticationMiddleware - находит по сессии Django-пользователя, подставляя его в поле user объекта request 
(добавить user атрибут к HttpRequest объекту)
"""





