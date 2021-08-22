import time
from django.utils.deprecation import MiddlewareMixin


class FakeUser:
    # определите у пользователя аттрибуты auth
    def __init__(self, auth=None):
        self.auth = auth


# Необходимо изменить поведение указанных методов.
# Помните про __call__()
class MyMiddleware(MiddlewareMixin):

    def __call__(self, request):
        begin_timestamp = time.time()
        response = self.process_request(request)
        print(f"Время до выполнения запроса: {begin_timestamp}")
        self.process_response(request, response)
        end_timestamp = time.time()
        request.runtime = end_timestamp - begin_timestamp
        print(f"Время после выполнения запроса: {end_timestamp}")
        print(f"Время выполнения запроса: {request.runtime}")
        return response

    def process_request(self, request):
        return self.get_response(request)

    def process_response(self, request, response):

        user = FakeUser()
        if request.auth == 'VALID_TOKEN':
            user.auth = True
            request.auth = True
        else:
            user.auth = False
            request.auth = False

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





